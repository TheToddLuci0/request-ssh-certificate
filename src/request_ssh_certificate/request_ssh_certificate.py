import os
import logging
import boto3
import json


def request(
    profile: str, region: str, valid_for: int, identity_file: str, lambda_arn: str
):
    session = boto3.Session(profile_name=profile, region_name=region)
    _lambda = session.client("lambda")
    sts = session.client("sts")
    req = sts.generate_presigned_url("get_caller_identity")
    with open(os.path.expanduser(identity_file), "r") as keyfile:
        key = keyfile.read()
    payload = {
        "stsurl": req,
        "length": int(valid_for),
        "pubkey": key,
        "username": os.getlogin(),
    }
    response = _lambda.invoke(FunctionName=lambda_arn, Payload=json.dumps(payload))
    if response["StatusCode"] >= 300:
        print(response["Payload"].read())
        os.exit(11)

    cert = response["Payload"].read()
    cert_file = os.path.expanduser(identity_file).replace(".pub", "-cert.pub")
    if not cert_file.endswith("-cert.pub"):
        logging.error(
            "Something has gone horribly wrong, bailing to not destroy secret keys!"
        )
        os.exit(99)
    logging.info("Writing cert to " + cert_file)
    with open(cert_file, "w") as f:
        f.write(cert.decode("utf-8").replace('"', ""))

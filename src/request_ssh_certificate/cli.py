"""Console script for request_ssh_certificate."""
import argparse
import sys
import configparser
import logging
import os
from request_ssh_certificate.request_ssh_certificate import request


def main():
    """Console script for request_ssh_certificate."""
    config = configparser.ConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--valid-for",
        help="How long the cert should be valid for. Note: if the server has a lower max set than you request, the server will win.",
    )
    parser.add_argument("-i", "--identity-file", help="Public key to sign")
    parser.add_argument("--lambda-arn", help="ARN of the signing lambda")
    parser.add_argument("--profile", help="AWS profile to use")
    parser.add_argument("--region", help="AWS region name (ie us-east-1)")

    # Options for config file
    config_opts = parser.add_argument_group("Config Options")
    config_opts.add_argument(
        "--save",
        action="store_true",
        help="Save the command line args to a config file",
    )
    config_opts.add_argument(
        "-c",
        "--config",
        default="~/.config/ssh-key-sign.ini",
        help="Config file to use",
    )

    args = parser.parse_args()
    config_path = os.path.expanduser(args.config)
    config.read(config_path)
    logging.debug(args.__dict__)
    config.read_dict(
        {"DEFAULT": {k: v for k, v in args.__dict__.items() if v is not None}}
    )
    if args.save:
        logging.info("Writing config to {}".format(config_path))
        # We don't need to save these
        config.remove_option("DEFAULT", "config")
        config.remove_option("DEFAULT", "save")
        with open(config_path, "w+") as conffile:
            config.write(conffile)
    conf = config["DEFAULT"]
    logging.debug(config.__dict__)
    identity_file = conf.get("identity_file")
    region = conf.get("region")
    valid_for = conf.getint("valid_for")
    lambda_arn = conf.get("lambda_arn")
    profile = conf.get("profile")
    if identity_file is None:
        logging.error("Must have a key to sign!")
        os.exit(5)
    return request(
        profile=profile,
        region=region,
        valid_for=valid_for,
        identity_file=identity_file,
        lambda_arn=lambda_arn,
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

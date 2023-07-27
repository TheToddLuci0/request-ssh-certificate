# Request SSH Certificate
<p align="center">

<a href="https://pypi.python.org/pypi/request-ssh-certificate">
<img src="https://img.shields.io/pypi/v/request-ssh-certificate.svg" /></a>
<a href="https://travis-ci.org/TheToddLuci0/request-ssh-certificate"><img src="https://travis-ci.org/TheToddLuci0/request-ssh-certificate.svg?branch=master" /></a>
</p>
Request a SSH certificate from a lambda. This is intended to be used with [SSH-Certificate-CA-lambda](https://github.com/TheToddLuci0/ssh-certificate-CA-lambda).

## Install

`pipx install request-ssh-certificate`

## Useage

```
usage: request-ssh-certificate [-h] [-t VALID_FOR] [-i IDENTITY_FILE] [--lambda-arn LAMBDA_ARN] [--profile PROFILE] [--region REGION] [--save] [-c CONFIG]

options:
  -h, --help            show this help message and exit
  -t VALID_FOR, --valid-for VALID_FOR
                        How long the cert should be valid for. Note: if the server has a lower max set than you request, the server will win.
  -i IDENTITY_FILE, --identity-file IDENTITY_FILE
                        Public key to sign
  --lambda-arn LAMBDA_ARN
                        ARN of the signing lambda
  --profile PROFILE     AWS profile to use
  --region REGION       AWS region name (ie us-east-1)

Config Options:
  --save                Save the command line args to a config file
  -c CONFIG, --config CONFIG
                        Config file to use
```

# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)

# SNS Message Verification

SNS message verification is not included in AWS SDK for Python ([issue](https://github.com/boto/boto3/issues/1469)). AWS documentation only provides [example code in Java](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.example.java.html). This repository provides a Python module that inplements SNS message verification logic based on the official documentation, along with example code of how to use this module to implement an HTTP endpoint for SNS. 


## Prerequisite
- Python >= 3.7

## Development Setup
Download this repo and run `pip install -r requirements.txt`.

## Install
`pip install git+https://github.com/wlwg/sns-message-verification.git`

## Usage
Refer to the example code [`flask_example.py`](flask_example.py) to see how to implement an SNS http endpoint using this package.

## Issues
Feel free to create an issue if you found a bug or have a feature requests.

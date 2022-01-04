# AWS SNS Message Validator

PyPI: https://pypi.org/project/aws-sns-message-validator/ 

## Motivation
An HTTP endpoint for AWS SNS needs to validate the received messages before processing them which involves some non-trivial logic, especially [signature verification](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.verify.signature.html). In terms of implementation, AWS does not offer any help with SNS message validation in their SDK for Python ([issue](https://github.com/boto/boto3/issues/1469)) nor does it provide example code in the documentation (example code is only available [in Java](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.example.java.html)). Therefore Python developers would need to invent their own wheels. 

To solve this problem, this repository offers an SNS message validator which is implemented according to the guide on [the official AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html), and offers [example code](flask_example.py) of how to use it to implement an HTTP endpoint for SNS. 


## Prerequisite
- Python >= 3.6 

## Install
`pip install aws-sns-message-validator`

## Usage
Refer to the example code [`flask_example.py`](flask_example.py) to see how to use this package in your SNS http endpoint. In order to quickly try out the example code, follow the steps below:
- Make sure you have Python>=3.6 installed. (Create a virtual environment if you want to.)
- Checkout this repo and install dev dependencies by `python3 -m pip install -r requirements.txt`
- Run `FLASK_APP=flask_example.py flask run --port=5000` to start an http server.
- Use `ngrok` to expose the local server to the public internet (`./ngrok http -bind-tls=true localhost:5000`). Now you should get a public endpoint (`https://xxxxxxxx.ngrok.io`) that can be set as a subscriber of an SNS topic.

## Issues
Feel free to create an issue if you found a bug or have a feature request.

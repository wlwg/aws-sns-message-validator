# SNS Message Validator

Implementing an HTTP endpoint for AWS SNS involves some non-trivial logic, especially [signature verification](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.verify.signature.html). AWS documentation only provides [example code in Java](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.example.java.html). AWS SDK for Python does not include any helper for SNS message validation ([issue](https://github.com/boto/boto3/issues/1469)) so Python developers would need to invent their own wheels to do that. This repository inplements an SNS message validator based on [the official AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html), and offers example code of how to use it to implement an HTTP endpoint for SNS in Python. 


## Prerequisite
- Python >= 3.7

## Development Setup
Download this repo and run `pip install -r requirements.txt`.

## Install
`pip install git+https://github.com/wlwg/sns-message-validator.git`

## Usage
Refer to the example code [`flask_example.py`](flask_example.py) to see how to use this package in your SNS http endpoint. In order to quickly try out the example code, follow the steps below:
- Make sure you have Python>=3.7 installed. (Create a virtual environment if you want to.)
- Checkout this repo and install dev dependencies by `python3 -m pip install -r requirements.txt`
- Run `FLASK_APP=flask_example.py flask run --port=5000` to start an http server.
- Use `ngrok` to expose the local server to the public internet (`./ngrok http -bind-tls=true localhost:5000`). Now you should get a public endpoint (`https://xxxxxxxx.ngrok.io`) for SNS.

## Issues
Feel free to create an issue if you found a bug or have a feature requests.

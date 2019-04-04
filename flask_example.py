
import logging
import json
import requests
from flask import Flask, request, Response
from sns_message_validator import (
    InvalidMessageTypeException,
    InvalidCertURLException,
    InvalidSignatureVersionException,
    SignatureVerificationFailureException,
    SNSMessageType,
    SNSMessageValidator,
)


APP = Flask(__name__)

@APP.route('/', methods=['POST'])
def main():
    logger = logging.getLogger('view.main')
    sns_message_validator = SNSMessageValidator()

    # Validate message type from header without having to parse the request body.
    message_type = request.headers.get('x-amz-sns-message-type')
    try:
        sns_message_validator.validate_message_type(message_type)
    except InvalidMessageTypeException as ex:
        logger.error(ex)
        return Response('Invalid message type.', status=500)

    try:
        message = json.loads(request.data)
    except json.decoder.JSONDecodeError as ex:
        error_msg = 'Request body is not in json format.'
        logger.error(f'{error_msg} {ex}')
        return Response(error_msg, status=500)

    try:
        sns_message_validator.validate_message(message=message)
    except (InvalidCertURLException, InvalidSignatureVersionException, SignatureVerificationFailureException) as ex:
        logger.error(ex)
        return Response('Invalid message.', status=500)

    if message_type == SNSMessageType.SubscriptionConfirmation.value:
        resp = requests.get(message.get('SubscribeURL'))
        logger.debug(resp)
        if resp.status_code != 200:
            return Response('Subscription confirmation failed.', status=500)
        return Response('Subscription is successfully confirmed.', status=200)

    if message_type == SNSMessageType.UnsubscribeConfirmation.value:
        resp = requests.get(message.get('UnsubscribeURL'))
        if resp.status_code != 200:
            return Response('Subscription confirmation failed.', status=500)
        return Response('Successfully unsubscribed.', status=200)

    logger.debug(message.get('Message')) # replace this with your own business logic of processing the message
    return Response('Message Received.', status=200)

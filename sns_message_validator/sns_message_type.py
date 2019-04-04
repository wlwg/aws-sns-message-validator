import enum


class SNSMessageType(enum.Enum):
    SubscriptionConfirmation = 'SubscriptionConfirmation'
    Notification = 'Notification'
    UnsubscribeConfirmation = 'UnsubscribeConfirmation'

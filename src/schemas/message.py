from marshmallow import Schema
from marshmallow import fields

from constants import MAX_MESSAGE_LENGTH
from constants import MAX_NAMING_LENGTH


class MessageCreateRequestSchema(Schema):
    phoneNumber = fields.Str(required=True, description='Номер телефона, на который нужно отправить SMS',)
    text = fields.Str(required=True, description='Текст SMS сообщения', validate=lambda x: len(x) < MAX_MESSAGE_LENGTH,)
    naming = fields.Str(
        required=False,
        description='Подпись отправителя',
        allow_none=True,
        validate=lambda x: len(x) < MAX_NAMING_LENGTH,
    )


class MessageCreateResponseSchema(Schema):
    messageId = fields.Str(
        required=True, description='Идентификатор сообщения. В дальшейнем по нему можно получить статус сообщения.',
    )
    phoneNumber = fields.Str(required=True, description='Номер телефона, на который нужно отправить SMS',)
    text = fields.Str(required=True, description='Текст SMS сообщения', validate=lambda x: len(x) < MAX_MESSAGE_LENGTH,)

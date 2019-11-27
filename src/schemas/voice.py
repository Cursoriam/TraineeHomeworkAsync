from marshmallow import Schema
from marshmallow import fields


class TranscriptionCreateRequestSchema(Schema):
    filepath = fields.Str(required=True, description='Путь к файлу с образцом речи')


class TranscriptionCreateResponseSchema(Schema):
    text = fields.Str(required=True, description='Транскрибированный из аудио текст')
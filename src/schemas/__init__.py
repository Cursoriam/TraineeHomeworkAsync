from .message import MessageCreateRequestSchema
from .message import MessageCreateResponseSchema
from .voice import TranscriptionCreateRequestSchema
from .voice import TranscriptionCreateResponseSchema

APISPEC_DEFAULT_PARAMS = [
    {'in': 'header', 'name': 'Authorization', 'schema': {'type': 'string'}, 'required': 'true'},
]

__all__ = [
    'APISPEC_DEFAULT_PARAMS',
    'MessageCreateRequestSchema',
    'MessageCreateResponseSchema',
    'TranscriptionCreateRequestSchema',
    'TranscriptionCreateResponseSchema',
]

from .message import MessageCreateRequestSchema
from .message import MessageCreateResponseSchema

APISPEC_DEFAULT_PARAMS = [
    {'in': 'header', 'name': 'Authorization', 'schema': {'type': 'string'}, 'required': 'true'},
]

__all__ = [
    'APISPEC_DEFAULT_PARAMS',
    'MessageCreateRequestSchema',
    'MessageCreateResponseSchema',
]

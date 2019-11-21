from aiohttp_apispec import validation_middleware

from .contextvars import set_context_vars
from .exception import exception_middleware

MIDDLEWARES = [
    set_context_vars,
    exception_middleware,
    validation_middleware,
]

__all__ = ['MIDDLEWARES']

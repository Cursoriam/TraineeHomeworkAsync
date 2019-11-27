from aiohttp_apispec import validation_middleware

from .contextvars import set_context_vars
from .exception import exception_middleware
from .auth import auth_middleware

MIDDLEWARES = [
    set_context_vars,
    exception_middleware,
    validation_middleware,
    auth_middleware,
]

__all__ = ['MIDDLEWARES']

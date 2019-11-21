from .base import BaseAppException
from .base import ServerError


class Forbidden(ServerError):
    status_code = 403
    message = 'Доступ запрещён'


class ValidationError(ServerError):
    status_code = 500
    message = 'Ошибка проверки данных'


class InputValidationError(ServerError):
    status_code = 400
    message = 'Некорректный запрос'


class NotFound(ServerError):
    status_code = 404
    message = 'Ресурс не найден'


class MessageSendingException(ServerError):
    status_code = 500
    message = 'Произошла ошибка во время отправки сообщения'


__all__ = [
    'BaseAppException',
    'Forbidden',
    'ValidationError',
    'InputValidationError',
    'NotFound',
    'MessageSendingException',
]

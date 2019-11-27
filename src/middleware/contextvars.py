from contextvars import ContextVar

from aiohttp import web

REQ_ID = ContextVar('X-Request-Id', default='None')
DEVICE_ID = ContextVar('X-Device-Id', default='None')


@web.middleware
async def set_context_vars(request, handler) -> web.Response:
    """
    Проверят, является ли сессия завершённой
    :param request:
    :param handler:
    """
    REQ_ID.set(request.headers.get('Request-Id', 'None'))
    DEVICE_ID.set(request.headers.get('X-Device-Id', 'None'))
    return await handler(request)

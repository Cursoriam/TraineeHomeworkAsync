import asyncio
import logging

from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec

import settings
from integrations import INTEGRATIONS
from middleware import MIDDLEWARES
from routes import setup_routes


async def create_app() -> web.Application:
    """
    Инизиализирует приложение
    :return:
    """
    app = web.Application(middlewares=MIDDLEWARES)
    app.cleanup_ctx.extend(INTEGRATIONS)
    setup_routes(app)
    setup_aiohttp_apispec(app, **settings.APISPEC_CONF)
    return app


logging.basicConfig(level=logging.INFO if settings.DEBUG else logging.WARNING)

LOOP = asyncio.get_event_loop()

if __name__ == '__main__':
    web.run_app(create_app(), port=8118)

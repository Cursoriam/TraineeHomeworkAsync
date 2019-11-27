from typing import Optional

from aiohttp import web

import exceptions


def check_token(auth_type: str, token: str) -> Optional[dict]:
    """
    Проверяет JWT токен
    :param auth_type:
    :param token:
    :return:
    """
    return dict(data='sample')


@web.middleware
async def auth_middleware(request, handler) -> web.Response:
    """
    Verify token
    :param request:
    :param handler:
    :return:
    """

    auth = request.headers.get('Authorization', '').split()

    if not auth:
        # No token provided at all, skipping. User is not authenticated, but
        # we don't return error, so we can have api methods that not require authentication
        return await handler(request)

    if len(auth) != 2:
        raise exceptions.AuthTypeInvalid()

    auth_type = auth[0]
    token = auth[1]

    user = check_token(auth_type, token)

    setattr(request, 'api_user', user)

    return await handler(request)

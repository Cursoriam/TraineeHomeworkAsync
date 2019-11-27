from collections import Callable

import exceptions

from aiohttp import web
from aiohttp import web_exceptions
from marshmallow import ValidationError as MarshmallowValidationError


@web.middleware
async def exception_middleware(request: web.Request, handler: Callable) -> web.Response:
    """
    Обрабатывает исключения приложения
    :param request: объект запроса
    :param handler: обработчик
    :return: объект ответа
    """
    try:
        response: web.Response = await handler(request)
        return response
    except MarshmallowValidationError as ex:
        exc = exceptions.ValidationError(debug=str(ex), message=exceptions.ValidationError.message)
    except exceptions.BaseAppException as ex:
        exc = ex
    except web_exceptions.HTTPBadRequest as ex:
        exc = exceptions.InputValidationError(debug=ex.text, message=exceptions.InputValidationError.message)
    except web_exceptions.HTTPUnprocessableEntity as ex:
        exc = exceptions.ValidationError(debug=ex.text, message=exceptions.ValidationError.message)
    except web_exceptions.HTTPForbidden as ex:
        exc = exceptions.Forbidden(debug=f'Goodbye Moonmen. {ex}', message=exceptions.Forbidden.message)
    except web_exceptions.HTTPNotFound as ex:
        exc = exceptions.NotFound(debug=ex.text, message=exceptions.NotFound.message)
    except Exception as ex:  # pylint: disable=broad-except
        exc = exceptions.ServerError(debug=str(ex), message=exceptions.ServerError.message)

    exc_data = exc.as_dict()
    exc_data['message'] = exc.message
    exc_data.pop('code', None)
    exc.__init__(**exc_data)

    return web.json_response(exc.as_dict(), status=exc.status_code)

from uuid import uuid4

from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema

from schemas import MessageCreateRequestSchema, APISPEC_DEFAULT_PARAMS
from schemas import MessageCreateResponseSchema
from utils.auth import access_token_required


@docs(
    tags=['SMS'], summary='Запрос отправки сообщения', description='Описание запроса',
    parameters=APISPEC_DEFAULT_PARAMS,
)
@request_schema(MessageCreateRequestSchema)
@response_schema(MessageCreateResponseSchema)
@access_token_required
async def send_message(request):
    """
    Отправляет сообщение
    :param request:
    :return:
    """
    message_id = str(uuid4())
    res = dict(
        phoneNumber=request['data']['phoneNumber'],
        text=request['data']['text'],
        messageId=message_id,
    )

    validated_games_list = MessageCreateResponseSchema().load(res)

    return web.json_response(validated_games_list)

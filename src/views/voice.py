from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema

from integrations.google_speech_to_text import GoogleSTT
from schemas import TranscriptionCreateRequestSchema
from schemas import TranscriptionCreateResponseSchema


@docs(tags=['Voice Transcription'], summary='Запрос отправки сообщения',
      description='Описание запроса')
@request_schema(TranscriptionCreateRequestSchema)
@response_schema(TranscriptionCreateResponseSchema)
async def speechrecognition(request):

    audio_decoded = GoogleSTT.transcript(
        open(request['data']['filepath'], 'rb').read()
    )

    res = dict(text=audio_decoded,)
    text = TranscriptionCreateResponseSchema().load(res)

    return web.json_response(text)
from base64 import b64encode
from json import loads

from requests import post
from requests.exceptions import ConnectionError

from settings import URL
from settings import API_KEY


class GoogleSTT:
    @classmethod
    async def transcript(cls, audio_file: bytes) -> str:
        try:
            req = loads(
                post(URL, params=dict(key=API_KEY, ),
                        json=dict(
                        audio=dict(content=b64encode(audio_file).decode(), ),
                        config=dict(languageCode='en-US', ),
                         )
                     ).text
            )
        except ConnectionError:
            raise ConnectionError('Too many requests')
        print(req)
        try:
            results = req['results']
        except KeyError:
            raise KeyError('No param \'results\'')

        transcripted: str = ''

        for result in results:
            try:
                alternatives = result['alternatives']
            except KeyError:
                raise KeyError('No param \'alternatives\'')

            try:
                alternative = alternatives[0]
            except IndexError:
                raise IndexError('There is no index 0 in dict')

            try:
                transcripted = transcripted+alternative['transcript']
            except KeyError:
                raise KeyError('No param \'transcripted\'')

        return transcripted
import json
from typing import Any
from typing import Mapping
from typing import Optional

from aiohttp.web_exceptions import HTTPError
from marshmallow import Schema
from marshmallow import fields

from settings import DEBUG


class BaseAppException(HTTPError):
    ...


class ServerError(BaseAppException):
    status_code: int = 500
    message: str = 'Что-то пошло не так'
    title: Optional[str] = None
    description: str = ''

    def __init__(self,
                 message: Optional[str] = None,
                 title: Optional[str] = None,
                 payload: Optional[Mapping[str, Any]] = None,
                 debug: Optional[str] = None,
                 exc_code: Optional[str] = None,
                 status_code: Optional[int] = None,
                 ):
        self.title = title or self.title
        self.code = exc_code or self.__class__.__name__
        self.status_code = status_code or self.status_code
        self.message = message or self.message
        self.payload = payload
        self.debug = debug
        super().__init__(
            body=json.dumps(self.as_dict(), ensure_ascii=False), content_type='application/json'
        )

    def as_dict(self) -> dict:
        """
        Преобразует данные класса ошибки в словарь
        :return:
        """
        debug = dict(debug=self.debug) if DEBUG else dict()
        error_body = dict(code=self.code, title=self.title, message=self.message, payload=self.payload, **debug)
        validated_response_data = self.get_schema().load(error_body)
        return validated_response_data

    @classmethod
    def get_schema(cls) -> Schema:
        """
        Возвращает схему исключения
        :return:
        """
        class ExceptionSchema(Schema):
            code = fields.Constant(cls.__name__, example=cls.__name__, description='Код ошибки в PascalCase')
            title = fields.String(
                required=False,
                allow_none=True,
                example=None,
                description='Заголовок ошибки для отображения на клиенте с учетом локализации.',
            )
            message = fields.String(
                required=True, example=cls.message, description='Сообщение об ошибке с учетом локализации.'
            )
            payload = fields.Dict(
                allow_none=True,
                required=True,
                example=None,
                description='Метаданные ошибки, могут содержать любые данные, '
                            'необходимые клиенту для корректной обработки ошибки.',
            )
            debug = fields.String(
                required=False,
                allow_none=True,
                example=None,
                description='(необязательное поле) Подробная информация об ошибке, '
                            'случившейся в серверном приложении. Приходит на клиент '
                            'только в случае, если в серверном приложении включен DEBUG-режим.',
            )

        ExceptionSchema.__name__ = cls.__name__
        return ExceptionSchema()


__all__ = ['BaseAppException', 'ServerError']

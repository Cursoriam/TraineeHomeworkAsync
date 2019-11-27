from views import send_message
from views import speechrecognition


def setup_routes(app):
    """
    Устанавливает пути запросов
    :param app:
    """
    app.router.add_post('/api/pitter/v1/message', send_message)
    app.router.add_post('/voice', speechrecognition)
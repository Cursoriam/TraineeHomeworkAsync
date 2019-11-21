from views import send_message


def setup_routes(app):
    """
    Устанавливает пути запросов
    :param app:
    """
    app.router.add_post('/api/pitter/v1/message', send_message)

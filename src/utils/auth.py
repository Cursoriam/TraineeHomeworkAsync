from exceptions import AccessTokenInvalid


def access_token_required(func):
    """
    Проверка авторизации
    :param func:
    :return:
    """

    def wrapper(request):
        if not getattr(request, 'api_user', None):
            raise AccessTokenInvalid()
        return func(request)

    return wrapper

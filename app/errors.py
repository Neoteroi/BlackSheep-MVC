from blacksheep import Request, Response
from blacksheep.server.responses import text
from essentials.exceptions import (ObjectNotFound,
                                   NotImplementedException,
                                   UnauthorizedException,
                                   ForbiddenException,
                                   AcceptedException)
from blacksheep.server import Application


def configure_error_handlers(app: Application):

    # noinspection PyUnusedLocal
    async def not_found_handler(app, request: Request, exception: Exception) -> Response:
        return text(str(exception) or 'Not found', 404)

    # noinspection PyUnusedLocal
    async def not_implemented(*args) -> Response:
        return text('Not implemented', status=500)

    # noinspection PyUnusedLocal
    async def unauthorized(*args) -> Response:
        return text('Unauthorized', status=401)

    # noinspection PyUnusedLocal
    async def forbidden(*args) -> Response:
        return text('Forbidden', status=403)

    # noinspection PyUnusedLocal
    async def accepted(*args) -> Response:
        return text('Accepted', status=202)

    app.exceptions_handlers.update({
        ObjectNotFound: not_found_handler,
        NotImplementedException: not_implemented,
        UnauthorizedException: unauthorized,
        ForbiddenException: forbidden,
        AcceptedException: accepted
    })

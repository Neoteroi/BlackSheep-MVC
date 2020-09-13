from typing import Optional

from guardpost import Identity, User
from guardpost.asynchronous.authentication import AuthenticationHandler

from blacksheep import Request


class AppAuthenticationHandler(AuthenticationHandler):
    def __init__(self):
        ...

    async def authenticate(self, context: Request) -> Optional[Identity]:
        # TODO: implement desired logic;
        #       for example, a user context can be created using Request's cookies; or
        #       an Authorization header
        # Here, in this example, a user is hardcoded to provide an example.
        #
        # Request handlers are injected with this user, when a parameter is named
        # 'user' without type annotations,
        # or when type annotation is guardpost.User or guardpost.Identity

        user = User(
            {"id": "2c853c84-4abf-4cc1-901a-83a32431495b", "name": "John Doe"}, "DEMO"
        )

        # NB: do not change the name `identity` property.
        # It is called `identity` because it can be either a human or a service
        context.identity = user
        return user


def configure_authentication(app):
    app.use_authentication().add(AppAuthenticationHandler())

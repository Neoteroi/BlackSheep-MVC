"""
This module contains classes to configure initialization and disposing of services.
For example, a connection pool to a PostgreSQL database can be initialized at
application startup, and disposed when the application is stopped.

This class is common between, and abstracted from, front-end logic and data access
logic. See how it is used in app.program.py
app.on_start += context.initialize
"""


class AsyncEventHandler:
    def __init__(self, context):
        self.__handlers = []
        self.context = context

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def __len__(self):
        return len(self.__handlers)

    def append(self, handler):
        self.__handlers.append(handler)

    async def __call__(self, *args, **kwargs):
        return await self.fire()

    async def fire(self):
        for handler in self.__handlers:
            await handler()


class ServicesRegistrationContext:
    def __init__(self):
        self.initialize = AsyncEventHandler(self)
        self.dispose = AsyncEventHandler(self)

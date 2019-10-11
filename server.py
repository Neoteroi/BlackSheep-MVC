"""This module is where the application is configured.

To run with uvicorn cli, with hot reload:
    $ uvicorn server:app --port 44777 --reload --log-level info
"""
try:
    import uvloop
except ModuleNotFoundError:
    print('[*] Running without `uvloop`')
    uvloop = ...

import asyncio
from app.program import configure_application
from app.services import configure_services
from app.configuration import load_configuration

if uvloop is not ...:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = configure_application(*configure_services(load_configuration()))


if __name__ == '__main__':
    import main

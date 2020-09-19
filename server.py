"""This module is where the application is configured.

To run with uvicorn cli, with hot reload:
    $ uvicorn server:app --reload --log-level info
"""
try:
    import uvloop
except ModuleNotFoundError:
    print("[*] Running without `uvloop`")
    uvloop = ...
from app.program import configure_application
from app.services import configure_services
from app.configuration import load_configuration

if uvloop is not ...:
    uvloop.install()

app = configure_application(*configure_services(load_configuration()))

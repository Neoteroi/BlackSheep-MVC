"""This module is where the application is configured.

To run with uvicorn cli, with hot reload:
    $ uvicorn server:app --reload --log-level info
"""
import uvicorn

try:
    import uvloop
except ModuleNotFoundError:
    print("[*] Running without `uvloop`")
    uvloop = ...
from app.configuration import load_configuration
from app.program import configure_application
from app.services import configure_services

if uvloop is not ...:
    uvloop.install()

app = configure_application(*configure_services(load_configuration()))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")

"""
Use this script to debug the application with IDEs.
"""
import uvicorn
from server import app


# Nota bene: to debug an application that configures an event loop before calling uvicorn.run,
# replace the following line with a code that avoids overriding the event loop.
# This is necessary for example, when data access layer and business logic
# are configured before starting the application.
# See https://github.com/encode/uvicorn/pull/446#issuecomment-540484961
uvicorn.run(app, host='127.0.0.1', port=44777, log_level='info')


# For example, import subclass Config to a class whose setup_event_loop does nothing.
# The code in the following Gist works at the time of this writing (10/10/2019).
# https://gist.github.com/RobertoPrevato/e504dce6e12361b108a858ccc02172ea

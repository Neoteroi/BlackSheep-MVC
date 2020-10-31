"""
This module contains OpenAPI Documentation definition for the API.

It exposes a docs object that can be used to decorate request handlers with additional
information, used to generate OpenAPI documentation.
"""
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

docs = OpenAPIHandler(info=Info(title="Cats API", version="0.0.1"))

# include only endpoints whose path starts with "/api/"
docs.include = lambda path, _: path.startswith("/api/")

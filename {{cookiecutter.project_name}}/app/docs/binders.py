"""
This module configures OpenAPI Documentation for custom binders.
"""
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Parameter, ParameterLocation, Schema, ValueFormat, ValueType

from app.binders import PageOptionsBinder


def set_binders_docs(docs: OpenAPIHandler):
    """
    This function configures OpenAPI Documentation for custom application binders.
    """
    docs.set_binder_docs(
        PageOptionsBinder,
        [
            Parameter(
                "page",
                ParameterLocation.QUERY,
                description="Page number.",
                schema=Schema(minimum=0, format=ValueFormat.INT64, default=1),
            ),
            Parameter(
                "limit",
                ParameterLocation.QUERY,
                description="Number of results per page.",
                schema=Schema(
                    minimum=0, maximum=1000, format=ValueFormat.INT32, default=100
                ),
            ),
            Parameter(
                "continuation_id",
                ParameterLocation.QUERY,
                description=(
                    "Optional, ID of the last item that was retrieved. "
                    "If provided, enables faster pagination."
                ),
                schema=Schema(format=ValueFormat.INT64, default=None),
            ),
            Parameter(
                "order",
                ParameterLocation.QUERY,
                description=("Optional sort order (asc / desc) - default asc."),
                schema=Schema(ValueType.STRING, default=None),
            ),
        ],
    )

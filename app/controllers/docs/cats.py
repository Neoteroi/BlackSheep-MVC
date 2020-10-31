from domain.cats import CatType, CreateCatInput, Foo, HttpError, CreateCatOutput
from uuid import uuid4
from blacksheep.server.openapi.common import (
    ContentDoc,
    EndpointDocs,
    HeaderInfo,
    RequestBodyInfo,
    ResponseExample,
    ResponseInfo,
)


create_cat_docs = EndpointDocs(
    request_body=RequestBodyInfo(
        description="Example description etc. etc.",
        examples={
            "fat_cat": CreateCatInput(
                name="Fatty", active=False, type=CatType.EUROPEAN, foo=Foo.FOO
            ),
            "thin_cat": CreateCatInput(
                name="Thinny", active=False, type=CatType.PERSIAN, foo=Foo.UFO
            ),
        },
    ),
    responses={
        201: ResponseInfo(
            "The cat has been created",
            headers={"Location": HeaderInfo(str, "URL to the new created object")},
            content=[
                ContentDoc(
                    CreateCatOutput,
                    examples=[
                        ResponseExample(
                            CreateCatOutput(uuid4()),
                            description="Something something",
                        ),
                        CreateCatOutput(uuid4()),
                        CreateCatOutput(uuid4()),
                    ],
                ),
            ],
        ),
        400: ResponseInfo(
            "Bad request",
            content=[
                ContentDoc(
                    HttpError,
                    examples=[
                        HttpError(
                            404,
                            "Bad request because something something",
                            "DUPLICATE_CAT",
                        )
                    ],
                )
            ],
        ),
    },
)

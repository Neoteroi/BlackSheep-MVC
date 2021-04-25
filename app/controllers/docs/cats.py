from datetime import datetime
from domain.cats import (
    Cat,
    CatType,
    CatsList,
    CreateCatInput,
    Foo,
    HttpError,
    CreateCatOutput,
)
from uuid import UUID, uuid4
from blacksheep.server.openapi.common import (
    ContentInfo,
    EndpointDocs,
    HeaderInfo,
    RequestBodyInfo,
    ResponseExample,
    ResponseInfo,
)


get_cat_docs = EndpointDocs(
    summary="Gets a cat by id",
    description="""A sample API that uses a petstore as an
          example to demonstrate features in the OpenAPI 3 specification""",
    responses={
        200: ResponseInfo(
            "A cat",
            content=[
                ContentInfo(
                    Cat,
                    examples=[
                        ResponseExample(
                            Cat(
                                id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
                                name="Foo",
                                active=True,
                                type=CatType.EUROPEAN,
                                creation_time=datetime.now(),
                            )
                        )
                    ],
                )
            ],
        ),
        404: "Cat not found",
    },
)


get_cats_docs = EndpointDocs(
    summary="Gets a page of cats",
    description="""Returns a paginated list of cats, including the total count of items
    that respect the given filters.
    """,
    responses={
        200: ResponseInfo(
            "A paginated set of cats",
            content=[
                ContentInfo(
                    CatsList,
                    examples=[
                        CatsList(
                            [
                                Cat(
                                    id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
                                    name="Foo",
                                    active=True,
                                    type=CatType.EUROPEAN,
                                    creation_time=datetime.now(),
                                ),
                                Cat(
                                    id=UUID("f212cabf-987c-48e6-8cad-71d1c041209a"),
                                    name="Frufru",
                                    active=True,
                                    type=CatType.PERSIAN,
                                    creation_time=datetime.now(),
                                ),
                            ],
                            101,
                        )
                    ],
                )
            ],
        ),
    },
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
                ContentInfo(
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
                ContentInfo(
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

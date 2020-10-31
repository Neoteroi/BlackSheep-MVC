from datetime import datetime
from uuid import UUID
from blacksheep.server.openapi.common import ContentDoc, ResponseExample, ResponseInfo
from app.controllers.docs.cats import create_cat_docs
from domain.cats import (
    Cat,
    CatType,
    CreateCatInput,
    Foo,
    SomethingElse,
    UpdateCatInput,
)
from typing import List, Sequence

from app.docs import docs
from blacksheep import Response
from blacksheep.server.bindings import FromHeader, FromJson, FromQuery
from blacksheep.server.controllers import ApiController, delete, get, patch, post


# In this case, the entity name is obtained from the class name: "cats"
# To specify a @classmethod called "class_name" and returning a string, like in the
# Foo example below.
class Cats(ApiController):
    @get()
    def get_cats(
        self,
        page: FromQuery[int] = FromQuery(1),
        page_size: FromQuery[int] = FromQuery(30),
        search: FromQuery[str] = FromQuery(""),
    ) -> Response:
        """
        Returns a list of paginated cats.
        """

    @docs.ignore()
    def secret_api(self):
        ...

    @docs.deprecated()
    def deprecated_api(self):
        """
        This endpoint is deprecated.
        """

    @docs(
        summary="Gets a cat by id",
        description="""A sample API that uses a petstore as an
          example to demonstrate features in the OpenAPI 3 specification""",
        responses={
            200: ResponseInfo(
                "A cat",
                content=[
                    ContentDoc(
                        Cat,
                        examples=[
                            ResponseExample(
                                Cat(
                                    id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
                                    name="Foo",
                                    active=True,
                                    type=CatType.EUROPEAN,
                                    foo=Foo.FOO,
                                    creation_time=datetime.now(),
                                    friends=[
                                        Cat(
                                            id=UUID(
                                                "34b2b4c2-c78f-41aa-a08e-a672f4cbbcb4"
                                            ),
                                            name="Rufus",
                                            active=True,
                                            type=CatType.PERSIAN,
                                            foo=Foo.UFO,
                                            creation_time=datetime.now(),
                                            friends=[],
                                        )
                                    ],
                                )
                            )
                        ],
                    )
                ],
            ),
            404: "Cat not found",
        },
    )
    @get(":cat_id")
    def get_cat(self, cat_id: str) -> Response:
        """
        Gets a cat by id.
        """

    @docs.ignore()
    @post("/invite/cat")
    def invite_cat(self, example: FromHeader[List[str]]) -> Response:
        return self.text("Hi!")

    @post("/example")
    def example_post(self, foo: FromJson[List[UUID]]) -> Response:
        return self.text("Hi!")

    @docs(summary="Updates a Cat")
    @patch(":cat_id")
    def update_cat(self, cat_id: str, input: UpdateCatInput) -> Response:
        """
        Updates a cat with given id.
        """

    @post()
    @docs(create_cat_docs)
    def create_cat(self, input: FromJson[CreateCatInput]) -> Response:
        """
        Creates a new cat.
        """

    @post("/bulk/upload")
    def bulk_create_cat(self, input: FromJson[Sequence[CreateCatInput]]) -> Response:
        """
        Creates many cats.
        """

    @docs(
        responses={
            204: "Cat deleted successfully",
        },
    )
    @delete(":cat_id")
    def delete_cat(self, cat_id: str) -> Response:
        """
        Deletes a cat by id.

        Lorem ipsum dolor sit amet.
        """

    @post("magic")
    def magic_cat(self, cat: SomethingElse) -> Response:
        """
        Creates a magic cat
        """


class FooExample(ApiController):
    @classmethod
    def class_name(cls) -> str:
        return "foo"

    @docs.ignore()
    @get(":foo_id")
    def get_foo(self, foo_id: str) -> Response:
        """
        Handles GET /api/foo/:id
        """

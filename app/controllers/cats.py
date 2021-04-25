from uuid import UUID
from app.controllers.docs.cats import create_cat_docs, get_cat_docs, get_cats_docs
from domain.cats import (
    Cat,
    CatsList,
    CreateCatInput,
    UpdateCatInput,
)

from app.docs import docs
from blacksheep import Response
from blacksheep.server.bindings import FromJson, FromQuery
from blacksheep.server.controllers import ApiController, delete, get, patch, post


# In this case, the entity name is obtained from the class name: "cats"
# To specify a @classmethod called "class_name" and returning a string, like in the
# Foo example below.
class Cats(ApiController):
    @docs(get_cats_docs)
    @get()
    def get_cats(
        self,
        page: FromQuery[int] = FromQuery(1),
        page_size: FromQuery[int] = FromQuery(30),
        search: FromQuery[str] = FromQuery(""),
    ) -> CatsList:
        """
        Returns a list of paginated cats.
        """

    @docs(get_cat_docs)
    @get("{cat_id}")
    def get_cat(self, cat_id: UUID) -> Cat:
        """
        Gets a cat by id.
        """

    @docs(summary="Updates a Cat")
    @patch("{cat_id}")
    def update_cat(self, cat_id: str, input: UpdateCatInput) -> Cat:
        """
        Updates a cat with given id.
        """

    @post()
    @docs(create_cat_docs)
    def create_cat(self, input: FromJson[CreateCatInput]) -> Cat:
        """
        Creates a new cat.
        """

    @docs(
        responses={
            204: "Cat deleted successfully",
        },
    )
    @delete("{cat_id}")
    def delete_cat(self, cat_id: str) -> Response:
        """
        Deletes a cat by id.

        Lorem ipsum dolor sit amet.
        """


class FooExample(ApiController):
    @classmethod
    def class_name(cls) -> str:
        return "foo"

    @docs.ignore()
    @get("{foo_id}")
    def get_foo(self, foo_id: str) -> Response:
        """
        Handles GET /api/foo/:id
        """

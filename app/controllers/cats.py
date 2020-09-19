from blacksheep import Response
from blacksheep.server.controllers import ApiController, delete, get, patch, post


# In this case, the entity name is obtained from the class name: "cats"
# To specify a @classmethod called "class_name" and returning a string, like in the
# Foo example below.
class Cats(ApiController):
    @get(":cat_id")
    def get_cat(self, cat_id: str) -> Response:
        """
        Handles GET /api/cats/:id
        """

    @patch(":cat_id")
    def update_cat(self, cat_id: str) -> Response:
        """
        Handles PATCH /api/cats/:id
        """

    @post()
    def create_cat(self) -> Response:
        """
        Handles POST /api/cats
        """

    @delete(":cat_id")
    def delete_cat(self, cat_id: str) -> Response:
        """
        Handles DELETE /api/cats/:id
        """


class FooExample(ApiController):
    @classmethod
    def class_name(cls) -> str:
        return "foo"

    @get(":cat_id")
    def get_cat(self, cat_id: str) -> Response:
        """
        Handles GET /api/foo/:id
        """

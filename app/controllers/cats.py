from blacksheep import Response
from blacksheep.server.bindings import FromQuery
from blacksheep.server.controllers import ApiController, delete, get, patch, post
from app.docs import docs


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
    @get(":cat_id")
    def get_cat(self, cat_id: str) -> Response:
        """
        <docs format="yaml">
        summary: Lorem ipsum dolor sit amet.
        description: A sample API that uses a petstore as an example to demonstrate
            features in the swagger-2.0 specification
        responses:
            '200':
                description: pet response
                schema:
                    type: array
                    items:
                        $ref: '#/definitions/Pet'
        </docs>
        <summary>
            Gets a cat by id.
        </summary>
        <description>
            Something something.
        </description>
        <tags>
            ONE, TWO
        </tags>
        <examples>
            application/json:
                - id: 9e311914-6010-4257-8b4e-71be418e2d8f
                  cultureCode: en-us
                - id: b1934c47-a46a-4cf4-b0c7-74ae4e686864
                  cultureCode: en-gb
                - id: f87852db-b12c-4bc0-8c26-a946620aebba
                  cultureCode: it
                - id: 06e08c64-f525-484e-900d-3f3addae6b51
                  cultureCode: ja
                - id: 56d94aac-52cb-4c31-9807-dc45007646d8
                  brandId: eab80225-f5b0-4735-ae2a-1761af4b4054
                  cultureCode: en-us
        </examples>
        <responses>
            200: OK
            404: Cat not found
        </responses>
        """

    @patch(":cat_id")
    def update_cat(self, cat_id: str) -> Response:
        """
        Updates a cat with given id.
        """

    @post()
    def create_cat(self) -> Response:
        """
        Creates a new cat.
        """

    @delete(":cat_id")
    def delete_cat(self, cat_id: str) -> Response:
        """
        Deletes a cat by id.
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

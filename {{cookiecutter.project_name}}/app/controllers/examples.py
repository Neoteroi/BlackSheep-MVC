"""
Example API implemented using a controller.
"""
from typing import List, Optional

from blacksheep.server.controllers import Controller, get, post


class ExamplesController(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return "/api/examples"

    @classmethod
    def class_name(cls) -> str:
        return "Examples"

    @get()
    async def get_examples(self) -> List[str]:
        """
        Gets a list of examples.
        """
        return list(f"example {i}" for i in range(3))

    @post()
    async def add_example(self, example: str):
        """
        Adds an example.
        """

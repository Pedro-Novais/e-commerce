from flask import Request

from ._I18n import I18n

from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    OperationError,
    ParameterNotSend
)

class CreateCategory:
    def __init__(self, shop_name: str, request: Request):
        self.shop = shop_name
        request = request.get_json()

        self.name = request.get("name", None)
        if not self.name:
            raise ParameterNotSend()
        
        self.description = request.get("description")

    def action(self):
        category_repo = CategoryRepository()

        new_category = category_repo.create_category(
            shop=self.shop,
            name=self.name,
            description=self.description
        )

        if not new_category:
            raise OperationError(I18n.ERROR_CREATE_CATEGORY)
        
        return I18n.SUCCESS_CREATE_CATEGORY
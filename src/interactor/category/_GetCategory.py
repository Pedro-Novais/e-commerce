from flask import Request

from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    OperationError,
    ParameterNotSend
)

class GetCategory:
    def __init__(self, shop_name: str, request: Request):
        self.shop = shop_name
        request = request.get_json()

        self.name = request.get("name", None)
        
        self.description = request.get("description", None)

    def action(self):

        if not self.name or not self.description:
            raise OperationError("Nenhuma modificação foi realizada!")
        
        category_repo = CategoryRepository()

        new_category = category_repo.create_category(
            shop=self.shop,
            name=self.name,
            description=self.description
        )

        if not new_category:
            raise OperationError("Erro ao criar nova categoria!")
        
        return "Categoria criada com sucesso"
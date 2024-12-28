from flask import Request

from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    OperationError,
    NotFoundError
)

class UpdateCategory:
    def __init__(self, category_id: int, shop_name: str, request: Request):
        self.shop = shop_name
        self.category = category_id
        request = request.get_json()

        self.name = request.get("name", None)
        
        self.description = request.get("description", None)

    def action(self):
        
        category_repo = CategoryRepository()

        category_update = category_repo.update_category(
            category_id=self.category,
            shop=self.shop,
            name=self.name,
            description=self.description
        )

        if not category_update:
            raise OperationError("Erro ao atualizar categoria!")
        
        if category_update == "AnyData":
            raise NotFoundError("Categoria não foi enconmtrada para atualização!")
        
        return "Categoria atualizada com sucesso"
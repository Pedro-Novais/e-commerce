from flask import Request

from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    OperationError,
    NotFoundError
)

class DeleteCategory:
    def __init__(self, category_id: int, shop_name: str):
        self.shop = shop_name
        self.category = category_id

    def action(self):
        
        category_repo = CategoryRepository()

        delete_category = category_repo.delete(id=self.category, shop=self.shop)

        if not delete_category:
            raise OperationError("Erro ao deletar categoria!")
        
        if delete_category == "AnyData":
            raise NotFoundError("Categoria não foi encontrada!")
        
        return "Categoria deletada com sucesso"
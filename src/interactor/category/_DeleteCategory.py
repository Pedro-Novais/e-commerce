from utils._I18nShared import I18nShared
from ._I18n import I18n

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
            raise OperationError(I18n.ERROR_DELETE_CATEGORY)
        
        if delete_category == I18nShared.ANY_DATA:
            raise NotFoundError(I18n.NOT_FOUND_CATEGORY)
        
        return I18n.SUCCESS_DELETE_CATEGORY
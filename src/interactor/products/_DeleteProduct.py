from utils._I18nShared import I18nShared
from ._I18n import I18n

from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import (
    ParameterNotSend,
    OperationError
)

class DeleteProduct:
    def __init__(self, product_id: int, shop_name: str):
        self.shop = shop_name
        self.product_id = product_id

        if not self.product_id:
            raise ParameterNotSend()
        
    def action(self):
        product_repo = ProductRepository()

        delete_product = product_repo.delete(id=self.product_id, shop=self. shop)

        if not delete_product:
            raise OperationError(I18n.ERROR_DELETE_PRODUCT)
        
        if delete_product == I18nShared.ANY_DATA:
            raise OperationError(I18n.NOT_FOUND_PRODUCT)

        return I18n.SUCCESS_DELETE_PRODUCT
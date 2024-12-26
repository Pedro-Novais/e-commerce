from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError
    )

class GetOneProduct:
    def __init__(self, productId: int, shop_name: str):
        self.shop = shop_name
        self.productId = productId

        if not self.productId:
            raise NotFoundError("Parametros obrigatórios não foram enviados!")

    def action(self):
        product_repo = ProductRepository()

        product = product_repo.get_by_id(id=self.productId, shop=self.shop)

        if not product:
            raise NotFoundError("Nenhum produto foi encontrado!")
        
        data = {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "is_digital": product.is_digital,
            "custom_properties": product.custom_properties,
            "images": product.images,
        }

        return data
from ._I18n import I18n

from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import NotFoundError

class GetOneProduct:
    def __init__(self, productId: int, shop_name: str):
        self.shop = shop_name
        self.productId = productId

        if not self.productId:
            raise NotFoundError()

    def action(self):
        product_repo = ProductRepository()

        product = product_repo.get_one_product(id=self.productId, shop=self.shop)

        if not product:
            raise NotFoundError(I18n.NOT_FOUND_PRODUCT)
        
        data = {
            "name": product.name,
            "description": product.description,
            "is_digital": product.is_digital,
            "custom_properties": product.custom_properties,
            "variants": [
                {
                "price": variant.price,
                "color": variant.color,
                "size": variant.size,
                "images": variant.images
                }
                for variant in product.variants
            ]
        }

        return data
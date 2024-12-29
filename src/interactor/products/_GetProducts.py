from ._I18n import I18n

from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import NotFoundError

class GetProducts:
    def __init__(self, shop_name: str):
        self.shop = shop_name

    def action(self):
        product_repo = ProductRepository()

        products = product_repo.get_all_products(shop=self.shop)

        if not products:
            raise NotFoundError(I18n.NOT_FOUND_PRODUCT)

        data = [
            {   
                "name": product.name,
                "description": product.description,
                "is_digital": product.is_digital,
                "custom_properties": product.custom_properties,
                "category": product.category.name,
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
            for product in products
        ]
        return data
         
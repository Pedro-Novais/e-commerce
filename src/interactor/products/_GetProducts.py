from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import NotFoundError

class GetProducts:
    def __init__(self, shop_name: str):
        self.shop = shop_name

    def action(self):
        product_repo = ProductRepository()

        products = product_repo.get_all_products(shop=self.shop)

        if not products:
            raise NotFoundError("Produtos não foram encontrados!")

        data = [
            {   
                "name": products[0].name,
                "description": products[0].description,
                "is_digital": products[0].is_digital,
                "custom_properties": products[0].custom_properties,
                "category": products[0].category.name,
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
         
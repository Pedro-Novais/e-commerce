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
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "is_digital": product.is_digital,
            "custom_properties": product.custom_properties,
            "images": product.images,
            "category": product.category.name
            }
            for product in products
        ]

        return data
         
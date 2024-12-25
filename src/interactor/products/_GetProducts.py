from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import NotFoundError

class GetProducts:
    def __init__(self):
        pass

    def action(self):
        product_repo = ProductRepository()

        products = product_repo.get_all_products()

        if not products:
            raise NotFoundError("Produtos não foram encontrados!")
        
        data = [
            {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "category": product.category.name
            }
            for product in products
        ]

        return data
         
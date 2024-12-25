from repository._ProductRepository import ProductRepository
from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    ParameterNotSend,
    OperationError
)

from flask import Request

class CreateProduct:
    def __init__(self, request: Request):
        request = request.get_json()

        self.name = request.get("name")
        if not self.name:
            raise ParameterNotSend()
        
        self.description = request.get("description", None)

        self.price = request.get("price")
        if not self.price:
            raise ParameterNotSend()
        
        if not isinstance(self.price, float):
            raise FormatInvalidError()
        
        self.stock = request.get("stock_quantity", 0)

        self.is_digital = request.get("is_digital", False)

        self.custom_properties = request.get("custom_properties", [])

        self.images = request.get("images", [])

        self.category = request.get("category", None)

    def action(self):
        product_repo = ProductRepository()
        category_repo = CategoryRepository()

        category_valid = category_repo.get_by_id(id=self.category)

        if not category_valid:
            raise NotFoundError("Categoria utilizada no cadastro, não foi encontrada!")
        
        create_product = product_repo.create_product(
            name=self.name,
            description=self.description,
            price=self.price,
            category_id=self.category,
            stock_quantity=self.stock,
            is_digital=self.is_digital,
            custom_properties=self.custom_properties,
            images=self.images
        )

        if not create_product:
            raise OperationError("Erro ao criar novo produto!")
        
        return "Produto criado com sucesso!"
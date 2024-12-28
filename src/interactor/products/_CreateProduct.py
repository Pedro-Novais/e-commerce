from repository._ProductRepository import ProductRepository
from repository._ProductVariantsRepository import ProductVariantsRepository
from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    ParameterNotSend,
    OperationError
)

from flask import Request

class CreateProduct:
    def __init__(self, request: Request, shop_name: str):
        self.shop = shop_name
        request = request.get_json()

        self.name = request.get("name")
        if not self.name:
            raise ParameterNotSend()
        
        self.description = request.get("description", None)

        self.is_digital = request.get("is_digital", False) 

        self.custom_properties = request.get("custom_properties", [])

        self.category = request.get("category", None)

        self.variants = request.get("variants", None)
        if not self.variants:
            raise ParameterNotSend()
        
        for variant in self.variants:
            if not variant.get("price"):
                raise ParameterNotSend()
            if not isinstance(variant.get("price"), float):
                raise FormatInvalidError()

    def action(self):
        product_repo = ProductRepository()
        category_repo = CategoryRepository()

        category_valid = category_repo.get_by_id(id=self.category, shop=self.shop)

        if not category_valid:
            raise NotFoundError("Categoria utilizada no cadastro, não foi encontrada!")
        
        create_product = product_repo.create_product(
            name=self.name,
            description=self.description,
            category_id=self.category,
            is_digital=self.is_digital,
            custom_properties=self.custom_properties,
            shop=self.shop,
            product_variants=self.variants
        )

        if not create_product:
            raise OperationError("Erro ao criar novo produto!")
        
        return "Produto criado com sucesso!"
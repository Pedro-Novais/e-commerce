from flask import Request

from repository._ProductRepository import ProductRepository
from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    ParameterNotSend,
    InfoAlreadyInUseError,
    OperationError
)

class UpdateProduct:
    def __init__(self, request: Request, productId: int, shop_name: str):
        self.shop = shop_name
        request = request.get_json()

        self.productId = productId

        if not self.productId:
            raise ParameterNotSend()

        self.name = request.get("name", None)
        
        self.description = request.get("description", None)

        self.price = request.get("price", None)
        if self.price:
            if not isinstance(self.price, float):
                raise FormatInvalidError()
        
        self.stock = request.get("stock_quantity", None)
        if self.stock:
            if not isinstance(self.stock, int):
                raise FormatInvalidError() 

        self.is_digital = request.get("is_digital", None)
        if self.is_digital:
            if not isinstance(self.is_digital, bool):
                raise FormatInvalidError()

        self.custom_properties = request.get("custom_properties", None)
        if self.custom_properties:
            if not isinstance(self.custom_properties, list):
                raise FormatInvalidError()
            
        self.images = request.get("images", None)
        if self.images:
            if not isinstance(self.images, list):
                raise FormatInvalidError()

        self.category = request.get("category", None)

    def action(self):
        product_repo = ProductRepository()
        category_repo = CategoryRepository()

        if self.category:
            category_valid = category_repo.get_by_id(id=self.category, shop=self.shop)

            if not category_valid:
                raise NotFoundError("Categoria utilizada na atualização do item, não foi encontrada!")
        
        update_product = product_repo.update_product(
            shop=self.shop,
            product_id=self.productId,
            name=self.name,
            description=self.description,
            price=self.price,
            category_id=self.category,
            stock_quantity=self.stock,
            is_digital=self.is_digital,
            custom_properties=self.custom_properties,
            images=self.images
        )

        if not update_product:
            raise OperationError("Erro ao atualizar produto!")
        
        if update_product == "AnyData":
             raise OperationError("Produto não foi encontrado para efetuar as alterações!")
        
        return "Produto atualizado com sucesso!"
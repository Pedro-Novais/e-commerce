from flask import Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    GetOneProduct,
    GetProducts,
    CreateProduct,
    DeleteProduct,
    UpdateProduct
)

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    ParameterNotSend,
    InfoAlreadyInUseError,
    OperationError,
    CredentialIncorrectError,
    AdminCanotBeDeletedError,
    )

class ProductController:
    def __init__(self, request: Request, shop_name: str):
        self.shop_name = shop_name
        self.request = request

    def get_one_product(self, product_id: int):
        try:
            action = GetOneProduct(productId=product_id, shop_name=self.shop_name).action()
            return jsonify(action), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def get_products(self):
        try:
            action = GetProducts(shop_name=self.shop_name).action()
            return jsonify(action), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def add_product(self):
        try:
            action = CreateProduct(request=self.request, shop_name=self.shop_name).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            ParameterNotSend,
            NotFoundError,
            FormatInvalidError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def delete_product(self, productId: int):
        try:
            action = DeleteProduct(product_id=productId, shop_name=self.shop_name).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            ParameterNotSend,
            OperationError
            ) as e:
            return error_handler(error=e)

    def edit_product(self, productId: int):
        try:
            action = UpdateProduct(request=self.request, productId=productId).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            ParameterNotSend,
            OperationError,
            FormatInvalidError
            ) as e:
            return error_handler(error=e)
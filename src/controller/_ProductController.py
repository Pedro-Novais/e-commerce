from flask import Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    GetProduct,
    GetProducts,
    CreateProduct,
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
    def __init__(self, request: Request):
        self.request = request

    def get_products(self):
        pass

    def get_product(self, product_id):
        pass

    def add_product(self):
        try:
            action = CreateProduct(request=self.request).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            ParameterNotSend,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def delete_product(self):
        pass

    def edit_product(self):
        pass
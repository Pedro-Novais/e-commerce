from flask import Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    GetOneProduct,
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

    def get_one_products(self):
        pass

    def get_products(self):
        try:
            action = GetProducts().action()
            return jsonify(action), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def add_product(self):
        try:
            action = CreateProduct(request=self.request).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            ParameterNotSend,
            NotFoundError,
            FormatInvalidError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def delete_product(self):
        pass

    def edit_product(self):
        pass
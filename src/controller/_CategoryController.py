from flask import Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    CreateCategory,
    UpdateCategory,
    DeleteCategory,
    GetCategory
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

class CategoryController:
    def __init__(self, request: Request, shop_name: str):
        self.shop_name = shop_name
        self.request = request

    # def get_category(self, user_id: int):
    #     try:
    #         action = CreateCategory(user_id=user_id, shop_name=self.shop_name, request=self.request).action()
    #         return jsonify(action), 201
        
    #     except (
    #         Exception,
    #         NotFoundError,
    #         OperationError
    #         ) as e:
    #         return error_handler(error=e)
        
    def create_category(self):
        try:
            action = CreateCategory(shop_name=self.shop_name, request=self.request).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
        
    def update_category(self, category_id: int):
        try:
            action = UpdateCategory(category_id=category_id, shop_name=self.shop_name, request=self.request).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
        
    def delete_category(self, category_id: int):
        try:
            action = DeleteCategory(shop_name=self.shop_name, category_id=category_id).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
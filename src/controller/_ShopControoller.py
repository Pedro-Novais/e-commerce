from flask import Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    GetShop,
    CreateShop,
    UpdateShop,
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

class ShopController:
    def __init__(self, request: Request, shop_name: str):
        self.shop_name = shop_name
        self.request = request

    def get_shop(self):
        try:
            action = GetShop(shop_name=self.shop_name).action()
            return jsonify(action), 201
        
        except Exception as e:
            return error_handler(error=e)

    def post_shop(self):
        try:
            action = CreateShop(shop_name=self.shop_name, request=self.request).action()
            return jsonify(action), 201
        
        except Exception as e:
            return error_handler(error=e)
    
    def update_shop(self):
        try:
            action = UpdateShop(shop_name=self.shop_name, request=self.request).action()
            return jsonify({"msg":action}), 201
        
        except Exception as e:
            return error_handler(error=e)
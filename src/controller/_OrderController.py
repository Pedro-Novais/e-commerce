from flask import Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    CreateOrder,
    WebHookOrder
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

class OrderController:
    def __init__(self, request: Request, shop_name: str):
        self.shop_name = shop_name
        self.request = request

    def create_order(self, user_id: int):
        try:
            action = CreateOrder(user_id=user_id, shop_name=self.shop_name, request=self.request).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
        
    def webhook_order(self):
        try:
            action = WebHookOrder(request=self.request).action()
            return jsonify({"msg": action}), 201
        
        except Exception as e:
            return error_handler(error=e)

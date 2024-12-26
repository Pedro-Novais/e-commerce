from flask import Response, Request, jsonify
from middleware.error_handler import error_handler

from interactor import (
    CreateUser,
    LoginUser,
    UpdateUser,
    DeleteUser,
    GetUser,
    CreateAddress,
    UpdateAddress,
    DeleteAddress
)

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    InfoAlreadyInUseError,
    OperationError,
    CredentialIncorrectError,
    AdminCanotBeDeletedError
    )

class UserController:
    def __init__(self, request, shop_name):
        self.request = request
        self.shop_name = shop_name
    
    def get_user(self, userId: int) -> Response:
        try:
            action = GetUser(userId=userId, shop_name=self.shop_name).action()
            return jsonify(action), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def create_user(self) -> Response:
        try:
            action = CreateUser(request=self.request, shop_name=self.shop_name).action()
            return jsonify({"msg": action}), 200
        
        except (
            Exception,
            NotFoundError,
            FormatInvalidError,
            InfoAlreadyInUseError,
            OperationError
            ) as e:
            return error_handler(error=e)
    
    def login_user(self) -> Response:
        try:
            action = LoginUser(request=self.request, shop_name=self.shop_name).action()
            return jsonify({"msg": action}), 200
        
        except (
            Exception,
            NotFoundError,
            CredentialIncorrectError,
            OperationError
            ) as e:
            return error_handler(error=e)
        
    def update_user(self, request: Request, userId: int) -> Response:
        try:
            action = UpdateUser(request=request, userId=userId).action()
            return jsonify(action), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
    
    def delete_user(self, userId: int) -> Response:
        try:
            action = DeleteUser(userId=userId, shop_name=self.shop_name).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            AdminCanotBeDeletedError,
            OperationError
            ) as e:
            return error_handler(error=e)
        
    def add_address_from_user(self, userId: int):
        try:
            action = CreateAddress(request=self.request).action(userId=userId)
            return jsonify(action), 201
        
        except (
            Exception,
            NotFoundError,
            AdminCanotBeDeletedError,
            OperationError
            ) as e:
            return error_handler(error=e)

    def update_address_from_user(self, userId: int, address_id: int) -> Response:
        try:
            action = UpdateAddress(request=self.request).action(userId=userId, addressId=address_id)
            return jsonify(action), 201
        
        except (
            Exception,
            OperationError
            ) as e:
            return error_handler(error=e)

    def delete_address_from_user(self, user_id: int, address_id: int) -> Response:
        try:
            action = DeleteAddress(user_id=user_id, address_id=address_id).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
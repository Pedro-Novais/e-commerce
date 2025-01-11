from flask import Response, Request, jsonify, make_response
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
    
    def user_logged(self, userId: int) -> Response:
        try:
            response = {
                    "msg": "Usuário possui sessão"
                }
            
            if not userId:
                response = {
                    "msg": "Usuário não possui sessão"
                }
                return jsonify(response), 404
            
            return jsonify(response), 201
        
        except Exception as e:
            return error_handler(error=e)

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
            token = LoginUser(request=self.request, shop_name=self.shop_name).action()
            response = make_response(jsonify({"msg": "Usuário autenticado com sucesso", "token": token}), 201)
            response.set_cookie(
                'authToken',
                token,
                httponly=True,  
                secure=False,    
                samesite='Strict',  
                max_age=60 * 60 
            )
            return response
        
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
            action = CreateAddress(request=self.request, shop_name=self.shop_name).action(userId=userId)
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
            action = UpdateAddress(request=self.request, shop_name=self.shop_name).action(userId=userId, addressId=address_id)
            return jsonify(action), 201
        
        except (
            Exception,
            OperationError
            ) as e:
            return error_handler(error=e)

    def delete_address_from_user(self, user_id: int, address_id: int) -> Response:
        try:
            action = DeleteAddress(user_id=user_id, address_id=address_id, shop_name=self.shop_name).action()
            return jsonify({"msg": action}), 201
        
        except (
            Exception,
            NotFoundError,
            OperationError
            ) as e:
            return error_handler(error=e)
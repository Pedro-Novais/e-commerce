from flask import Request

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    ParameterNotSend,
    InfoAlreadyInUseError,
    OperationError,
    CredentialIncorrectError,
    AdminCanotBeDeletedError,
    )

class CreateOrder:
    def __init__(self, user_id: int, shop_name: str, request: Request):
        self.user_id = user_id
        self.shop = shop_name
        
        request = request.get_json()
        
        self.validators()

    def action(self):
        print("teste de api")
        response = {
            "msg": "certo",
            "code": 200
        }
        return response
    
    def validators(self):
        pass

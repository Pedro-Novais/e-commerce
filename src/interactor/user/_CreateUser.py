from flask import Request, Response

from utils.validators import (
    valid_email, 
    valid_password
    )

from ._I18n import I18n

from middleware.criptografy import hash_password

from repository._UserRepository import UserRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    InfoAlreadyInUseError,
    OperationError
)

class CreateUser:
    def __init__(self, request: Request, shop_name: str):
        self.shop = shop_name
        self.request = request.get_json()

        self.name = self.request.get("name")
        if not self.name:
            raise NotFoundError()

        if not isinstance(self.name, str):
            raise FormatInvalidError("Nome inválido!")
        
        self.email = self.request.get("email")
        if not self.email:
            raise NotFoundError()
        
        if not valid_email(email=self.email):
            raise FormatInvalidError("Email inválido!")

        self.password = self.request.get("password")
        if not self.password:
            raise NotFoundError()
        
        if not valid_password(password=self.password):
            raise FormatInvalidError(I18n.ERROR_FORMAT_PASSWORD)
        
        self.is_admin = self.request.get("is_admin", False) in [True]
        
    def action(self):
        user_repo = UserRepository()

        new_email = user_repo.get_user_by_email(email=self.email, shop=self.shop)

        if new_email:
            raise InfoAlreadyInUseError(I18n.ERROR_EMAIL_ALREADY_REGISTERED.format(email=new_email))
        
        password_criptography = hash_password(password=self.password)

        new_user = user_repo.create_user(
            shop_name=self.shop,
            name=self.name,
            email=self.email,
            password=password_criptography,
            is_admin=self.is_admin
        )
        
        if not new_user:
            raise OperationError(I18n.ERROR_CREATE_USER)
        
        return I18n.SUCCESS_CREATE_USER
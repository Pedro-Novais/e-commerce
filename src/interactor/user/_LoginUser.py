from flask import Request

from utils.validators import valid_email

from ._I18n import I18n

from repository._UserRepository import UserRepository

from middleware.criptografy import (
    check_password,
    generate_token
)

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    CredentialIncorrectError
)

class LoginUser:
    def __init__(self, request: Request, shop_name: str) -> str:
        self.shop = shop_name
        self.request = request.get_json()
        
        self.email = self.request.get("email")
        if not self.email:
            raise NotFoundError()
        
        if not valid_email(email=self.email):
            raise FormatInvalidError("Email inválido!")
        
        self.password = self.request.get("password")
        if not self.password:
            raise NotFoundError()
        
    def action(self):
        user_repo = UserRepository()

        credential_save = user_repo.get_user_by_email(email=self.email, shop=self.shop)

        if not credential_save:
            raise NotFoundError(I18n.NOT_FOUND_EMAIL.format(email=self.email))
        
        if not check_password(password_save=credential_save.password, password_sended=self.password):
            raise CredentialIncorrectError(I18n.INVALID_CREDENTIALS)
        
        new_token = generate_token(user_id=credential_save.id)

        return new_token
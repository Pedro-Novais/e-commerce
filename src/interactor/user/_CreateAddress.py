from flask import Request

from ._I18n import I18n

from repository._AddressRepository import AddressRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    OperationError
)

class CreateAddress:
    def __init__(self, request: Request, shop_name: str):
        self.shop = shop_name
        self.request = request.get_json()

        self.street = self.request.get("street")
        if not self.street:
            raise NotFoundError()
        
        self.number = self.request.get("number")
        if not self.number:
            raise NotFoundError()

        self.city = self.request.get("city")
        if not self.city:
            raise NotFoundError()

        self.state = self.request.get("state")
        if not self.state:
            raise NotFoundError()

        self.zip_code = self.request.get("zip_code")
        if not self.zip_code:
            raise NotFoundError()

    def action(self, userId: int):
        address_repo = AddressRepository()

        new_address = address_repo.create_address(
            user_id=userId,
            shop_name=self.shop,
            street=self.street,
            number=self.number,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code
        )

        if not new_address:
            raise OperationError(I18n.ERROR_SAVE_ADDRESS)
        
        data = {
            "street": new_address.street,
            "number": self.number,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code
        }

        return data
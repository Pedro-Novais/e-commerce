from flask import Request

from repository._AddressRepository import AddressRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    OperationError
)


class CreateAddress:
    def __init__(self, request: Request):
        self.request = request.get_json()

        self.street = self.request.get("street")
        if not self.street:
            raise NotFoundError("Paramêtros não enviados ao servidor!")
        
        self.number = self.request.get("number")
        if not self.number:
            raise NotFoundError("Paramêtros não enviados ao servidor!")

        self.city = self.request.get("city")
        if not self.city:
            raise NotFoundError("Paramêtros não enviados ao servidor!")

        self.state = self.request.get("state")
        if not self.state:
            raise NotFoundError("Paramêtros não enviados ao servidor!")

        self.zip_code = self.request.get("zip_code")
        if not self.zip_code:
            raise NotFoundError("Paramêtros não enviados ao servidor!")

    def action(self, userId: int):
        address_repo = AddressRepository()

        new_address = address_repo.create_address(
            user_id=userId,
            street=self.street,
            number=self.number,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code
        )

        if not new_address:
            raise OperationError("Erro ao salvar novo endereço!")
        
        data = {
            "street": new_address.street,
            "number": self.number,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code
        }

        return data
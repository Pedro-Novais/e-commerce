from flask import Request

from repository._AddressRepository import AddressRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    OperationError
)

class UpdateAddress:
    def __init__(self, request: Request, shop_name: str):
        self.shop = shop_name
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

    def action(self, userId: int, addressId: int):
        address_repo = AddressRepository()

        update_address = address_repo.update_address(
            user_id=userId,
            shop_name=self.shop,
            address_id=addressId,
            street=self.street,
            number=self.number,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code
        )

        if not update_address:
            raise OperationError("Erro ao atualizar endereço!")
        
        if update_address == "AnyData":
            raise NotFoundError("Endereço não foi encontrado para realizar as alterações!")
        
        data = {
            "street": update_address.street,
            "number": self.number,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code
        }

        return data
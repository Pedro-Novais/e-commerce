from flask import Request

from repository._AddressRepository import AddressRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    OperationError
)

class DeleteAddress:
    def __init__(self, user_id: int, address_id: int, shop_name: str):
        self.user_id = user_id
        self.address_id = address_id
        self.shop = shop_name

    def action(self):
        address_repo = AddressRepository()

        delete_address = address_repo.delete_address(user_id=self.user_id, address_id=self.address_id, shop_name=self.shop)

        if not delete_address:
            raise OperationError("Erro ao excluir o endereço!")
        
        if delete_address == "AnyData":
            raise NotFoundError("Endereço não foi encontrado para ser excluído!")
        
        return "Endereço deletado com sucesso!"
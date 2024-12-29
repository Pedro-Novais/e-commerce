from utils._I18nShared import I18nShared
from ._I18n import I18n

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
            raise OperationError(I18n.ERROR_DELETE_ADDRESS)
        
        if delete_address == I18nShared.ANY_DATA:
            raise NotFoundError(I18n.NOT_FOUND_ADDRESS)
        
        return I18n.SUCCESS_DELETE_ADDRESS
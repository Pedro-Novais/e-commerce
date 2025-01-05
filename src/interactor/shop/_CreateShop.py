from flask import Request

from ._I18n import I18n
from repository._ShopRepository import ShopRepository

from custom_exceptions._CustomExceptions import (
    ParameterNotSend,
    OperationError
)

from ._ValidatorsShop import (
    validate_company_infos,
    validiate_address
)

class CreateShop:
    def __init__(self, shop_name: str, request: Request):
        self.shop = shop_name
        
        request = request.get_json()
        errors = []
        
        self.name = request.get("name", None)
        if self.name is None:
            raise ParameterNotSend(I18n.PARAMETER_NOT_SEND)

        self.subdomain = request.get("subdomain", None)
        if self.subdomain is None:
            raise ParameterNotSend(I18n.PARAMETER_NOT_SEND)
        
        self.company_infos = request.get("company_infos", {})
        validate_company_infos(self.company_infos, errors)

        self.address = request.get("address", {})
        validiate_address(self.address, errors)

        if len(errors) > 0:
            raise ParameterNotSend(I18n.PARAMETER_NOT_SEND)
        
    def action(self):
        shop_repo = ShopRepository()

        new_shop = shop_repo.create_shop(
            name= self.name,
            company_infos= self.company_infos,
            address= self.address,
            subdomain= self.subdomain
        )

        if not new_shop:
            raise OperationError(I18n.ERROR_CREATE_SHOP)
        
        return I18n.SUCCESS_CREATE_SHOP
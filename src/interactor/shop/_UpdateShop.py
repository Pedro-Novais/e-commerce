from flask import Request

from ._I18n import I18n
from utils._I18nShared import I18nShared
from repository._ShopRepository import ShopRepository

from ._ValidatorsShop import (
    validate_company_infos,
    validate_chat_infos,
    validiate_address,
    validate_images,
    validate_colors
)

from custom_exceptions._CustomExceptions import (
    OperationError,
    NotFoundError
)

class UpdateShop:
    def __init__(self, shop_name: str, request: Request):
        self.shop = shop_name
        
        request = request.get_json()
        errors = []

        self.company_infos = request.get("company_infos", None)
        if self.company_infos:
            validate_company_infos(company_infos=self.company_infos, validator=errors)

        self.address = request.get("address", None)
        if self.address:
            validiate_address(address=self.address, validator=errors)
        
        self.chat_infos = request.get("chat_infos", None)
        if self.chat_infos:
            validate_chat_infos(chat_infos=self.chat_infos, validator=errors)
        
        self.colors = request.get("colors", None)
        if self.colors:
            validate_colors(colors=self.colors, validator=errors)
        
        self.images = request.get("images", None)
        if self.images:
            validate_images(images=self.images, validator=errors)

    def action(self):
        shop_repo = ShopRepository()

        update_shop = shop_repo.update_shop(
            name_subdomain= self.shop,
            company_infos=self.company_infos,
            address=self.address,
            chat_infos=self.chat_infos,
            colors=self.colors,
            images=self.images
        )

        if not update_shop:
            raise OperationError(I18n.ERROR_UPDATE_SHOP)
        
        if update_shop == I18nShared.ANY_DATA:
            raise NotFoundError(I18n.NOT_FOUND_SHOP)
        
        return I18n.SUCCESS_UPDATE_SHOP
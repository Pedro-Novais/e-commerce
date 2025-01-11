from ._I18n import I18n

from repository._ShopRepository import ShopRepository

from custom_exceptions._CustomExceptions import NotFoundError

class GetShop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
    
    def action(self):
        shop_repo = ShopRepository()

        shop = shop_repo.get_by_name(name=self.shop_name)

        if not shop:
            raise NotFoundError(I18n.NOT_FOUND_SHOP)

        company_infos = shop.company_infos

        address = shop.address

        images = shop.images

        colors = shop.colors

        chat_infos = shop.chat_infos

        data = {
            "name": shop.name,
            "company_infos": company_infos,
            "address": address,
            "subdomain": shop.subdomain or None,
            "images": images,
            "colors": colors,
            "chat_infos": chat_infos,
            "is_active": shop.is_active or None
        }

        return data
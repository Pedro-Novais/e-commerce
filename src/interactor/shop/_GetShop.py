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
        
        validator = []

        company_infos = shop.company_infos
        self.validate_company_infos(company_infos, validator)

        address = shop.address
        self.valdiate_address(address, validator)

        images = shop.images
        self.validate_images(images, validator)

        colors = shop.colors
        self.validate_color(colors, validator)

        chat_infos = shop.chat_infos
        self.validate_chat_infos(chat_infos, validator)

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
    
    def validate_company_infos(self, company_infos: dict, validator: list):
        """
            "name": company_infos.name or None,
            "cnpj": shop.company_infos.cnpj or None,
            "ie": shop.company_infos.ie or None,
            "im": shop.company_infos.im or None,
            "phone": shop.company_infos.phone or None,
        """
        pass

    def valdiate_address(self, address: dict, validator: list):
        """
            "phone": shop.company_infos.phone or None,
            "street": shop.address.street or None,
            "number": shop.address.number or None,
            "complement": shop.address.complement or None,
            "neighborhood": shop.address.neighborhood or None,
            "city": shop.address.city or None,
            "state": shop.address.state or None,
            "country": shop.address.country or None,
            "zipcode": shop.address.zipcode or None,
        """
        pass

    def validate_images(self, images: dict, validator: list):
        """
            "logo": shop.logo or None,
            "favicon": shop.favicon or None,
            "banners": [
                {
                    "url": banner.url or None,
                    "position": banner.position or None,
                    "product_link": banner.product_link or None
                }
                for banner in shop.images
            ]
        """
        pass
    
    def validate_color(self, color: dict, valdiate: list):
        """
            "backgroundPrimary": shop.colors.backgroundPrimary or None,
            "backgroundSecondary": shop.colors.backgroundSecondary or None,
            "backgroundThird": shop.colors.backgroundThird or None,
            "fontColorPrimary": shop.colors.fontColorPrimary or None,
            "fontColorSecondary": shop.colors.fontColorSecondary or None,
            "buttonPrimary": shop.colors.buttonPrimary or None,
            "buttonSecondary": shop.colors.buttonSecondary or None,
        """
        pass

    def validate_chat_infos(self, chat_infos: dict, validator: list):
        """
            "whatsapp": {
                    "is_active": shop.chat_infos.whatsapp.is_active or None,
                    "action": shop.chat_infos.whatsapp.action or None,
                },
            "ia": {
                "is_actiis_activevate": shop.chat_infos.ia.is_active or None,
                "action": shop.chat_infos.ia.action or None
            }
        """
        pass
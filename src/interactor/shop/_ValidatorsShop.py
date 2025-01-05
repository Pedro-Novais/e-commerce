def validate_company_infos(company_infos: dict, validator: list):
    """
        "name": company_infos.name or None,
        "cnpj": shop.company_infos.cnpj or None,
        "ie": shop.company_infos.ie or None,
        "im": shop.company_infos.im or None,
        "phone": shop.company_infos.phone or None,
    """
    if not company_infos.get("name", None):
        validator.append("name")
    
    if not company_infos.get("cnpj", None):
        validator.append("cnpj")

    if not company_infos.get("phone", None):
        validator.append("phone")

    if not company_infos.get("email", None):
        validator.append("email")

def validiate_address(address: dict, validator: list):
    """
        "street": shop.address.street or None,
        "number": shop.address.number or None,
        "complement": shop.address.complement or None,
        "neighborhood": shop.address.neighborhood or None,
        "city": shop.address.city or None,
        "state": shop.address.state or None,
        "country": shop.address.country or None,
        "zipcode": shop.address.zipcode or None,
    """
    if not address.get("street", None):
        validator.append("street")

    if not address.get("number", None):
        validator.append("number")  

    # if not address.get("neighborhood", None):
    #     validator.append("neighborhood")

    if not address.get("city", None):
        validator.append("city")

    if not address.get("state", None):
        validator.append("state")

    if not address.get("country", None):
        validator.append("country")

    if not address.get("zip_code", None):
        validator.append("zip_code")

def validate_images(images: dict, validator: list):
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
    if not images:
        return
    
    if not images.get("logo", None):
        validator.append("logo")
    
    if not images.get("favicon", None):
        validator.append("favicon")
    
    if not images.get("banners", None):
        validator.append("banners")

    for image in images.banner:
        if not image.get("url", None):
            validator.append("url")
        
        if not image.get("position", None):
            validator.append("position")
        
        if not image.get("product_link", None):
            validator.append("product_link")    

def validate_colors(color: dict, valdiate: list):
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

def validate_chat_infos(chat_infos: dict, validator: list):
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
    
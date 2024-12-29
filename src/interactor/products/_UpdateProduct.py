from flask import Request

from utils._I18nShared import I18nShared
from ._I18n import I18n

from repository._ProductRepository import ProductRepository
from repository._CategoryRepository import CategoryRepository

from custom_exceptions._CustomExceptions import (
    NotFoundError,
    FormatInvalidError,
    ParameterNotSend,
    OperationError
)

class UpdateProduct:
    def __init__(self, request: Request, productId: int, shop_name: str):
        self.shop = shop_name
        request = request.get_json()

        self.productId = productId

        if not self.productId:
            raise ParameterNotSend()

        self.name = request.get("name", None)
        
        self.description = request.get("description", None)

        self.is_digital = request.get("is_digital", None)
        if self.is_digital:
            if not isinstance(self.is_digital, bool):
                raise FormatInvalidError()

        self.custom_properties = request.get("custom_properties", None)
        if self.custom_properties:
            if not isinstance(self.custom_properties, list):
                raise FormatInvalidError()

        self.category = request.get("category", None)

    def action(self):
        product_repo = ProductRepository()
        category_repo = CategoryRepository()

        if self.category:
            category_valid = category_repo.get_by_id(id=self.category, shop=self.shop)

            if not category_valid:
                raise NotFoundError(I18n.NOT_FOUND_CATEGORY_TO_ITEM)
        
        update_product = product_repo.update_product(
            shop=self.shop,
            product_id=self.productId,
            name=self.name,
            description=self.description,
            category_id=self.category,
            is_digital=self.is_digital,
            custom_properties=self.custom_properties,
        )

        if not update_product:
            raise OperationError(I18n.ERROR_UPDATE_PRODUCT)
        
        if update_product == I18nShared.ANY_DATA:
             raise NotFoundError(I18n.NOT_FOUND_PRODUCT)
        
        return I18n.SUCCESS_UPDATE_PRODUCT
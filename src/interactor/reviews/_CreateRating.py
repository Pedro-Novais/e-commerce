from flask import Request

from ._I18n import I18n

from repository._ReviewRepository import ReviewRepository
from repository._ProductRepository import ProductRepository

from custom_exceptions._CustomExceptions import (
    OperationError,
    NotFoundError,
    FormatInvalidError
)
class CreateRating:
    def __init__(self, request: Request, userId: int, productId: int, shop_name: str):
        self.shop = shop_name
        self.user = userId
        self.product = productId

        request = request.get_json()

        self.rating = request.get("rating", None)
        if self.rating and not isinstance(self.rating, int):
            raise FormatInvalidError()
        
        self.comment = request.get("comment", None)

        if not self.rating and not self.comment:
            raise NotFoundError(I18n.NOT_FOUND_RATING)

        if self.rating > 5:
            self.rating = 5

        elif self.rating < 0:
            self.rating = 0
          
    def action(self):
        review_repo = ReviewRepository()
        product_repo = ProductRepository()

        product = product_repo.get_by_id(id=self.product, shop=self.shop)

        if not product:
            raise NotFoundError(I18n.NOT_FOUND_PRODUCT)
        
        new_review = review_repo.create_rating(
            shop = self.shop,
            user = self.user,
            product = self.product,
            rating = self.rating,
            comment = self.comment
        )

        if not new_review:
            raise OperationError(I18n.ERROR_ADDIDNG_RATING)
        
        return I18n.SUCCESS_ADDING_RATING

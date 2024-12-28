from flask import Request

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
            raise NotFoundError("Nenhuma avaliação foi realizada!")

        if self.rating > 5:
            self.rating = 5

        elif self.rating < 0:
            self.rating = 0
          
    def action(self):
        review_repo = ReviewRepository()
        product_repo = ProductRepository()

        product = product_repo.get_by_id(id=self.product, shop=self.shop)

        if not product:
            raise NotFoundError("Produto não foi encontrado!")
        
        new_review = review_repo.create_rating(
            shop = self.shop,
            user = self.user,
            product = self.product,
            rating = self.rating,
            comment = self.comment
        )

        if not new_review:
            raise OperationError("Erro ao adicionar comentário!")
        
        return "Comentário adicionado com sucesso!"

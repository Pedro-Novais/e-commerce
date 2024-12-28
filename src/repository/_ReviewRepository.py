from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.ReviewsModel import Review

class ReviewRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Review,
            conn=self.conn
        )

    def create_rating(
            self,
            shop: str,
            user: int,
            product: int,
            rating: int,
            comment: str = None
            ):
        with self.conn.get_db_session() as db:
            new_rating = Review(
                product_id = product,
                user_id = user,
                shop_name = shop,
                rating = rating,
                comment = comment
            )

            db.add(new_rating)
            db.commit()
            db.refresh(new_rating)

            return new_rating
from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.ProductModel import Product

class ProductRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Product,
            conn=self.conn
        )

    def create_product(
            self,
            name: str,
            description: str,
            price: float,
            category_id = int,
            stock_quantity: int = 0,
            ):
        with self.conn.get_db_session() as db:
            new_product = Product(
                name=name,
                description=description,
                price=price,
                stock_quantity=stock_quantity,
                category_id=category_id
            )

            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return new_product
from sqlalchemy.orm import joinedload
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

    def get_all_products(self):
        with self.conn.get_db_session() as db:
            return db.query(Product).options(joinedload(Product.category)).all()
    

    def create_product(
            self,
            name: str,
            description: str,
            price: float,
            category_id: int,
            custom_properties: list,
            images: list = [],
            stock_quantity: int = 0,
            is_digital: bool = False
            ):
        with self.conn.get_db_session() as db:
            new_product = Product(
                name=name,
                description=description,
                price=price,
                stock_quantity=stock_quantity,
                is_digital = is_digital,
                custom_properties=custom_properties,
                images=images,
                category_id=category_id
            )

            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return new_product
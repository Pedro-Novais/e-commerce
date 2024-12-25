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
        
    def update_product(
            self,
            product_id: int = None,
            name: str = None,
            description: str = None,
            price: float = None,
            category_id: int = None,
            custom_properties: list = None,
            images: list = None,
            stock_quantity: int = None,
            is_digital: bool = None
            ):
        with self.conn.get_db_session() as db:
            product = db.query(Product).filter(Product.id == product_id).first()

            if not product:
                return "AnyData"
            
            if name:
                product.name = name
            
            if description:
                product.description = description

            if price:
                product.price = price

            if category_id:
                product.category_id = category_id

            if custom_properties:
                product.custom_properties = custom_properties

            if images:
                product.images = images
            
            if stock_quantity:
                product.stock_quantity = stock_quantity

            if is_digital:
                product.is_digital = is_digital

            db.commit()
            db.refresh(product)
            return product
from sqlalchemy.orm import joinedload

from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository

from model.ProductModel import Product
from model.ProductVariantsModel import ProductVariants

from utils._I18nShared import I18nShared

class ProductRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Product,
            conn=self.conn
        )

    def get_one_product(self, id: int, shop: str):
        with self.conn.get_db_session() as db:
            return db.query(Product).filter(Product.id == id).filter(Product.shop_name == shop).options(joinedload(Product.variants)).first()

    def get_all_products(self, shop: str):
        with self.conn.get_db_session() as db:
            return db.query(Product).filter(Product.shop_name == shop).options(joinedload(Product.category)).options(joinedload(Product.variants)).all()
    

    def create_product(
            self,
            shop: str,
            name: str,
            description: str,
            category_id: int,
            custom_properties: list,
            product_variants: list,
            is_digital: bool = False
            ):
        with self.conn.get_db_session() as db:
            new_product = Product(
                shop_name = shop,
                name = name,
                description = description,
                is_digital = is_digital,
                custom_properties = custom_properties,
                category_id = category_id
            )

            db.add(new_product)
            db.commit()
            db.refresh(new_product)

            for product_variant in product_variants:
                new_variants = ProductVariants(
                    product_id=new_product.id,
                    price=product_variant.get("price"),
                    color=product_variant.get("color", None),
                    size=product_variant.get("size", None),
                    images=product_variant.get("images", []),
                    shop_name=shop,
                )

                db.add(new_variants)

            db.commit()
            return new_product
        
    def update_product(
            self,
            shop: str,
            product_id: int = None,
            name: str = None,
            description: str = None,
            category_id: int = None,
            custom_properties: list = None,
            is_digital: bool = None
            ):
        with self.conn.get_db_session() as db:
            product = db.query(Product).filter(Product.id == product_id).filter(Product.shop_name == shop).first()

            if not product:
                return I18nShared.ANY_DATA
            
            if name:
                product.name = name
            
            if description:
                product.description = description

            if category_id:
                product.category_id = category_id

            if custom_properties:
                product.custom_properties = custom_properties

            if is_digital:
                product.is_digital = is_digital

            db.commit()
            db.refresh(product)
            return product
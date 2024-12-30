from sqlalchemy import select

from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.ProductVariantsModel import ProductVariants

class ProductVariantsRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=ProductVariants,
            conn=self.conn
        )

    def get_items_from_order(self, items: list[dict] = []):
        with self.conn.get_db_session() as db:
            item_ids = [item["id"] for item in items]

            existing_ids = db.execute(select(ProductVariants.id).where(ProductVariants.id.in_(item_ids))).scalars().all()

            existing_ids_set = set(existing_ids)

            missing_items = set(item_ids) - existing_ids_set

            if missing_items:
                return False
            
            return existing_ids
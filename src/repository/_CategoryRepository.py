from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.CategoryModel import Category

class CategoryRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Category,
            conn=self.conn
        )

    def create_category(
            self,
            shop: str,
            name: str,
            description: str
            ):
        with self.conn.get_db_session() as db:
            new_category = Category(
                shop_name=shop,
                name=name,
                description=description
            )

            db.add(new_category)
            db.commit()
            db.refresh(new_category)

            return new_category
        
    def update_category(
            self,
            shop: str,
            category_id: int = None,
            name: str = None,
            description: str = None,
            ):
        with self.conn.get_db_session() as db:
            category_update = db.query(Category).filter(Category.id == category_id).filter(Category.shop_name == shop).first()

            if not category_update:
                return "AnyData"
            
            if name:
                category_update.name = name
            
            if description:
                category_update.description = description

            db.commit()
            db.refresh(category_update)
            return category_update
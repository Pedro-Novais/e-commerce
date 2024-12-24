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
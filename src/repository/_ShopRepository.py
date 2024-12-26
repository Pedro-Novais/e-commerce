from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.ShopModel import Shop

class ShopRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Shop,
            conn=self.conn
        )

    def get_by_name(self, name: str):
        with self.conn.get_db_session() as db:
            return db.query(self.Data).filter(self.Data.name == name).first()
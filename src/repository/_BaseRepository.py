from utils._I18nShared import I18nShared

class BaseRepository:
    def __init__(self, DataModel, conn):
        self.Data = DataModel
        self.conn = conn

    def get_all(self, shop):
        with self.conn.get_db_session() as db:
            return db.query(self.Data).filter(self.Data.shop_name == shop).all()
        
    def get_by_id(self, id: int, shop: str ):
        with self.conn.get_db_session() as db:
            return db.query(self.Data).filter(self.Data.id == id).filter(self.Data.shop_name == shop).first()
        
    def delete(self, id: int, shop: str):
        with self.conn.get_db_session() as db:
            data = db.query(self.Data).filter(self.Data.id == id).filter(self.Data.shop_name == shop).first()

            if not data:
                return I18nShared.ANY_DATA
            
            db.delete(data)
            db.commit()
            return data
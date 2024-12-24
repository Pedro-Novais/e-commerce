class BaseRepository:
    def __init__(self, DataModel, conn):
        self.Data = DataModel
        self.conn = conn

    def get_all(self):
        with self.conn.get_db_session() as db:
            return db.query(self.Data).all()
        
    def get_by_id(self, id: int ):
        with self.conn.get_db_session() as db:
            return db.query(self.Data).filter(self.Data.id == id).first()
        
    def delete(self, id: int):
        with self.conn.get_db_session() as db:
            data = db.query(self.Data).filter(self.Data.id == id).first()

            if not data:
                return None
            
            db.delete(data)
            db.commit()
            return data
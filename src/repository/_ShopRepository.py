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
        
    def create_shop(
        self,
        name: str,
        company_infos: str,
        address: dict,
        subdomain: str,
        chat_infos: list = [],
        colors: list = [],
        images: list = [],
        is_active: bool = False 
    ):
        with self.conn.get_db_session() as db:
            new_shop = Shop(
                name=name,
                subdomain=subdomain,
                company_infos=company_infos,
                chat_infos=chat_infos,
                colors=colors,
                images=images,  
                address=address,
                is_active=is_active
            )

            db.add(new_shop)
            db.commit()
            db.refresh(new_shop)

            return new_shop
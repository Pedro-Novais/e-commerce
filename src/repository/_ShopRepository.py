from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.ShopModel import Shop

from utils._I18nShared import I18nShared
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
    
    def update_shop(
        self,
        name_subdomain: str = None,
        company_infos: str = None,
        address: dict = None,
        subdomain: str = None,
        chat_infos: list = None,
        colors: list = None,
        images: list = None,
        is_active: bool = False 
    ):
        with self.conn.get_db_session() as db:
            update_shop = db.query(Shop).filter(Shop.name == name_subdomain).first()

            if not update_shop:
                return I18nShared.ANY_DATA
            
            if company_infos:
                update_shop.company_infos = company_infos
            
            if address:
                update_shop.address = address
            
            if chat_infos:
                update_shop.chat_infos = chat_infos
            
            if colors:
                update_shop.colors = colors
            
            if images:
                update_shop.images = images

            db.commit()
            db.refresh(update_shop)

            return update_shop
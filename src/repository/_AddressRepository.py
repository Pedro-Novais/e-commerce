from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.AdressModel import Address

class AddressRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Address,
            conn=self.conn
        )

    def get_all_address(self, user_id: int):
        with self.conn.get_db_session() as db:
            return db.query(Address).filter(Address.user_id == user_id).all()
    
    def create_address(
            self,
            user_id: int,
            shop_name: str, 
            street: str,
            number: int,
            city: str,
            state: str, 
            zip_code: str,
            country: str = "Brasil"
        ):
        with self.conn.get_db_session() as db:

            new_address = Address(
                user_id=user_id,
                shop_name=shop_name,
                street=street,
                number=number,
                city=city,
                state=state,
                zip_code=zip_code
            )

            db.add(new_address)
            db.commit()
            db.refresh(new_address)
            return new_address
        
    def update_address(
            self,
            user_id: int,
            shop_name: str, 
            address_id: int,
            street: str,
            number: int,
            city: str,
            state: str,
            zip_code: str,
            country: str = "Brasil"
            ):
        with self.conn.get_db_session() as db:
            address = db.query(Address).filter(Address.id == address_id).filter(Address.user_id == user_id).filter(Address.shop_name == shop_name).first()

            if not address:
                return "AnyData"
            
            if street:
                address.street = street

            if number:
                address.number = number

            if city:
                address.city = city

            if state:
                address.state = state

            if zip_code:
                address.zip_code = zip_code

            db.commit()
            db.refresh(address)
            return address
        
    def delete_address(self,  user_id: int, address_id: int, shop_name: str):
        with self.conn.get_db_session() as db:
            address = db.query(Address).filter(Address.id == address_id).filter(Address.user_id == user_id).filter(Address.shop_name == shop_name).first()

            if not address:
                return "AnyData"
            
            db.delete(address)
            db.commit()
            return address
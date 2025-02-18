from sqlalchemy.orm import joinedload
from .Conn import ConnDatabase
from ._BaseRepository import BaseRepository
from model.UserModel import User

class UserRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=User,
            conn=self.conn
        )

    def get_all_user(self):
        with self.conn.get_db_session() as db:
            return db.query(User).all()
        
    def get_user_by_id(self, user_id: int, shop: str):
        with self.conn.get_db_session() as db:
            return db.query(User).options(joinedload(User.addresses)).filter(User.id == user_id).filter(User.shop_name == shop).first()
    
    def get_user_by_email(self, email: str, shop: str ):
        with self.conn.get_db_session() as db:
            return db.query(User).filter(User.email == email).filter(User.shop_name == shop).first()
        
    def create_user(
            self,
            shop_name: str,
            name: str,
            email: str,
            password: str,
            is_admin: bool = False  
            ):
            with self.conn.get_db_session() as db:

                new_user = User(
                    name=name,
                    email=email,
                    password=password,
                    is_admin=is_admin,
                    shop_name = shop_name
                )

                db.add(new_user)
                db.commit()
                db.refresh(new_user)
                return new_user
        
    def update_user(
            self,
            user_id: int,
            name: str = None,
            email: str = None,
            password: str = None,
            is_admin: bool = None  
            ):
        with self.conn.get_db_session() as db:
            user = db.query(User).filter(User.id == user_id).first()

            if not user:
                return None
            
            if name:
                user.name = name
            
            if email:
                user.email = email

            if password:
                user.password = password

            if is_admin:
                user.is_admin = is_admin

            db.commit()
            db.refresh(user)
            return user
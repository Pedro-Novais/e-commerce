import bcrypt
import jwt
import os

from datetime import datetime, timedelta
from dotenv import load_dotenv

def generate_token(user_id: int):
    load_dotenv()

    expiration_time = datetime.utcnow() + timedelta(hours=1)

    token = jwt.encode({
        'user_id': user_id,
        'exp': expiration_time
    }, os.getenv("SECRET_KEY"), algorithm='HS256')

    return token

def hash_password(
        password: str
        ) -> str:
    
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def check_password(
        password_save: str, 
        password_sended: str
        ) -> bool:
    
    return bcrypt.checkpw(password_sended.encode('utf-8'), password_save.encode('utf-8'))
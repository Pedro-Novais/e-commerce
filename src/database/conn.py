from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from custom_exceptions._CustomExceptions import OperationError
from contextlib import contextmanager
from dotenv import load_dotenv
import os

class ConnDatabase:
    def __init__(self):
        load_dotenv()
    
        engine = create_engine(os.getenv('DATABASE_URL'))
        self.SessionLocal = sessionmaker(bind=engine)

    @contextmanager
    def get_db_session(self):
        db = self.SessionLocal()
        try:
            yield db 
        except Exception as e:
            db.rollback()  
            raise OperationError(message="Algum erro ocorreu ao salvar os dados!", error=e)
        finally:
            db.close() 
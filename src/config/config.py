import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

Base = declarative_base()
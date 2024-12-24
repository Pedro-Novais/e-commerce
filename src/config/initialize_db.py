from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import Base

from model import (
    UserModel,
    ReviewsModel,
    CouponsModel,
    PaymentsModel,
    ProductModel,
    AdressModel,
    InventoryModel,
    OrderItemModel,
    OrderModel,
    CategoryModel
)



def initialize_database(app: Flask) -> None:
    try:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        Base.metadata.create_all(bind=engine)
        print(Base.metadata.tables)

    except Exception as e:
        print("algum erro ocorreu ao inicializar as tabelas, erro; {}".format(e))

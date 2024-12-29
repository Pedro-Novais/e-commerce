import os
from flask import Flask
from sqlalchemy import create_engine

from dotenv import load_dotenv

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
    CategoryModel,
    CartModel,
    ShopModel,
    ProductVariantsModel,
    CartItemModel
)



def initialize_database(app: Flask) -> None:
    try:
        load_dotenv()
        engine = create_engine(os.getenv('DATABASE_URL'))
        Base.metadata.create_all(bind=engine)

    except Exception as e:
        print("algum erro ocorreu ao inicializar as tabelas, erro; {}".format(e))

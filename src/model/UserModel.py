from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from config.config import Base

from .AdressModel import Address

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    shop_name = Column(String, ForeignKey('shops.name'))
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False) 
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    addresses = relationship("Address", back_populates="user")
    orders = relationship("Order", back_populates="user")
    shop = relationship("Shop", back_populates="users")
    cart = relationship("Cart", back_populates="user")
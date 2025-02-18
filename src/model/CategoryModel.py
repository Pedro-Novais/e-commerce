from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from config.config import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    shop_name = Column(String, ForeignKey('shops.name'), nullable=False) 
    name = Column(String(150), nullable=False, unique=True)
    description = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")
    shop = relationship("Shop", back_populates="categories")
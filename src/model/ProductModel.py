from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, DECIMAL, func
from sqlalchemy.orm import relationship
from config.config import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
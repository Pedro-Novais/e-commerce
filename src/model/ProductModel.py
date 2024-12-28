from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, DECIMAL, JSON, BOOLEAN, func
from sqlalchemy.orm import relationship
from config.config import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    is_digital = Column(BOOLEAN, default=False, nullable=False)
    custom_properties = Column(JSON, default=list)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete="CASCADE"))
    shop_name = Column(String, ForeignKey('shops.name'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    shop = relationship("Shop", back_populates="products")
    variants = relationship("ProductVariants", back_populates="product", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="product")
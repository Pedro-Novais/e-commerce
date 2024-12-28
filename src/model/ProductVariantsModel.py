from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, DECIMAL, JSON, BOOLEAN, func
from sqlalchemy.orm import relationship
from config.config import Base

class ProductVariants(Base):
    __tablename__ = 'product_variants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    color = Column(String(50), nullable=True)  
    size = Column(String(50), nullable=True) 
    images = Column(JSON, default=list)
    shop_name = Column(String, ForeignKey('shops.name'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="variants")
    shop = relationship("Shop", back_populates="product_variants")
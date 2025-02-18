from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from config.config import Base

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    shop_name = Column(String, ForeignKey('shops.name'))
    quantity_change = Column(Integer, nullable=False) 
    reason = Column(String(255))
    created_at = Column(DateTime, default=func.now())

    product = relationship("Product")
    shop = relationship("Shop", back_populates="inventory")
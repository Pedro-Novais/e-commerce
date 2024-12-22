from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from config.config import Base

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity_change = Column(Integer, nullable=False)  # positivo para entrada, negativo para saída
    reason = Column(String(255))
    created_at = Column(DateTime, default=func.now())

    product = relationship("Product")
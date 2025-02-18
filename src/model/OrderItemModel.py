from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, String
from sqlalchemy.orm import relationship
from config.config import Base

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_variant_id = Column(Integer, ForeignKey('product_variants.id'))
    shop_name = Column(String, ForeignKey('shops.name'))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product_variant  = relationship("ProductVariants", back_populates="order_items")
    shop = relationship("Shop", back_populates="order_items")

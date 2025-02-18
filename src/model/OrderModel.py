from sqlalchemy import Column, JSON, Text, String, Integer, ForeignKey, DateTime, DECIMAL, func
from sqlalchemy.orm import relationship
from config.config import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    shop_name = Column(String, ForeignKey('shops.name'))
    payer_email = Column(String(100))
    payer_address = Column(JSON)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    discount = Column(DECIMAL(10, 2), default=0.00)
    tax = Column(DECIMAL(10, 2), default=0.00)
    shipping_fee = Column(DECIMAL(10, 2), default=0.00)
    shipment_tracking_number = Column(String(255))
    delivery_date = Column(DateTime)
    reason = Column(Text)
    status = Column(String(50), default='NEW')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order")
    address = relationship("Address", back_populates="orders")
    shop = relationship("Shop", back_populates="orders") 
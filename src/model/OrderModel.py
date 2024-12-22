from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, DECIMAL, func
from sqlalchemy.orm import relationship
from config.config import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), default='PENDING')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order")
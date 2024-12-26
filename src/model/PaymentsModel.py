from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from config.config import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    shop_name = Column(String, ForeignKey('shops.name')) 
    payment_method = Column(String(50), nullable=False)  
    status = Column(String(50), default='PENDING')
    transaction_id = Column(String(255))
    paid_at = Column(DateTime)
    created_at = Column(DateTime, default=func.now())

    order = relationship("Order", back_populates="payment")
    shop = relationship("Shop", back_populates="payments")

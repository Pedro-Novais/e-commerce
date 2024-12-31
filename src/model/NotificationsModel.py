from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from config.initialize_db import Base

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    shop_name = Column(String, ForeignKey('shops.name'))
    notification_id = Column(String(255))  
    notification_type = Column(String(50), default="payment")  
    data = Column(JSON)  
    processed = Column(String(10), default='PENDING')
    received_at = Column(DateTime, default=func.now())
    processed_at = Column(DateTime, nullable=True)
    retry_quantity = Column(Integer, default=0)

    shop = relationship("Shop", back_populates="notifications")
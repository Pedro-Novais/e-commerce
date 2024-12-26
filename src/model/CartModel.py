from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime, String, func
from sqlalchemy.orm import relationship
from config.config import Base

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    shop_name = Column(String, ForeignKey('shops.name'), nullable=False) 
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="cart")
    cart_items = relationship("CartItem", back_populates="cart")
    shop = relationship("Shop") 
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime, String, func
from sqlalchemy.orm import relationship
from config.config import Base

class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    shop_name = Column(String, ForeignKey('shops.name'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)  
    price = Column(DECIMAL(10, 2), nullable=False)  

    cart = relationship("Cart", back_populates="cart_items")  
    product = relationship("Product")  
    shop = relationship("Shop")
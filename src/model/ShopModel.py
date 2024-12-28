from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, DECIMAL, JSON, BOOLEAN, func
from sqlalchemy.orm import relationship
from config.config import Base

class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    subdomain = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship("Order", back_populates="shop")
    products = relationship("Product", back_populates="shop")
    product_variants = relationship("ProductVariants", back_populates="shop")
    users = relationship("User", back_populates="shop")
    reviews = relationship("Review", back_populates="shop")
    payments = relationship("Payment", back_populates="shop")
    order_items = relationship("OrderItem", back_populates="shop")
    inventory = relationship("Inventory", back_populates="shop")
    coupons = relationship("Coupon", back_populates="shop")
    categories = relationship("Category", back_populates="shop")
    addresses = relationship("Address", back_populates="shop")
    carts = relationship("Cart", back_populates="shop")
    cart_items = relationship("CartItem", back_populates="shop")  
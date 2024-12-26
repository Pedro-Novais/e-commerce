from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, String, func
from sqlalchemy.orm import relationship
from config.config import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    shop_name = Column(String, ForeignKey('shops.name'))
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=func.now())

    product = relationship("Product")
    user = relationship("User")
    shop = relationship("Shop", back_populates="reviews")

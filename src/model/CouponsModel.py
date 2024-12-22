from sqlalchemy import Column, String, Integer, DateTime, DECIMAL, func
from sqlalchemy.orm import relationship
from config.config import Base

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_percentage = Column(DECIMAL(5, 2))
    discount_amount = Column(DECIMAL(10, 2))
    usage_limit = Column(Integer, default=1)
    expiration_date = Column(DateTime)
    created_at = Column(DateTime, default=func.now())
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from config.config import Base

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    street = Column(String(150), nullable=False)
    number = Column(Integer, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)
    country = Column(String(100), default='Brasil')
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="addresses")
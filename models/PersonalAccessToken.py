from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PersonalAccessToken(Base): 
    __tablename__ = "personal_access_tokens"
``
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(Enum('jwt', 'others'), nullable=False)
    secret = Column(String(255), nullable=False)
    redirect = Column(String(255), nullable=True)
    revoked_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime)

    user = relationship('User', backref='personal_access_tokens')
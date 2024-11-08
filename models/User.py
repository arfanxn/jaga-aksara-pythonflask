from typing import List

from sqlalchemy import Column, Integer, String, Enum, DateTime, CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from models import PersonalAccessToken 

Base = declarative_base()

class User(Base): 
    __tablename__ = "users"

    id = Column(CHAR(36), primary_key=True)
    country_code = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    phone = Column(String(16), unique=True, nullable=False)
    sex = Column(Enum('male', 'female'), nullable=False)
    level = Column(Enum('standard', 'admin'), nullable=False)
    birth_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # personal_access_tokens:Mapped[List["PersonalAccessToken"]] = relationship(back_populates='users')

    def __repr__(self) -> str:        
        return f"User(id={self.id!r}, name={self.name!r})"

    def to_json(self):
        return {    
            "id": self.id,
            "country_code" : self.country_code,
            "name": self.name,
            "phone": self.phone,    
            "sex": self.sex,
            "level": self.level,
            "birth_date": self.birth_date.isoformat(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None
        }
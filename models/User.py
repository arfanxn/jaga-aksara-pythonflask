from typing import List

from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from models import PersonalAccessToken 

Base = declarative_base()

class User(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(Enum('male', 'female', 'non-binary'), nullable=False)
    birth_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # personal_access_tokens:Mapped[List["PersonalAccessToken"]] = relationship(back_populates='users')

    def __repr__(self) -> str:        
        return f"User(id={self.id!r}, name={self.name!r})"

    def to_json(self):
        return {    
            "id": self.id,
            "name": self.name,
            "email": self.email,    
            "gender": self.gender,
            "birth_date": self.birth_date.isoformat(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None
        }
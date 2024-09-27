from sqlalchemy import String
from sqlalchemy import Column, Integer, String, Enum, DateTime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(Enum('male', 'female', 'non-binary'), nullable=False)
    birth_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.name!r})"
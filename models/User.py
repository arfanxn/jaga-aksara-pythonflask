from pony.orm import PrimaryKey, Required, Optional, Set
from db import get_db
from datetime import datetime, date, time
from enums import UserSexEnum, UserLevelEnum
from models import Otp
import uuid


class User(get_db().Entity):
    _table_ = 'users'

    id = PrimaryKey(str, default=lambda: str(uuid.uuid4()))  
    country_code = Required(int)
    phone = Required(str, unique=True)
    name = Required(str)
    sex = Required(str) # use the UserSexEnum.MALE.value, UserSexEnum.FEMALE.values
    level = Required(str) # use the UserLevelEnum.STANDARD.value, UserLevelEnum.ADMIN.value
    birth_date = Required(date)
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime)

    otps = Set('Otp')  # user has many otps
    articles = Set('Article')  # user has many articles
    transliterations = Set('Transliteration')  # user has many transliterations
    chats = Set('Chat')  # user has many chats
    
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
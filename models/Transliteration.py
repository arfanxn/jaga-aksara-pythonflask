from pony.orm import PrimaryKey, Required, Optional
from db import get_db
from datetime import datetime
from models import User


class Transliteration(get_db().Entity):
    _table_ = 'transliterations'

    id = PrimaryKey(int, auto=True)  
    photo = Required(str)
    result = Required(str) 
    impression = Required(int, default=0) 
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime)

    user = Required('User', column='user_id') # article belongs to user (user)
    
    def to_json(self):
        return {    
            "id": self.id,
            "photo": self.photo,
            "result": self.result,
            "impression": self.impression,
            "created_at": self.created_at.isoformat(),
            "created_at_formatted": self.created_at.strftime('%Y-%m-%d'),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None,

            "user": self.user.to_json(),
        }
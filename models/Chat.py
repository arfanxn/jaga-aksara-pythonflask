from pony.orm import PrimaryKey, Required, Optional
from db import get_db
from datetime import datetime
from models import User


class Chat(get_db().Entity):
    _table_ = 'chats'

    id = PrimaryKey(int, auto=True)  
    question = Required(str)
    answer = Required(str) 
    status = Required(str) # use the ChatStatusEnum.ACTIVE.value, ChatStatusEnum.DELETED.values
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime)

    user = Required('User', column='user_id') # article belongs to user (user)
    
    def to_json(self):
        return {    
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None,

            "user": self.user.to_json(),
        }
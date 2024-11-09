from pony.orm import PrimaryKey, Required, Optional
from db import get_db
from datetime import datetime
from models import User


class Article(get_db().Entity):
    _table_ = 'articles'

    id = PrimaryKey(int, auto=True)  
    title = Required(str)
    thumbnail = Required(str)
    content = Required(str) 
    impression = Required(int, default=0) 
    view_time = Required(int, default=0) 
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime)

    author = Required('User', column='user_id') # article belongs to author (user)
    
    def to_json(self):
        return {    
            "id": self.id,
            "title": self.title,
            "thumbnail": self.thumbnail,
            "content": self.content,
            "impression": self.impression,
            "view_time": self.view_time,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None,

            "author": self.author.to_json(),
            "author_name" : self.author.name 
        }
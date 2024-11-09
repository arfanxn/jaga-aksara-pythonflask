from pony.orm import PrimaryKey, Required, Optional, Set
from db import get_db
from datetime import datetime, date, time
from enums import OtpStatusEnum
from models import User
import random 


class Otp(get_db().Entity):
    _table_ = 'otps'

    id = PrimaryKey(int, auto=True)  
    # user_id = Required(str)
    code = Required(int, default=lambda: random.randint(100000, 999999))
    status = Required(str, default=OtpStatusEnum.AVAILABLE.value) # use the OtpStatusEnum.AVAILABLE.value, OtpStatusEnum.USED.value
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime)

    user = Required('User', column='user_id') # otp belongs to user 

    def to_json(self):
        return {    
            "id": self.id,
            "user_id" : self.user_id,
            "code": self.code,
            "status": self.status,    
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None
        }
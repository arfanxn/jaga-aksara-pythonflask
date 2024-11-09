from db import get_db
import config

db = get_db()

from .User import User
from .Otp import Otp
from .PersonalAccessToken import PersonalAccessToken

config.inject_into_db(db)

db.generate_mapping(create_tables=False)
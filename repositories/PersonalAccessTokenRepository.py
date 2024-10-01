import db

from models import PersonalAccessToken
from sqlalchemy.sql import func

class PersonalAccessTokenRepository: 

    def create_or_update(pat:PersonalAccessToken): 
        db_session = db.get_session()
        query =  db_session.query(PersonalAccessToken)

        if pat.id is not None:
            query = query.where(PersonalAccessToken.id == pat.id)
        if pat.user_id is not None:
            query = query.where(PersonalAccessToken.user_id == pat.user_id)
        if pat.name is not None:
            query = query.where(PersonalAccessToken.name == pat.name)        
        
        retrieved_pat = query.first()
        if retrieved_pat is None:
            db_session.add(pat)
            retrieved_pat = pat
        else :
            retrieved_pat.name = pat.name
            retrieved_pat.secret = pat.secret
            retrieved_pat.redirect = pat.redirect
            retrieved_pat.revoked_at = pat.revoked_at
            retrieved_pat.updated_at = func.now()

        db_session.commit()

        return retrieved_pat
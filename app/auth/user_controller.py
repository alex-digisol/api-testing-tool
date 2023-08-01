from flask_login import UserMixin

from sqlalchemy import select, insert
from app.database import get_db, users, user_providers




class UserController(UserMixin):
    def __init__(self, name, email, profile_pic):
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    def get_id(self):
        try:
            return str(self.email)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None

    @staticmethod
    def get(email):
        db = get_db()
        sql = select(users).where(users.c.email == email)
        user = db.execute(sql).fetchone()

        if not user:
            return None

        return {
            "name": user.name, 
            "email": user.email, 
            "profile_pic": user.profile_pic
        }

    @staticmethod
    def create(name, email, profile_pic, provider):
        db = get_db()
        q_user = insert(users).values(
            name=name,
            email=email,
            profile_pic=profile_pic,
        )
        result = db.execute(q_user)
        q_provider = insert(user_providers).values(
            user_id=result.inserted_primary_key[0],
            provider=provider
        )
        result = db.execute(q_provider)
        db.commit()
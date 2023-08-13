from api.db import db, BaseModelMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User(email={self.email!r})>'.format(self=self)

    @classmethod
    def create(cls, new_user):
        user = cls.get_by_email(new_user.email)
        if user:
            return None
        new_user.save()
        return new_user

    @classmethod
    def get_by_email(cls, email):
        return cls.simple_filter_one(email=email)

    @classmethod
    def login(cls, email, password):
        user = cls.get_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return None
        return user

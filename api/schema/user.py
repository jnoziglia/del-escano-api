from marshmallow import fields, post_load
from api.ext import ma
from api.model.user import User


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String()
    password = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


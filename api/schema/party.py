from marshmallow import fields, post_load
from api.ext import ma
from api.model.party import Party


class PartySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    votes = fields.Integer()
    seats = fields.Integer()

    @post_load
    def make_party(self, data, **kwargs):
        return Party(**data)

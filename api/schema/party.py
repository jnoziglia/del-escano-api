from marshmallow import Schema, fields, post_load
from api.model.party import Party


class PartySchema(Schema):
    name = fields.Str()
    votes = fields.Int()
    seats = fields.Int()

    @post_load
    def make_party(self, data, **kwargs):
        return Party(**data)

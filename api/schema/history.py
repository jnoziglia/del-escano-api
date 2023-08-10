from marshmallow import fields, post_load
from api.ext import ma
from api.model.history import History
from api.schema.party import PartySchema


class HistorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    seat_count = fields.Integer()
    result = fields.List(fields.Nested(PartySchema()))
    created_at = fields.DateTime()

    @post_load
    def make_history(self, data, **kwargs):
        return History(**data)

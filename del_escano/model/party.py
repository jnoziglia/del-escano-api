import datetime as dt

from marshmallow import Schema, fields, post_load


class Party(object):
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def __repr__(self):
        return '<Party(name={self.name!r})>'.format(self=self)


class PartySchema(Schema):
    name = fields.Str()
    votes = fields.Int()

    @post_load
    def make_party(self, data, **kwargs):
        return Party(**data)

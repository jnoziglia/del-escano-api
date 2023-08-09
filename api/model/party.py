from api.db import db, BaseModelMixin


class Party(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    votes = db.Column(db.Integer, nullable=False)

    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.seats = 0

    def __repr__(self):
        return '<Party(name={self.name!r})>'.format(self=self)

from api.db import db, BaseModelMixin


class Party(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    votes = db.Column(db.Integer, nullable=False)

    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.seats = 0

    @db.orm.reconstructor
    def init_on_load(self):
        self.seats = 0

    def __repr__(self):
        return '<Party(name={self.name!r})>'.format(self=self)

    def calculate_dhont_quot(self):
        quot = self.votes / (self.seats + 1)
        return quot

    def already_exists(self):
        return Party.query.filter_by(name=self.name).first() is not None

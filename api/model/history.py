from api.db import db, BaseModelMixin
import datetime as dt


class History(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    seat_count = db.Column(db.Integer, nullable=False)
    result = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, seat_count, result):
        self.seat_count = seat_count
        self.result = result
        self.created_at = dt.datetime.utcnow()

    def __repr__(self):
        return '<History(seat_count={self.seat_count!r})>'.format(self=self)
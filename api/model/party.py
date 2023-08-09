import datetime as dt


class Party:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.seats = 0

    def __repr__(self):
        return '<Party(name={self.name!r})>'.format(self=self)

    def set_seat(self, seats):
        self.seats = seats

import datetime as dt


class Party:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def __repr__(self):
        return '<Party(name={self.name!r})>'.format(self=self)

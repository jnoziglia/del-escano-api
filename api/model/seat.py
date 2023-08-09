class Seat:
    def __init__(self, parties):
        self.parties = parties

    def __repr__(self):
        return '<Seat(parties={self.parties!r})>'.format(self=self)

    def calculate_seats(self, seat_count):
        self.reset_seats()
        for i in range(seat_count):
            self.parties.sort(key=lambda party: party.votes / (party.seats + 1), reverse=True)
            self.parties[0].seats = self.parties[0].seats + 1
        return self.parties

    def set_parties(self, parties):
        self.parties = parties
        return self.parties

    def reset_seats(self):
        for party in self.parties:
            party.seats = 0

from flask import jsonify, request, Blueprint
from api.schema.party import PartySchema
from api.model.party import Party
from api.model.seat import Seat

app_file1 = Blueprint('app_file1', __name__)
init_seats = Seat([])


@app_file1.route("/parties", methods=['GET'])
def get_parties():
    parties = Party.get_all()
    schema = PartySchema(many=True)
    result = schema.dump(parties)
    return jsonify(result)


@app_file1.route("/parties", methods=['POST'])
def add_party():
    schema = PartySchema()
    party = schema.load(request.get_json())
    party.save()
    resp = schema.dump(party)
    return resp, 204


@app_file1.route("/seats", methods=['GET'])
def get_seats():
    parties = Party.get_all()
    schema = PartySchema(many=True)
    init_seats.set_parties(parties)
    seats = schema.dump(init_seats.calculate_seats(int(request.args.get('seat_count'))))
    return jsonify(seats)

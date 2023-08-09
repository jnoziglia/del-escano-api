from flask import jsonify, request, Blueprint
from api.schema.party import PartySchema
from api.model.party import Party
from api.model.seat import Seat

app_file1 = Blueprint('app_file1', __name__)

init_parties = [
    Party('Fdt', 5000000),
    Party('Pro', 3000000),
    Party('Lla', 2500000)
]

init_seats = Seat(init_parties)


@app_file1.route("/parties", methods=['GET'])
def get_parties():
    schema = PartySchema(many=True)
    parties = schema.dump(init_parties)
    return jsonify(parties)


@app_file1.route("/parties", methods=['POST'])
def add_party():
    party = PartySchema().load(request.get_json())
    init_parties.append(party)
    return '', 204


@app_file1.route("/seats", methods=['GET'])
def get_seats():
    schema = PartySchema(many=True)
    seats = schema.dump(init_seats.calculate_seats(int(request.args.get('seat_count'))))
    return jsonify(seats)

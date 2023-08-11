from flask import jsonify, request, Blueprint
from api.schema.party import PartySchema
from api.model.party import Party
from api.schema.history import HistorySchema
from api.model.history import History

app_file1 = Blueprint('app_file1', __name__)


@app_file1.route("/parties", methods=['GET'])
def get_parties():
    parties = Party.get_all()
    schema = PartySchema(many=True, only=("name", "votes"))
    result = schema.dump(parties)
    return jsonify(result)


@app_file1.route("/parties", methods=['POST'])
def add_party():
    schema = PartySchema(only=("id", "name", "votes"))
    party = schema.load(request.get_json())
    party.save()
    resp = schema.dump(party)
    return resp, 201


@app_file1.route("/parties/<id>", methods=['PUT'])
def edit_party(id):
    schema = PartySchema(only=("id", "name", "votes"))
    party = Party.get_by_id(id)
    party_json = request.get_json()
    if party:
        party.name = party_json['name'] if 'name' in party_json else party.name
        party.votes = party_json['votes'] if 'votes' in party_json else party.votes
    else:
        party = schema.load(party_json)
    party.save()
    resp = schema.dump(party)
    return resp, 201


@app_file1.route("/parties/<id>", methods=['DELETE'])
def delete_party(id):
    party = Party.get_by_id(id)
    if party:
        party.delete()
    return '', 204


@app_file1.route("/seats", methods=['GET'])
def get_seats():
    parties = Party.get_all()
    try:
        if len(parties) == 0:
            raise ValueError('No parties')
    except ValueError as e:
        return 'No parties', 500
    else:
        schema = PartySchema(many=True)
        seat_count = int(request.args.get('seat_count'))
        for i in range(seat_count):
            quot_list = list(map(lambda party: party.calculate_dhont_quot(), parties))
            max_value = max(quot_list)
            max_index = quot_list.index(max_value)
            parties[max_index].seats += 1
        result = schema.dump(parties)
        history = History(seat_count=seat_count, result=result)
        history.save()
        return jsonify(result)


@app_file1.route("/history", methods=['GET'])
def get_history():
    history = History.get_all()
    schema = HistorySchema(many=True)
    result = schema.dump(history)
    return jsonify(result)


@app_file1.route("/history/<id>", methods=['DELETE'])
def delete_history(id):
    history = History.get_by_id(id)
    if history:
        history.delete()
    return '', 204

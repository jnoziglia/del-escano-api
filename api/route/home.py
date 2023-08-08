from flask import jsonify, request, Blueprint
from api.model.party import Party
from api.schema.party import PartySchema
from app import app, init_parties


@app.route("/parties", methods=['GET'])
def get_parties():
    schema = PartySchema(many=True)
    parties = schema.dump(init_parties)
    return jsonify(parties)


@app.route("/parties", methods=['POST'])
def add_party():
    party = PartySchema().load(request.get_json())
    init_parties.append(party)
    return '', 204

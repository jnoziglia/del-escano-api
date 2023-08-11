from flask import jsonify, request, Blueprint
from api.schema.party import PartySchema
from api.model.party import Party

party_bp = Blueprint('party_bp', __name__)
party_fields = ('id', 'name', 'votes')
party_schema = PartySchema(only=party_fields)
parties_schema = PartySchema(many=True, only=party_fields)


@party_bp.route("/parties", methods=['GET'])
def get_parties():
    parties = Party.get_all()
    result = parties_schema.dump(parties)
    return jsonify(result)


@party_bp.route("/parties/<id>", methods=['GET'])
def get_party(id):
    party = Party.get_by_id(id)
    result = party_schema.dump(party)
    return jsonify(result)


@party_bp.route("/parties", methods=['POST'])
def add_party():
    party = party_schema.load(request.get_json())
    party.save()
    resp = party_schema.dump(party)
    return resp, 201


@party_bp.route("/parties/<id>", methods=['PUT'])
def edit_party(id):
    party = Party.get_by_id(id)
    party_json = request.get_json()
    party.name = party_json['name'] if 'name' in party_json else party.name
    party.votes = party_json['votes'] if 'votes' in party_json else party.votes
    party.save()
    resp = party_schema.dump(party)
    return resp, 201


@party_bp.route("/parties/<id>", methods=['DELETE'])
def delete_party(id):
    party = Party.get_by_id(id)
    if party:
        party.delete()
    return '', 204


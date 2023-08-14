from flask import request, Blueprint
from api.schema.party import PartySchema
from api.model.party import Party
from auth_middleware import token_required
from api.common.error_handling import *

party_bp = Blueprint('party_bp', __name__)
party_fields = ('id', 'name', 'votes')
party_schema = PartySchema(only=party_fields)
parties_schema = PartySchema(many=True, only=party_fields)


@party_bp.route("/parties", methods=['GET'])
@token_required
def get_parties(current_user):
    parties = Party.get_all()
    result = parties_schema.dump(parties)
    return result


@party_bp.route("/parties/<id>", methods=['GET'])
@token_required
def get_party(current_user, id):
    party = Party.get_by_id(id)
    result = party_schema.dump(party)
    return result


@party_bp.route("/parties", methods=['POST'])
@token_required
def add_party(current_user):
    party = party_schema.load(request.get_json())
    if party.already_exists():
        raise ObjectAlreadyExists('Party already exists')
    party.save()
    resp = party_schema.dump(party)
    return resp, 201


@party_bp.route("/parties/<id>", methods=['PUT'])
@token_required
def edit_party(current_user, id):
    party = Party.get_by_id(id)
    party_json = request.get_json()
    party.name = party_json['name'] if 'name' in party_json else party.name
    party.votes = party_json['votes'] if 'votes' in party_json else party.votes
    party.save()
    resp = party_schema.dump(party)
    return resp, 201


@party_bp.route("/parties/<id>", methods=['DELETE'])
@token_required
def delete_party(current_user, id):
    party = Party.get_by_id(id)
    if party:
        party.delete()
    return '', 204


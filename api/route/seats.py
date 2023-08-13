from flask import jsonify, request, Blueprint
from api.schema.party import PartySchema
from api.model.party import Party
from api.model.history import History
from api.common.error_handling import *

seats_bp = Blueprint('seats_bp', __name__)
party_fields = ('name', 'votes', 'seats')
parties_schema = PartySchema(many=True, only=party_fields)


@seats_bp.route("/seats", methods=['GET'])
def get_seats():
    try:
        seat_count = int(request.args.get('seat_count'))
    except TypeError:
        raise BadRequest('Missing or invalid seat_count query parameter')
    parties = Party.get_all()
    if len(parties) == 0:
        raise ObjectNotFound('There are no parties to calculate seats')
    for i in range(seat_count):
        quot_list = list(map(lambda party: party.calculate_dhont_quot(), parties))
        max_value = max(quot_list)
        max_index = quot_list.index(max_value)
        parties[max_index].seats += 1
    result = parties_schema.dump(parties)
    history = History(seat_count=seat_count, result=result)
    history.save()
    return result

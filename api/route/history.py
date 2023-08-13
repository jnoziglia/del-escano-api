from flask import Blueprint
from api.schema.history import HistorySchema
from api.model.history import History
from auth_middleware import token_required

history_bp = Blueprint('history_bp', __name__)
history_schema = HistorySchema(many=True)


@history_bp.route("/history", methods=['GET'])
@token_required
def get_history(current_user):
    history = History.get_all()
    result = history_schema.dump(history)
    return result

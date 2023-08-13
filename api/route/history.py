from flask import jsonify, Blueprint
from api.schema.history import HistorySchema
from api.model.history import History

history_bp = Blueprint('history_bp', __name__)
history_schema = HistorySchema(many=True)


@history_bp.route("/history", methods=['GET'])
def get_history():
    history = History.get_all()
    result = history_schema.dump(history)
    return result

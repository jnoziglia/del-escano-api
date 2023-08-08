from flask import Flask, jsonify, request

from api.model.party import Party
from api.schema.party import PartySchema

app = Flask(__name__)

init_parties = [
    Party('Fdt', 0),
    Party('Pro', 0),
    Party('Lla', 0)
]


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

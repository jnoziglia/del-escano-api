from flask import Flask, jsonify, request

app = Flask(__name__)

parties = [
    {'name': 'party1', 'votes': 0}
]


@app.route("/parties", methods=['GET'])
def get_parties():
    return jsonify(parties)


@app.route("/parties", methods=['POST'])
def add_party():
    party = request.get_json()
    parties.append(party)
    return '', 204

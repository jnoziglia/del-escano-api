from flask import Flask, jsonify, request

from api.schema.party import PartySchema
from api.route.home import app_file1

app = Flask(__name__)
app.register_blueprint(app_file1)

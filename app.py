import os
from flask import Flask, jsonify
from api.ext import ma, migrate

from api.db import db


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404


app = Flask(__name__)

with app.app_context():
    app.config.from_object(os.getenv('APP_SETTINGS_MODULE'))
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

from api.route.home import app_file1

app.register_blueprint(app_file1)

# register_error_handlers(app)

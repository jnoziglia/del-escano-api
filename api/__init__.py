import os
from flask import Flask, jsonify
from api.ext import ma, migrate
from api.route.home import app_file1
from api.db import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS_MODULE'))

    if test_config is None:
        db.init_app(app)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(app_file1)

    # register_error_handlers(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


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

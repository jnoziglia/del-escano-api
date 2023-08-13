import os
from flask import Flask, jsonify
from api.ext import ma, migrate
from api.route.party import party_bp
from api.route.history import history_bp
from api.route.seats import seats_bp
from api.db import db
from api.common.error_handling import ObjectNotFound, AppErrorBaseClass


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    if test_config is None:
        db.init_app(app)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(party_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(seats_bp)

    register_error_handlers(app)

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

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404

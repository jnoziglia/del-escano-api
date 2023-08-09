import os
from flask import Flask
from api.ext import ma, migrate

from api.db import db

app = Flask(__name__)

with app.app_context():
    app.config.from_object(os.getenv('APP_SETTINGS_MODULE'))
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

from api.route.home import app_file1
app.register_blueprint(app_file1)

from flask import request, Blueprint, current_app
from api.schema.user import UserSchema
from api.model.user import User
import jwt
from datetime import datetime, timedelta

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()


@user_bp.route("/users/login", methods=['POST'])
def login():
    user_json = request.get_json()
    user = User.login(user_json['email'], user_json['password'])
    if user:
        try:
            # token should expire after 24 hrs
            token = jwt.encode(
                {"user_id": user.id},
                current_app.config["SECRET_KEY"],
                algorithm="HS256"
            )
            return {
                "token": token,
                "message": "Successfully fetched auth token"
            }
        except Exception as e:
            return {
                "error": "Something went wrong",
                "message": str(e)
            }, 500
    else:
        return 'User not found', 404


@user_bp.route("/users", methods=['POST'])
def add_user():
    user = user_schema.load(request.get_json())
    if user.create(user):
        resp = user_schema.dump(user)
        return resp, 201
    else:
        return 'User already exists', 409

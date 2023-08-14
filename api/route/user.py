from flask import request, Blueprint, current_app
from api.schema.user import UserSchema
from api.model.user import User
import jwt
from api.common.error_handling import ObjectNotFound, ObjectAlreadyExists, BadRequest
from marshmallow import ValidationError

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()


@user_bp.route("/users/login", methods=['POST'])
def login():
    user_json = request.get_json()
    try:
        user_schema.load(user_json)
    except ValidationError as e:
        raise BadRequest('Invalid data to login')
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
        raise ObjectNotFound('User not found')


@user_bp.route("/users", methods=['POST'])
def add_user():
    try:
        user = user_schema.load(request.get_json())
    except ValidationError as e:
        raise BadRequest('Invalid data to create a user')
    if user.create(user):
        return {'message': 'User created successfully. '
                           'Use your email and password at /users/login to login to the API'}, 201
    else:
        raise ObjectAlreadyExists('User already exists')

from flask import request, Blueprint
from api.schema.user import UserSchema
from api.model.user import User

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()


@user_bp.route("/users/login", methods=['GET'])
def login():
    user_json = request.get_json()
    user = User.login(user_json['email'], user_json['password'])
    if user:
        return '', 200
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

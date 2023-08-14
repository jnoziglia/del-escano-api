from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from api.model.user import User
from api.common.error_handling import Unauthorized


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            raise Unauthorized("Authentication Token is missing")
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.get_by_id(data["user_id"])
            if current_user is None:
                raise Unauthorized("Invalid Authentication token")
        except Exception as e:
            return {
                "message": "Something went wrong",
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated

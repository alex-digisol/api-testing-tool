import jwt
import os
from functools import wraps
from flask import jsonify, request, g

from app.auth.user_controller import UserController


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_cookie = request.cookies.get("auth")
        if not auth_cookie:
            return jsonify({}), 401

        try:
            result = jwt.decode(auth_cookie, os.getenv("SECRET_KEY"), algorithms="HS256")
            user_id = result["sub"]
            # Get user
            user = UserController.get_by_id(user_id)
            # TODO: user not active -> 401
            if not user:
                return jsonify({}), 401
            
            g.user = user

        except jwt.ExpiredSignatureError:
            return jsonify({}), 401

        return func(*args, **kwargs)

    return decorated_function
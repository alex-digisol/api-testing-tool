"""
Based on [Create a Flask Application With Google Login](https://realpython.com/flask-google-login/#creating-a-google-client) article
"""
import os
import requests
import json
import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app, jsonify, redirect, request, make_response, g
from app.middlewares.auth import login_required
from . import auth, GOOGLE_DISCOVERY_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from .user_controller import UserController


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@auth.route("/google/login", methods=["GET"])
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = current_app.config["google_client"].prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return jsonify({"link": request_uri})


@auth.route("/google/login/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    client = current_app.config["google_client"]
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        userinfo = userinfo_response.json()
        users_email = userinfo["email"]
        picture = userinfo["picture"]
        users_name = userinfo["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    user = UserController.get(users_email)
    if not user:
        user = UserController.create(users_name, users_email, picture, "google")

    t_now = datetime.now(tz=timezone.utc)
    t_exp = t_now + timedelta(days=1)
    # Create jwt tokens
    token = jwt.encode(
        payload={
            "sub": user["id"],
            "role": "user",  # TODO: Get user role from db
            "iss": "ApiTestingTool",
            "iat": t_now,
            "exp": t_exp
        },
        key=os.getenv("SECRET_KEY")
    )
    response = make_response(redirect('http://127.0.0.1:4200'))
    # TODO: cookie exp
    response.set_cookie("auth", token, domain="127.0.0.1", httponly=True, secure=True)
    return response


@auth.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect('http://127.0.0.1:4200'))
    response.set_cookie("auth", "", expires=0, domain="127.0.0.1", httponly=True, secure=True)
    return response


@auth.route("/profile", methods=["GET"])
@login_required
def profile():
    return jsonify(g.user), 200

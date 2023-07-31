"""
Based on [Create a Flask Application With Google Login](https://realpython.com/flask-google-login/#creating-a-google-client) article
"""
import os
import requests
import json
import jwt
from . import auth, GOOGLE_DISCOVERY_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from flask import current_app, jsonify, redirect, request, url_for, make_response, render_template
from .user import User

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@auth.route("/google/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = current_app.config["client"].prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return jsonify({"link": request_uri})


@auth.route("/google/login/callback")
def callback():
    code = request.args.get("code")
    client = current_app.config["client"]
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

    # Parse the tokens!
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

    # Doesn't exist? Add it to the database.
    if not User.get(users_email):
        User.create(users_name, users_email, picture)

    # Begin user session by logging the user in
    # login_user(user)

    # Create jwt tokens
    token = jwt.encode(
        payload={
            "email": users_email,
            "role": "user"
        },
        key=os.getenv("SECRET_KEY")
    )
    cookie_name = 'your_cookie_name'
    cookie_value = 'your_cookie_value'
    response = make_response(redirect('http://localhost:4200', code=302))  # Replace with your Angular frontend URL
    response.set_cookie(cookie_name, cookie_value)  # secure - cookie available only via https

    return response


@auth.route("/user/logout")
def logout():
    return redirect(url_for("main.home"))

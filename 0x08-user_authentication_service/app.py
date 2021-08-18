#!/usr/bin/env python3
"""Basic Flask App
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def greeting() -> str:
    """ GET /
    Return:
        - a greeting
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """POST /users
    JSON body:
        - email
        - password
    Return:
        - JSON payload
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        user = AUTH.register_user(email, pwd)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Creates a new session for the user and creates a session id cookie
    JSON body:
        - email
        - password
    Return:
        - JSON payload
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    if AUTH.valid_login(email, pwd):
        s_id = AUTH.create_session(email)
        res = make_response({"email": email, "message": "logged in"})
        res.set_cookie("session_id", value=s_id, domain="0.0.0.0",
                       secure=False)
        return res
    else:
        abort(401)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """GET /profile
    Finds the user of the corresponding session_id
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """DELETE /sessions
    Destroys a session and redirects the user to GET /
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """POST /reset_password
    Generates a reset token
    JSON body:
        - email: user's email
    Returns:
        - JSON payload
    """
    try:
        email = request.form.get("email")
        r_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": r_token}), 200
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """PUT /reset_password
    Updates a user's password
    JSON body:
        - email: user's email
        - reset_token: token generated to make new pwd
        - new_password: user's new password
    Returns:
        - JSON payload
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

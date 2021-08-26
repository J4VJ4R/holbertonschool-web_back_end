#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config app class
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as) -> Dict:
    """Gets a user from request
    """
    if login_as and int(login_as) in users:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """Excecuted before every request
    """
    u_id = request.args.get("login_as")
    if u_id:
        user = get_user(u_id)
        g.user = user
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """Select a language translation to use in every request
    """
    locale = request.args.get("locale")
    usr_id = request.args.get("login_as")
    header_locale = request.headers.get("locale")
    if locale:
        return locale
    if usr_id:
        user = get_user(usr_id)
        if user.get("locale") in Config.LANGUAGES:
            return user.get("locale")
    if header_locale:
        return header_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def welcome():
    """GET /
    returns render of 6-index.html"""
    return render_template("6-index.html", user=g.user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

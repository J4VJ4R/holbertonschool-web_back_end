#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config app class
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = 'UTC'


@app.route("/", methods=["GET"])
def welcome():
    """GET /
    returns render of 1-index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

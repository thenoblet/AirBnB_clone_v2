#!/usr/bin/python3
"""
This module sets up a basic Flask web application with two routes.

Routes:
    /       : Returns a welcome message "Hello HBNB!".
    /hbnb   : Returns a message "HBNB".

Imports:
    Flask from the flask package.

Functions:
    home(): Returns a welcome message "Hello HBNB!".
    holberton(): Returns a message "HBNB".
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    Handles requests to the root URL ('/') and returns
    welcome message.

    Returns:
        str: A welcome message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def holberton():
    """
    Handles requests to the '/hbnb' URL and returns a simple message.

    Returns:
        str: A message "HBNB".
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

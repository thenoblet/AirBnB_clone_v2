#!/usr/bin/python3
"""
flask_app.py

This module sets up a basic Flask web application that responds with "Hello HBNB" when accessed.

Imports:
    Flask from the flask package.

Functions:
    home(): Returns a welcome message "Hello HBNB".
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """
    The home function handles requests to the root URL ('/') and returns a simple greeting.

    Returns:
        str: A welcome message "Hello HBNB".
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

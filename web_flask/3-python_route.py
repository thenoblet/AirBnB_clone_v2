#!/usr/bin/python3
"""
This module sets up a basic Flask web application with four routes.

Routes:
    /               : Returns a welcome message "Hello HBNB!".
    /hbnb           : Returns a message "HBNB".
    /c/<text>       : Returns a message "C <text>" where <text>
                      is a dynamic part of the URL.
    /python/        : Returns a default message "Python is cool".
    /python/<text>  : Returns a message "Python <text>" where <text>
                      is a dynamic part of the URL.

Imports:
    Flask from the flask package.

Functions:
    home(): Returns a welcome message "Hello HBNB!".
    holberton(): Returns a message "HBNB".
    is_fun(text): Returns a message "C <text>" with underscores in
    <text> replaced by spaces.
    python_text(text): Returns a message "Python <text>" with
    underscores in <text> replaced by spaces. Defaults to "is cool".
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Handles requests to the root URL ('/') and
    returns a welcome message.

    Returns:
        str: A welcome message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """
    Handles requests to the '/hbnb' URL and returns a simple message.

    Returns:
        str: A message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def is_fun(text):
    """
    Handles requests to the '/c/<text>' URL and
    returns a message with the text.

    Parameters:
        text (str): The dynamic part of the URL.

    Returns:
        str: A message "C <text>" with underscores in
            <text> replaced by spaces.
    """
    clean_text = text.replace('_', ' ')
    return f"C {clean_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Handles requests to the '/python/' and '/python/<text>'
    URLs and returns a message with the text.

    Parameters:
        text (str, optional): The dynamic part of the URL.
        Defaults to "is cool".

    Returns:
        str: A message "Python <text>" with underscores
        in <text> replaced by spaces.
    """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

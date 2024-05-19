#!/usr/bin/python3
"""
This module sets up a basic Flask web application with three routes.

Routes:
    /        : Returns a welcome message "Hello HBNB!".
    /hbnb    : Returns a message "HBNB".
    /c/<text>: Returns a message "C <text>" where
               <text> is a dynamic part of the URL.

Imports:
    Flask from the flask package.

Functions:
    home(): Returns a welcome message "Hello HBNB!".
    holberton(): Returns a message "HBNB".
    c_is_fun(text): Returns a message "C <text>" with
    underscores in <text> replaced by spaces.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def home():
    """
    Handles requests to the root URL ('/') and returns a welcome message.

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


# @app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    Handles requests to the '/c/<text>' URL and returns
    a message with the text.

    Parameters:
        text (str): The dynamic part of the URL.

    Returns:
        str: A message "C <text>" with underscores in <text>
        replaced by spaces.
    """
    clean_text = text.replace('_', ' ')
    return f"C {clean_text}"


app.add_url_rule(
        "/c/<text>",
        endpoint="c_is_fun",
        view_func=c_is_fun,
        strict_slashes=False
)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

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
    /number/<int:n> : Returns a message "<n> is a number"
                      where <n> is an integer.
    /number_template/<int:n>: Renders an HTML template and
                              displays the number <n>.

Imports:
    Flask from the flask package.

Functions:
    home(): Returns a welcome message "Hello HBNB!".
    holberton(): Returns a message "HBNB".
    is_fun(text): Returns a message "C <text>" with underscores in
    <text> replaced by spaces.
    python_text(text): Returns a message "Python <text>" with
    underscores in <text> replaced by spaces. Defaults to "is cool".
    is_number(n): Returns a message "<n> is a number".
    num_template_route(n): Renders an HTML template and
                           displays the number <n>.
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Handles requests to the '/number/<n>' URL and returns
    a message indicating that <n> is a number.

    Parameters:
        n (int): The dynamic part of the URL, which is
                 expected to be an integer.

    Returns:
        str: A message "<n> is a number".
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template_route(n):
    """
    Handles requests to the '/number_template/<n>' URL and
    renders an HTML template to display the number.

    Parameters:
        n (int): The dynamic part of the URL, which is
                 expected to be an integer.

    Returns:
        str: Rendered HTML template displaying the number <n>.
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

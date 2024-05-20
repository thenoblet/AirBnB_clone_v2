#!/usr/bin/python3
"""
Starts a Flask web application.

This module sets up a basic Flask web application with
the following route:
    /states_list: Renders an HTML template displaying a list
                  of all State objects.

Imports:
    Flask from the flask package.
    render_template from the flask package.
    storage from the models package.
    State from the models.state module.

Functions:
    teardown_session(exception): Removes the current SQLAlchemy Session
    after each request.
    state_list(): Retrieves all State objects and renders them in
    an HTML template.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """
    Remove the current SQLAlchemy Session after each request.

    This function is registered to be called after each request to ensure
    that the SQLAlchemy Session is properly closed,
    preventing any potential resource leaks.

    Parameters:
        exception (Exception): The exception that was raised
        during the request (if any).
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    Handles requests to the '/states_list' URL and renders a
    list of State objects.

    This function retrieves all State objects from the storage and
    passes them to the '7-states_list.html' template for rendering.

    Returns:
        str: Rendered HTML template displaying a list of all State objects.
    """
    states = storage.all(State).values()

    return render_template("7-states_list.html", all_states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

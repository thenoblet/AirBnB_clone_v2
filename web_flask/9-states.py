#!/usr/bin/python3
"""
Starts a Flask web application.

This module sets up a Flask web application with the
following routes:
    /states        : Renders an HTML template displaying
                     all State objects.
    /states/<id>   : Renders an HTML template displaying a
                     specific State object by ID.

Imports:
    Flask from the flask package.
    render_template from the flask package.
    storage from the models package.
    State from the models.state module.

Functions:
    get_states(): Retrieves all State objects and renders them
                  in an HTML template.
    states_id(id): Retrieves a State object by ID and renders
                  it in an HTML template.
    teardown_session(exception): Removes the current SQLAlchemy
                 Session after each request.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def get_states():
    """
    Handles requests to the '/states' URL and renders
    a list of all State objects.

    This function retrieves all State objects from the storage and
    passes them to the '9-states.html' template for rendering.

    Returns:
        str: Rendered HTML template displaying a list of all State objects.
    """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, status="all")


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Handles requests to the '/states/<id>' URL and renders a
    specific State object by ID.

    This function retrieves a State object by its ID from the storage
    and passes it to the '9-states.html' template for rendering.
    If no State object with the given ID is found, it renders the template
    indicating that no state was found.

    Parameters:
        id (str): The ID of the State object to be retrieved.

    Returns:
        str: Rendered HTML template displaying the specific State object
        or a message indicating no state was found.
    """
    states = storage.all(State).values()
    state = next((s for s in states if s.id == id), None)

    if state:
        return render_template('9-states.html', states=state, status='id')

    return render_template('9-states.html', status="none")


@app.teardown_appcontext
def teardown_session(exception):
    """
    Remove the current SQLAlchemy Session after each request.

    This function is registered to be called after each request
    to ensure that the
    SQLAlchemy Session is properly closed, preventing any
    potential resource leaks.

    Parameters:
        exception (Exception): The exception that was raised
        during the request (if any).
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

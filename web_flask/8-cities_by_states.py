#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cites_by_states():
    """
    Handles requests to the '/cities_by_states' URL and renders a
    list of State objects.

    This function retrieves all State objects from the storage and
    passes them to the '7-states_list.html' template for rendering.

    Returns:
        str: Rendered HTML template displaying a list of all State objects.
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", all_states=states)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

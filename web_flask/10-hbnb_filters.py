#!/usr/bin/python3
"""
Starts a Flask web application for managing State and Amenity objects.

This module sets up a Flask web application with the following routes:
    /hbnb_filters: Displays the main HBnB filters HTML page.

Imports:
    storage from the models package.
    Flask and render_template from the flask package.

Functions:
    hbnb_filters(): Displays the main HBnB filters HTML page.
    teardown_session(exception): Removes the current SQLAlchemy
    session after each request.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page.

    Retrieves all State and Amenity objects from the database
    using the storage object and passes them to the
    '10-hbnb_filters.html' template for rendering.

    Returns:
        str: Rendered HTML template '10-hbnb_filters.html'
        displaying states and amenities.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template(
            "10-hbnb_filters.html",
            states=states,
            amenities=amenities
    )


@app.teardown_appcontext
def teardown_session(exception):
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

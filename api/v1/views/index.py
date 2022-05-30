#!/usr/bin/python3
"""Module with a Blueprint object for the API"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Route to return the number of each object"""
    number_of_objects = {
        "amenities": len(storage.all("Amenity")),
        "cities": len(storage.all("City")),
        "places": len(storage.all("Place")),
        "reviews": len(storage.all("Review")),
        "states": len(storage.all("State")),
        "users": len(storage.all("User"))
    }
    return jsonify(number_of_objects)

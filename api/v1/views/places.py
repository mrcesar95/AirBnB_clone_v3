#!/usr/bin/python3
"""
Create a new view for Place objects
 that handles all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models import storage
from flasgger.utils import swag_from

@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_all_places(city_id=None):
    """
    Returns the all stored places of a City
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places_in_city = city.places
    return jsonify([Place.to_dict(place) for place in places_in_city]), 200


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place_by_id(place_id=None):
    """
    Returns a specific Place given an object id
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(Place.to_dict(place)), 200


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id=None):
    """
    Deletes a Place given an id and returns an empty JSON
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id=None):
    """
    Creates a Place object
    """
    jrequest = request.get_json()
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if jrequest is None:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'user_id' not in jrequest:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)

    user = storage.get(User,  jrequest.get('user_id'))
    if not user:
        abort(404)
    if 'name' not in jrequest:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    place = Place(**jrequest)
    place.city_id = city_id
    place.save()
    return make_response(jsonify(Place.to_dict(place)), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id=None):
    """"
    Updates a Place object
    """
    jrequest = request.get_json()
    if jrequest is None:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for key, value in jrequest.items():
        if key not in ignore_keys:
            setattr(place, key, value)
    place.save()
    return make_response(jsonify(Place.to_dict(place)), 200)

@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/place/post_search.yml', methods=['POST'])
def places_search():
    """
    Retrieves all Place objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        states = data.get('states', None)
        cities = data.get('cities', None)
        amenities = data.get('amenities', None)

    if not data or not len(data) or (
            not states and
            not cities and
            not amenities):
        places = storage.all(Place).values()
        list_places = []
        for place in places:
            list_places.append(place.to_dict())
        return jsonify(list_places)

    list_places = []
    if states:
        states_obj = [storage.get(State, s_id) for s_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    if city:
                        for place in city.places:
                            list_places.append(place)

    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for place in city.places:
                    if place not in list_places:
                        list_places.append(place)

    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [place for place in list_places
                       if all([am in place.amenities
                               for am in amenities_obj])]

    places = []
    for p in list_places:
        d = p.to_dict()
        d.pop('amenities', None)
        places.append(d)

    return jsonify(places)
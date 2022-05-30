#!/usr/bin/python3
"""State module api"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_all_states():
    """
        Returns all States
    """
    return jsonify([state.to_dict() for state in
                    storage.all(State).values()]), 200


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_states_by_id(state_id=None):
    """
        return a states by id or error if not found
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id=None):
    """
        Deletes a state with id and returns an empty JSON
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def create_state():
    """
        Stores and returns a new state
    """
    state_in_json = request.get_json(silent=True)
    if state_in_json is None:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in state_in_json:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**state_in_json)
    state.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def update_state(state_id=None):
    """
        Return the information of a given state
    """
    keys = ['id', 'created_at', 'updated_at']
    req = request.get_json(silent=True)

    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not req:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, val in req.items():
        if key not in keys:
            setattr(state, key, val)
    state.save()
    return make_response(jsonify(state.to_dict()), 200)

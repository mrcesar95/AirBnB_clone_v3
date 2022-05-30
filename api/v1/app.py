#!/usr/bin/python3
"""initializes a flask web application"""
from flask import Flask, jsonify, make_response
from models import storage
from os import getenv
from api.v1.views.index import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """error handler for 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.teardown_appcontext
def close(execute):
    """closes the session"""
    storage.close()


if __name__ == '__main__':
    env_host = getenv('HBNB_API_HOST', default='0.0.0.0')
    env_port = getenv('HBNB_API_PORT', default='5000')
    app.run(host=env_host, port=env_port, threaded=True)

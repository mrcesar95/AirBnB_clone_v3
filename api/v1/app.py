#!/usr/bin/python3
"""initializes a flask web application"""
from flask import Flask, jsonify, make_response
from models import storage
from os import getenv
from api.v1.views.index import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
#CORS(app, resources={r"/api/v1/*": {"origins": ["0.0.0.0"]}})
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """error handler for 404"""
    return make_response(jsonify({'error': 'Not found'}), 404) 


@app.teardown_appcontext
def close(execute):
    """closes the session"""
    storage.close()


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    if host is None:
        host = '0.0.0.0'
    port = getenv('HBNB_API_PORT')
    if port is None:
        port = 5001
    app.run(host=host, port=port, threaded=True)

#!/usr/bin/env python3
from flask import Blueprint, Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from flaskapp.custom_omx import CustomOMX
from flaskapp.control_endpoint import ControlEndpoint
from flaskapp.playlist_endpoint import PlaylistEndpoint
from flaskapp.music_endpoint import MusicEndpoint


def create_app():
    app = Flask(__name__)
    app_blueprint = Blueprint('v1', __name__)
    app_api = swagger.docs(Api(app_blueprint), apiVersion='0.1')
    app_api = Api(app_blueprint)

    app.config['omx'] = CustomOMX()

    app_api.add_resource(ControlEndpoint, '/control')
    app_api.add_resource(MusicEndpoint, '/music')
    app_api.add_resource(PlaylistEndpoint, '/playlist')

    app.register_blueprint(app_blueprint)
    return app


app = create_app()
app.run(host='0.0.0.0')

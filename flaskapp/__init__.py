from flask import Blueprint, Flask
from flask_restful import Api

from flaskapp.custom_vlc import CustomVLC
from flaskapp.control_endpoint import ControlEndpoint
from flaskapp.youtube_endpoint import YoutubeEndpoint


def create_app():
    app = Flask(__name__)
    app_blueprint = Blueprint('v1', __name__)
    app_api = Api(app_blueprint)

    app.config['vlc'] = CustomVLC()

    app_api.add_resource(ControlEndpoint, '/control')
    app_api.add_resource(YoutubeEndpoint, '/youtube')

    app.register_blueprint(app_blueprint)
    return app


app = create_app()
app.run()

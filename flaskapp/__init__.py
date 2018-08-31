from flask import Blueprint, Flask
from flask_restful import Api

from flaskapp.custom_vlc import CustomVLC
from flaskapp.state_endpoint import StateEndpoint


def create_app():
    app = Flask(__name__)
    app_blueprint = Blueprint('v1', __name__)
    app_api = Api(app_blueprint)

    app.config['vlc'] = CustomVLC()

    app_api.add_resource(StateEndpoint, '/state')

    app.register_blueprint(app_blueprint)
    return app


app = create_app()
app.run()

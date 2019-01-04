from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restful import Api as FlaskApi
from flask_restful_swagger_2 import Api as SwaggerApi
from flask_swagger_ui import get_swaggerui_blueprint

from flaskapp.player import Player
from flaskapp.endpoints.control_endpoint import ControlEndpoint
from flaskapp.endpoints.gui_endpoint import GuiEndpoint
from flaskapp.endpoints.add_endpoint import AddEndpoint
from flaskapp.endpoints.music_endpoint import MusicEndpoint
from flaskapp.endpoints.playlist_endpoint import PlaylistEndpoint


def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app)

    flask_app.config['player'] = Player()

    # Blueprint for REST API
    app_blueprint = Blueprint('rest', __name__)
    app_api = SwaggerApi(app_blueprint, api_version='0.1', title='Pilody', description='OMX media player REST API',
                  contact='zessirb@gmail.com', api_spec_url='/swagger')
    app_api.add_resource(ControlEndpoint, '/control')
    app_api.add_resource(MusicEndpoint, '/music')
    app_api.add_resource(PlaylistEndpoint, '/playlist')
    flask_app.register_blueprint(app_blueprint)

    # Blueprint for swagger
    swagger_blueprint = get_swaggerui_blueprint('/docs', 'http://127.0.0.1:5000/swagger.json',
                                                config={'app_name': 'Pilody'})
    flask_app.register_blueprint(swagger_blueprint, url_prefix='/docs')

    # Blueprint for GUI
    gui_blueprint = Blueprint('gui', __name__)
    gui_api = FlaskApi(gui_blueprint)
    gui_api.add_resource(GuiEndpoint, '/gui')
    gui_api.add_resource(AddEndpoint, '/add')
    flask_app.register_blueprint(gui_blueprint)

    return flask_app

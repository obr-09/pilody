from flask import current_app, request
from flask_restful import Resource


class ControlEndpoint(Resource):

    def get(self):
        return 'playing'

    def post(self):
        action = request.form['action']
        if action == 'play':
            current_app.config['vlc'].play()
        elif action == 'resume':
            current_app.config['vlc'].resume()
        elif action == 'pause':
            current_app.config['vlc'].pause()
        elif action == 'stop':
            current_app.config['vlc'].stop()
        else:
            pass
        return action if action else 'None'

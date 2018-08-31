from flask import current_app, request
from flask_restful import Resource


class ControlEndpoint(Resource):

    def get(self):
        if current_app.config['vlc'].player:
            if current_app.config['vlc'].player.is_playing:
                return 'playing'
            else:
                return 'paused'
        else:
            return 'stopped'

    def post(self):
        action = request.form['action']
        if action == 'play':
            current_app.config['vlc'].play()
        elif action == 'resume':
            current_app.config['vlc'].toggle_pause()
        elif action == 'pause':
            current_app.config['vlc'].toggle_pause()
        elif action == 'stop':
            current_app.config['vlc'].stop()
        elif action == 'previous':
            current_app.config['vlc'].previous()
        elif action == 'next':
            current_app.config['vlc'].next()
        else:
            pass
        return action if action else 'None'

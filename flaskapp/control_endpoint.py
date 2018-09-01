from flask import current_app, request
from flask_restful import Resource


class ControlEndpoint(Resource):

    def get(self):
        if current_app.config['vlc'].player:
            if current_app.config['vlc'].player.is_playing:
                return {'state': 'playing'}
            else:
                return {'state': 'paused'}
        else:
            return {'state': 'stopped'}

    def post(self):
        action = request.form['action']
        if action == 'play':
            current_app.config['omx'].play()
        elif action == 'resume':
            current_app.config['omx'].toggle_pause()
        elif action == 'pause':
            current_app.config['omx'].toggle_pause()
        elif action == 'stop':
            current_app.config['omx'].stop()
        elif action == 'previous':
            current_app.config['omx'].previous()
        elif action == 'next':
            current_app.config['omx'].next()
        else:
            return {'error': 'Unrecognized action.'}, 400
        return {'action': 'Action {} done.'.format(action)}

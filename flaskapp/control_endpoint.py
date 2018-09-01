from flask import current_app, request
from flask_restful import Resource


class ControlEndpoint(Resource):

    def get(self):
        pass

    def post(self):
        action = request.form['action']
        if action in ['play', 'resume', 'pause']:
            current_app.config['omx'].toggle_pause()
        elif action == 'stop':
            current_app.config['omx'].stop()
        elif action == 'previous':
            current_app.config['omx'].previous()
        elif action == 'next':
            current_app.config['omx'].next()
        else:
            return {'message': 'Unrecognized action.'}, 400
        return {'message': 'Action {} submitted'.format(action)}, 200

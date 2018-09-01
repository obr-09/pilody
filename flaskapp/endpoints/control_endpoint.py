from flask import current_app, request
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

from flaskapp.swagger_schema import MessageModel, MusicActionSchema


class ControlEndpoint(Resource):

    def get(self):
        pass

    @swagger.doc({
        'tags': ['music'],
        'description': 'Control the current music playing',
        'parameters': [
            {
                'name': 'action',
                'description': 'Name of the action to do',
                'schema': MusicActionSchema,
                'required': True,
                'in': 'body',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Action submitted',
                'schema': MessageModel,
                'examples': {
                    'application/json': {
                        'message': 'Action {} submitted'
                    }
                }
            }
        }
    })
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
            return MessageModel(message='Unrecognized action.'), 400
        return MessageModel(message='Action {} submitted'.format(action)), 200

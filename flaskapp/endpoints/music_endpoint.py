import json

from flask import current_app, request
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

from flaskapp.swagger_schema import MessageModel, YoutubeUrlSchema, MusicInfoSchema
from flaskapp.youtube_utility import YoutubeUtility


class MusicEndpoint(Resource):

    @swagger.doc({
        'tags': ['music'],
        'description': 'Getting informations about the current music',
        'parameters': [
        ],
        'responses': {
            '200': {
                'description': 'Music informations',
                'schema': MusicInfoSchema,
                'examples': {
                    'application/json': {
                        'url': 'URL of the music',
                        'title': 'Title fetched from music source',
                        'artist': 'Artist or author who submitted the music'
                    }
                }
            }
        }
    })
    def get(self):
        music = current_app.config['omx'].get_music()
        return json.dumps(music), 200

    @swagger.doc({
        'tags': ['music'],
        'description': 'Setting a new music',
        'parameters': [
            {
                'name': 'youtube_url',
                'description': 'URL to a youtube video',
                'schema': YoutubeUrlSchema,
                'required': True,
                'in': 'body',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Music changed',
                'schema': MessageModel,
                'examples': {
                    'application/json': {
                        'message': 'The music was submitted'
                    }
                }
            }
        }
    })
    def post(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = YoutubeUtility.get_youtube_video(youtube_url)
            if video_data:
                current_app.config['omx'].set_audio(video_data.audio_url, video_data.title, video_data.author)
                return MessageModel(message='The music was submitted'), 200
            else:
                return MessageModel(message='No music found from the Youtube url'), 400
        else:
            return MessageModel(message='You need to pass youtube_url as body parameter'), 400

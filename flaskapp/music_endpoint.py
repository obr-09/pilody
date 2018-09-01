from flask import current_app, request
from flask_restful import Resource
from flask_restful_swagger import swagger

from flaskapp.youtube_utility import YoutubeUtility


class MusicEndpoint(Resource):

    def get(self):
        return {'error': 'Not implemented'}, 501

    'Setting a new music'
    @swagger.operation(
        parameters=[
            {
                'name': 'youtube_url',
                'description': 'URL to a youtube video',
                'required': True,
                'allowMultiple': False,
                'paramType': 'body'
            }
        ],
        responseMessages=[
            {
                'code': 200,
                'message': 'The music was submitted'
            }
        ]
    )
    def post(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = YoutubeUtility.get_youtube_video(youtube_url)
            if video_data:
                current_app.config['omx'].set_audio(video_data.audio_url)
                current_app.config['omx'].play()
                return {'message': 'The music was submitted'}, 200
            else:
                return {'message': 'No music found from the Youtube url'}, 400
        else:
            return {'message': 'You need to pass youtube_url as body parameter'}, 400

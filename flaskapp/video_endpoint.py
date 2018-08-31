from flask import current_app, request
from flask_restful import Resource

from flaskapp.custom_vlc import CustomVLC


class VideoEndpoint(Resource):

    def get(self):
        return {'error': 'Not implemented'}, 501
        # return current_app.config['vlc'].get_music_info()

    def post(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = CustomVLC.get_youtube_video(youtube_url)
            current_app.config['vlc'].set_video(video_data)

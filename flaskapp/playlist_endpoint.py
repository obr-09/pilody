from flask import current_app, request
from flask_restful import Resource

from flaskapp.custom_vlc import CustomVLC
from flaskapp.youtube_utility import YoutubeUtility


class PlaylistEndpoint(Resource):

    def get(self):
        pass

    def post(self):
        pass

    def patch(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = YoutubeUtility.get_youtube_video(youtube_url)
            current_app.config['omx'].add_audio(video_data.audio_url)

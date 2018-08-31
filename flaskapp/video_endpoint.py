from flask import current_app, request
from flask_restful import Resource

from flaskapp.custom_vlc import CustomVLC


class VideoEndpoint(Resource):

    def get(self):
        return current_app.config['vlc'].get_music_info()
        # video = current_app.config['vlc'].video_data
        # video_info = {'url': video.url}
        # if video.title and video.description and video.author:
        #     video_info.title = video.title
        #     video_info.description = video.description
        #     video_info.author = video.author
        # return video_info

    def post(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = CustomVLC.get_youtube_video(youtube_url)
            current_app.config['vlc'].set_video(video_data)

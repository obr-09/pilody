from flask import current_app, request
from flask_restful import Resource


class YoutubeEndpoint(Resource):

    def get(self):
        video = current_app.config['vlc'].video
        return {
            'title': video.title,
            'description': video.description,
            'author': video.author
        }

    def post(self):
        url = request.form['url']
        if url:
            current_app.config['vlc'].set_youtube_video(url)

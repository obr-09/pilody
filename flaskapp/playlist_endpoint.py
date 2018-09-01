from random import shuffle

from flask import current_app, request
from flask_restful import Resource

from flaskapp.custom_vlc import CustomVLC
from flaskapp.youtube_utility import YoutubeUtility


class PlaylistEndpoint(Resource):

    def get(self):
        pass

    def post(self):
        playlist_url = request.form['playlist_url']
        if playlist_url:
            video_list = YoutubeUtility.get_youtube_playlist(playlist_url)
            if video_list:
                url_list = []
                for video in video_list:
                    url_list.append(video.audio_url)
                shuffle(url_list)
                current_app.config['omx'].set_playlist(url_list)
                return {'message': 'The playlist was submitted'}, 200
            else:
                return {'message': 'No music found at Youtube playlist url'}, 404
        else:
            return {'message': 'You need to pass playlist_url as body parameter'}, 400

    def patch(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = YoutubeUtility.get_youtube_video(youtube_url)
            if video_data:
                current_app.config['omx'].add_audio(video_data.audio_url)
                return {'message': 'The music was submitted to the playlist'}, 200
            else:
                return {'message': 'No music found from the Youtube url'}, 404
        else:
            return {'message': 'You need to pass youtube_url as body parameter'}, 400

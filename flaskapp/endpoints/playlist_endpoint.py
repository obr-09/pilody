from random import shuffle

from flask import current_app, request
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

from flaskapp.swagger_schema import MessageModel, PlaylistUrlSchema, YoutubeUrlSchema
from flaskapp.youtube_utility import YoutubeUtility


class PlaylistEndpoint(Resource):

    @swagger.doc({
        'tags': ['music'],
        'description': 'Get the list of musics playing or waiting to be played'
    })
    def get(self):
        playing_music = current_app.config['omx'].get_music()
        next_musics = current_app.config['omx'].get_next_musics()
        if playing_music:
            next_musics.insert(0, playing_music)
        return next_musics

    @swagger.doc({
        'tags': ['music'],
        'description': 'Setting a new playlist',
        'parameters': [
            {
                'name': 'playlist_url',
                'description': 'URL to a youtube playlist',
                'schema': PlaylistUrlSchema,
                'required': True,
                'in': 'body',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Playlist changed',
                'schema': MessageModel,
                'examples': {
                    'application/json': {
                        'message': 'The playlist was submitted'
                    }
                }
            }
        }
    })
    def post(self):
        playlist_url = request.form['playlist_url']
        if playlist_url:
            video_list = YoutubeUtility.get_youtube_playlist(playlist_url)
            if video_list:
                music_list = []
                for video in video_list:
                    if video.audio_url:
                        music_list.append({'url': video.audio_url, 'title': video.title, 'author': video.author})
                shuffle(music_list)
                current_app.config['omx'].set_playlist(music_list)
                return MessageModel(message='The playlist was submitted'), 200
            else:
                return MessageModel(message='No music found at Youtube playlist url'), 404
        else:
            return MessageModel(message='You need to pass playlist_url as body parameter'), 400

    @swagger.doc({
        'tags': ['music'],
        'description': 'Adding a new music to the playlist',
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
                'description': 'Music added to playlist',
                'schema': MessageModel,
                'examples': {
                    'application/json': {
                        'message': 'The music was submitted to the playlist'
                    }
                }
            }
        }
    })
    def patch(self):
        youtube_url = request.form['youtube_url']
        if youtube_url:
            video_data = YoutubeUtility.get_youtube_video(youtube_url)
            if video_data:
                current_app.config['omx'].add_music({'url': video_data.audio_url, 'title': video_data.title, 'author': video_data.author})
                return MessageModel(message='The music was submitted to the playlist'), 200
            else:
                return MessageModel(message='No music found from the Youtube url'), 404
        else:
            return MessageModel(message='You need to pass youtube_url as body parameter'), 400

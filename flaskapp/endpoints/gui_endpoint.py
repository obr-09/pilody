from flask import render_template, Response
from flask_restful import Resource


class GuiEndpoint(Resource):

    def get(self):
        return Response(render_template('player.html'), status=200, mimetype='text/html')

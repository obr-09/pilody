from flask import render_template, Response, request
from flask_restful import Resource


class GuiEndpoint(Resource):

    def get(self):
        return Response(render_template('player.html', base_url=request.base_url), status=200, mimetype='text/html')

from flask import render_template, Response, request
from flask_restful import Resource


class AddEndpoint(Resource):

    def get(self):
        return Response(render_template('add.html', base_url=request.base_url), status=200, mimetype='text/html')

import io

from flask import request, jsonify, send_file
from flask_classy import FlaskView

from app.exception.exception import GetFileError, PostFileError
from app.service.service import Service

from utils.response.response import Response


class Base(FlaskView):
    route_base = '/'

    def get(self, filename):
        try:
            image = Service.get(filename)
        except GetFileError:
            return Response.response_404()
        return send_file(io.BytesIO(image), attachment_filename=filename)

    def post(self):
        file = request.files['file']
        try:
            Service.post(file.filename, file.read())
        except PostFileError:
            return Response.response_503()
        return jsonify({'status': 'ok'})

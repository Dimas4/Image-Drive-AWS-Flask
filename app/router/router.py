from flask import request, jsonify, send_file
from flask_classy import FlaskView
from app.service.service import Service
import io

service = Service()


class Base(FlaskView):
    route_base = '/'

    def get(self, filename):
        image = service.get(filename)
        return send_file(io.BytesIO(image), attachment_filename=filename)

    def post(self):
        file = request.files['file']

        file.save(file.filename)
        with open(file.filename, 'rb') as f:
            data = f.read()
        service.post(file.filename, data)
        return jsonify({'status': 'ok'})

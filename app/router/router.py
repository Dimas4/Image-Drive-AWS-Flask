from flask_classy import FlaskView
from flask import request, jsonify
from PIL import Image
from app.service.service import Service
from io import BytesIO

import io


service = Service()


class Base(FlaskView):
    route_base = '/'

    def get(self, filename):
        image = service.get(filename)
        print(image)

    def post(self):
        file = request.files['file']
        service.post(file.name, file.read())
        return jsonify({'status': 'ok'})

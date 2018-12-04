import json

from utils.create_app.create import app


class Response:
    def response_400(self, error=None):
        if error:
            return app.make_response((json.dumps(error), 400))
        return app.make_response(('Bad request', 400))

    def response_404(self):
        return app.make_response(('Not found', 404))

    def response_503(self):
        return app.make_response(('Error', 503))

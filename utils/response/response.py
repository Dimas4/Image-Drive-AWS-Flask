import json

from utils.create_app.create import app


class Response:
    @staticmethod
    def response_400(error=None):
        if error:
            return app.make_response((json.dumps(error), 400))
        return app.make_response(('Bad request', 400))

    @staticmethod
    def response_404():
        return app.make_response(('Not found', 404))

    @staticmethod
    def response_503():
        return app.make_response(('Error', 503))

from flask import Flask

from config.get_config import get_config


def create():
    app = Flask(__name__)
    app.config['config'] = get_config()
    return app


app = create()

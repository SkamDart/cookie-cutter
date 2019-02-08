from project.config import settings

__version__ = '0.0.0'

__all__ = ['settings']


def create_app(env=None):
    from flask import (
        Flask,
        jsonify,
        request
    )

    app = Flask(__name__)
    configure_app(app, env)

    # app.register_blueprint(api_blueprint, url_prefix='url_prefix')
    @app.route('/')
    def alive():
        return jsonify('Alive')

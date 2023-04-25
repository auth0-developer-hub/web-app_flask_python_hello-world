import json

from flask import Flask, render_template

from config import config
from webapp.views import webapp_bp
from auth.views import auth_bp


def to_pretty_json(obj: dict) -> str:
    return json.dumps(obj, default=lambda o: o.__dict__, indent=4)


def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    """
    Configuration of the app
    """
    app = Flask(__name__)

    app.secret_key = config["WEBAPP"]["SECRET_KEY"]

    app.jinja_env.filters['to_pretty_json'] = to_pretty_json

    app.register_error_handler(404, page_not_found)

    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(webapp_bp, url_prefix='/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')

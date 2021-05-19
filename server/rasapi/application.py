"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='RAS_API'):
    app = Flask(app_name)
    app.config.from_object('rasapi.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from rasapi.api import api
    app.register_blueprint(api, url_prefix="/")

    from rasapi.commands import cmd
    app.register_blueprint(cmd)

    from rasapi.models import db
    db.init_app(app)

    return app
   
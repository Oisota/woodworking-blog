from dotenv import load_dotenv
load_dotenv()

from flask import Flask, g

from app.exts import register_extensions
from app.blueprints import register_blueprints
from app.cli import register_cli

def create_app():
    """App Factory"""
    app = Flask(__name__)
    app.config.from_prefixed_env()

    register_extensions(app)
    register_cli(app)
    register_blueprints(app)

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return app
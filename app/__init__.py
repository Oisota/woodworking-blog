from dotenv import load_dotenv
load_dotenv()

from flask import Flask

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

    return app
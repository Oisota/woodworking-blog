
from .login import login_manager

def register_extensions(app):
    login_manager.init_app(app)
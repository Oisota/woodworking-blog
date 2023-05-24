from .auth import bp as auth_bp
from .core import bp as core_bp
from .blog import bp as blog_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(core_bp)
    app.register_blueprint(blog_bp)
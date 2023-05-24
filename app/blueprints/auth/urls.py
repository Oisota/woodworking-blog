from . import views

def register_urls(bp):
    """Register routes on blueprint"""
    bp.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'])
    bp.add_url_rule('/logout', view_func=views.logout, methods=['GET', 'POST'])
    bp.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'])
    bp.add_url_rule('/reset', view_func=views.register, methods=['GET', 'POST'])
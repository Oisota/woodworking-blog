
from . import views

def register_urls(bp):
    #bp.add_url_rule('/', view_func=views.home)
    bp.add_url_rule('/about/', view_func=views.about)
from . import views

def register_urls(bp):
    """Register routes on blueprint"""
    bp.add_url_rule('/blog/<publish_date>/<title_slug>/', view_func=views.post, methods=['GET'])
    bp.add_url_rule('/', view_func=views.posts, methods=['GET'])
    bp.add_url_rule('/archive', view_func=views.archive, methods=['GET'])
    bp.add_url_rule('/blog/<post_id>/edit', view_func=views.edit_post, methods=['GET', 'POST'])
    bp.add_url_rule('/blog/new/', view_func=views.new_post, methods=['GET', 'POST'])
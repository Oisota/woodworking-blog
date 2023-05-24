import flask_login

login_manager = flask_login.LoginManager()

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    # TODO load user from DB here
    user = User()
    user.id = email
    return user

# Should I make a new class that inherits from LoginManager?
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

class auth(LoginManager):
    def __init__(self, app):
        self.manager = LoginManager()
        self.manager.init_app(app)


def admin_only(function):
    @wraps(function)
    def decorated_view(*args, **kwargs):
        if current_user.is_anonymous or current_user.id != 1:
            return abort(code=403)
        else:
            return function(*args, **kwargs)
    return decorated_view

# login_manager = LoginManager()
# login_manager.init_app(app)



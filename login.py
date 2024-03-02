# Should I make a new class that inherits from LoginManager?
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

def admin_only(function):
    @wraps(function)
    def decorated_view(*args, **kwargs):
        if current_user.is_anonymous or current_user.id != 1:
            return abort(code=403)
        else:
            return function(*args, **kwargs)
    return decorated_view

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
 
db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    github_url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(), nullable=False)
    img_url_1 = db.Column(db.String(), nullable=False) 
    img_url_2 = db.Column(db.String(), nullable=True) 
    description = db.Column(db.String(), nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)


class Auth(LoginManager):
    def __init__(self, app):
        self.manager = LoginManager()
        self.manager.init_app(app)


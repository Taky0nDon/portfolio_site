import os


from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required

from forms import AddProjectForm


os.environ["DB_URI"] = "sqlite:///test-db.db" 
app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = os.environ["secret_key"]

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


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


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/projects')
def show_projects_page():
    result = db.session.execute(db.select(Project))
    project_rows = result.scalars().all()
    return render_template("projects.html", projects=project_rows)

@app.route('/about-me')
def show_about_me_page():
    return render_template("about-me.html")

@app.route('/about-site')
def show_about_site_page():
    return render_template("about-site.html")

@app.route('/contact')
def show_contact_page():
    return render_template("contact.html")

@app.route('/admin/add', methods=["GET", "POST"])
def add_project_data():
    form = AddProjectForm()
    if form.validate_on_submit():
        new_project = Project(
            title=form.project_title.data,
            description=form.project_description.data,
            github_url=form.project_github_url.data,
            img_url_1=form.project_img_url_1.data,
            img_url_2=form.project_img_url_2.data,
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("show_projects_page"))
    return render_template("add_project.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == login_form.email.data)).scalar()
        if not user:
            flash("No account found for that email address!")
        elif not check_password_hash(user.password_hash, login_form.password.data):
            flash("Incorrect password!")
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)


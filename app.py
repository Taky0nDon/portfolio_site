import os


from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5


from forms import AddProjectForm, LoginForm
from login import auth, login_user, check_password_hash
from classes import db, Project, User


os.environ["DB_URI"] = "sqlite:///test-db.db" 
app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = os.environ["secret_key"]

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db.init_app(app)

auth_manager = auth(app)

@auth_manager.manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


with app.app_context():
    db.create_all()

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
    return render_template("show_form.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.name == login_form.id.data)).scalar()
        print(f"{user=}, {login_form.id.data=}")
        # TODO reimplemet password hash
        if not user:
            print("login failed")
            flash("YOU ARE NOT THE ADMIN, PLEASE LEAVE.")
        elif not user.password_hash == login_form.password.data:
            flash("Incorrect password!")
        else:
            flash("credential correct")
            # login_user(user)
    return render_template("show_form.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)


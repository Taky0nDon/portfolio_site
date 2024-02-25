import os


from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


os.environ["DB_URI"] = "sqlite:///test-db.db" 
app = Flask(__name__)
app.config['SECRET_KEY'] = None

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy()
db.init_app(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    github_url = db.Column(db.String)
    title = db.Column(db.String())
    img_url_1 = db.Column(db.String()) 
    img_url_2 = db.Column(db.String()) 
    description = db.Column(db.String())


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/projects')
def show_projects_page():
    return render_template("projects.html", project_count=5)

@app.route('/about-me')
def show_about_me_page():
    return render_template("about-me.html")

@app.route('/about-site')
def show_about_site_page():
    return render_template("about-site.html")

@app.route('/contact')
def show_contact_page():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


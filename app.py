import os

from flask import Flask, abort, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/projects')
def show_projects_page():
    return render_template("projects.html")

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


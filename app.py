import os

from flask import Flask, abort, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = None

@app.route('/')
def home():
    return render_template("header.html")

@app.route('/test')
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

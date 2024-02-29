
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class AddProjectForm(FlaskForm):
    project_title = StringField("Project Title", validators=[DataRequired()])
    project_img_url_1 = StringField("Image URL 1", validators=[DataRequired()])
    project_img_url_2 = StringField("Image URL 2")
    project_description = StringField("Project Description", validators=[DataRequired()])
    project_github_url = StringField("project_github_url", validators=[DataRequired()])
    add_project = SubmitField("Add Project")

# id = db.Column(db.Integer, primary_key=True)
# github_url = db.Column(db.String)
# description = db.Column(db.String())


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    github_url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(), nullable=False)
    img_url_1 = db.Column(db.String(), nullable=False) 
    img_url_2 = db.Column(db.String(), nullable=False) 
    description = db.Column(db.String(), nullable=False)


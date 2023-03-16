
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Place(db.Model):
    __tablename__ = "place"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

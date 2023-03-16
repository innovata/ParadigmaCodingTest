
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    isAlive = db.Column(db.Boolean, nullable=False)
    placeId = db.Column(db.Integer, nullable=True)

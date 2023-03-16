
from pychall import PKG_PATH

import os
import json

from flask import Flask, render_template, request
from pychall.places.models import *

PSQL_URI = os.environ['PSQL_URI']

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://sambong:@127.0.0.1:5432/places"
app.config["SQLALCHEMY_DATABASE_URI"] = f"{PSQL_URI}/places"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def createtbl():
    with app.app_context():
        db.create_all()

def insert_json():
    with app.app_context():
        f = open(f"{PKG_PATH}/dataset/places.json")
        for d in json.load(f):
            place = Place(id=d['id'], name=d['name'])
            db.session.add(place)
        db.session.commit()

def find(id=None):
    with app.app_context():
        if id is None:
            places = Place.query.all()
        else:
            places = Place.query.filter_by(id=id)
        dics = []
        for place in places:
            dics.append({'id' : place.id, 'name' : place.name})
        return dics


if __name__ == "__main__":
    # createtbl()
    insert_csv()

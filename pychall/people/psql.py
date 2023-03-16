
from pychall import PKG_PATH

import os
import json

from flask import Flask, render_template, request
from pychall.people.models import *

PSQL_URI = os.environ['PSQL_URI']

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sambong:@127.0.0.1:5432/people"
app.config["SQLALCHEMY_DATABASE_URI"] = f"{PSQL_URI}/people"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def createtbl():
    with app.app_context():
        db.create_all()

def insert_json():
    with app.app_context():
        f = open(f"{PKG_PATH}/dataset/people.json")
        for d in json.load(f):
            person = Person(id=d['id'], name=d['name'], isAlive=d['isAlive'], placeId=d['placeId'])
            db.session.add(person)
        db.session.commit()

def find(id=None):
    with app.app_context():
        if id is None:
            people = Person.query.all()
        else:
            people = Person.query.filter_by(id=id)
        dics = []
        for person in people:
            dics.append({'id' : person.id, 'name' : person.name, 'isAlive':person.isAlive, 'placeId':person.placeId})
        return dics

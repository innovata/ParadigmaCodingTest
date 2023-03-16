
from pychall import psql, models, PJT_PATH, PKG_PATH
import json
import csv


def load_json(filename):
    with open(file=f"{PKG_PATH}/dataset/{filename}", mode='r') as f:
        text = f.read()
        f.close()
    return json.loads(s=text)

def load_csv(filename):
    with open(file=f"{PKG_PATH}/dataset/{filename}", newline='') as csvfile:
        return csv.reader(csvfile, delimiter=' ', quotechar='|')

def initialize():
    """Create DBs"""
    # db = psql.DataBase()
    # db.createdb(dbname='place')
    # db.createdb(dbname='person')
    """Create TBLs & Insert Data"""
    # jsdata = load_json(filename='places.json')
    # place = models.Place()
    # # place.droptbl()
    # place.createtbl()
    # place.insert_many(dics=jsdata)

    jsdata = load_json(filename='people.json')
    person = models.Person()
    # person.droptbl()
    person.createtbl()
    person.insert_many(dics=jsdata)

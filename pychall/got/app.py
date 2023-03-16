"""
This is Got-Flask module.

Set up the below OS Envrionment :

export FLASK_APP=pychall/got/app
export FLASK_RUN_PORT=8083
"""
print(f"{'*'*50} {__name__}\n{__doc__}\n{'*'*50}")


from flask import Flask, redirect, jsonify
import inspect
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/v1/places/")

@app.route("/v1/places/")
def call_api():
    handler = ApiHandler()
    return jsonify( handler.join() )

from flask_restplus import Resource, Api
from pandas import DataFrame

api = Api(app)

@api.route("/v1/places/<string:placeId>")
class ApiHandler(Resource):
    def get(self, placeId):
        return jsonify( self.join(placeId) )

    def places_api(self, placeId=None):
        if placeId is None:
            res = requests.get("http://127.0.0.1:8081/v1/places/")
        else:
            res = requests.get(f"http://127.0.0.1:8081/v1/places/{placeId}")
        rv = json.loads(res.text)
        print(f"\nplaces_api :\n{rv}")
        return rv

    def people_api(self, placeId=None):
        if placeId is None:
            res = requests.get("http://127.0.0.1:8082/v1/people/")
        else:
            res = requests.get(f"http://127.0.0.1:8082/v1/people/{placeId}")
        rv = json.loads(res.text)
        print(f"\npeople_api :\n{rv}")
        return rv

    def join(self, placeId=None):
        places = self.places_api(placeId)
        people = self.people_api(placeId)
        ppldf = DataFrame(people)
        print(f"\nppldf :\n{ppldf}")
        ppldf = ppldf.dropna(axis=0, how='any')
        for place in places:
            df = ppldf[ppldf.placeId == place['id']]
            del(df['placeId'])
            place['people'] = df.to_dict('records')
        return places


from flask_swagger import swagger

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['definitions']['Guide'] = __doc__
    swag['info']['title'] = 'people-microservice-api'
    swag['info']['version'] = '1.0.0'
    swag['paths'] = 'got-microservice:8083/v1/places/'
    return jsonify(swag)


def main():
    app.run(port=8083)

"""
This is People-Flask module.

Set up the below OS Envrionment :

export FLASK_APP=pychall/people/app
export FLASK_RUN_PORT=8082
"""
print(f"{'*'*50} {__name__}\n{__doc__}\n{'*'*50}")


from flask import Flask, redirect, jsonify
import inspect
from . import psql

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/v1/people/")

@app.route("/v1/people/")
def call_api():
    return jsonify( psql.find(id=None) )

from flask_restplus import Resource, Api

api = Api(app)

@api.route("/v1/people/<string:placeId>")
class ApiHandler(Resource):
    def get(self, placeId):
        return jsonify( psql.find(id=placeId) )


from flask_swagger import swagger

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['definitions']['Guide'] = __doc__
    swag['info']['title'] = 'people-microservice-api'
    swag['info']['version'] = '1.0.0'
    swag['paths'] = 'people-microservice:8082/v1/people/'
    return jsonify(swag)


def main():
    app.run(port=8082)

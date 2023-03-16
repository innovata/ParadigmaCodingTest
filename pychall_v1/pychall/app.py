"""
This is Flask module.

Set up the below OS Envrionment :

1. export FLASK_APP=app.py
"""
print(f"{'*'*50} {__name__}\n{__doc__}\n{'*'*50}")

from flask import Flask
import inspect
from pychall import dbg

app = Flask(__name__)
# dbg.odict(obj=app)
# dbg.attrs(obj=app)

@app.route("/")
def index():
    return f"{__name__} | {inspect.stack()[0][3]}"

@app.route("/<string:svc>")
def service(svc):
    return f"Service Name : {svc}"

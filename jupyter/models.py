
from jupyter.ide import *
from pychall import models, psql
import importlib

importlib.reload(psql)
importlib.reload(models)
# dir(models)
p = models.Place()
dir(p)
p.modelname
p.tblname
p.ct_sql
p.createtbl(p.ct_sql)
CREATE TABLE place (id INTEGER PRIMARY KEY, name VARCHAR);
CREATE TABLE leads (id INTEGER PRIMARY KEY, name VARCHAR);

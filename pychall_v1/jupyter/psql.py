
%env PSQL_DBNAME=pychall
%env PSQL_USER=sambong
from jupyter.ide import *
sorted(sys.path)
from pychall import psql
import importlib
importlib.reload(psql)
dir(psql)
dir(psql.conn)
psql.conn.__class__
psql.conn.__doc__
psql.conn.encoding
psql.conn.status
psql.conn.server_version
psql.conn.info
psql.conn.isexecuting()
psql.conn.dsn



class SampleModel(psql.Model):

    def __init__(self):
        super().__init__(__class__)

s = SampleModel()
# dir(s)
s.cur
dir(s.cur)
s.cur.__class__
s.cur.__doc__

s.cur.execute("CREATE TABLE place1 (id INTEGER PRIMARY KEY, name VARCHAR);")

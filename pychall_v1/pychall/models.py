
from pychall import psql



class Place(psql.Model):

    def __init__(self, dbname='place'):
        super().__init__(dbname, __class__)

    def createtbl(self):
        sql = f"CREATE TABLE {self.modelname} (id integer PRIMARY KEY, name varchar);"
        self.oneway_op(sql=sql)

class Person(psql.Model):

    def __init__(self, dbname='person'):
        super().__init__(dbname, __class__)

    def createtbl(self):
        sql = f"CREATE FOREIGN TABLE {self.modelname} (id integer PRIMARY KEY, name varchar, isAlive boolean, placeId integer REFERENCES place.place(id));"
        self.oneway_op(sql=sql)
        


import unittest
from pychall import psql
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pprint
pp = pprint.PrettyPrinter(indent=2)
import inspect
import sys
from pychall import dbg



@unittest.skip("inspector")
class PsqlModuleInspector(unittest.TestCase):

    # @unittest.skip("reason")
    def test__module(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        dbg.odict(obj=psql)
        # dbg.attrs(obj=psql)

@unittest.skip("test_case")
class DataBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.db = psql.DataBase()

    @unittest.skip("reason")
    def test__createdb_dropdb(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        self.db.createdb(dbname='sampledb')
        self.db.dropdb(dbname='sampledb')

    # @unittest.skip("reason")
    def test__initdbs(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        dbnames = ['Place','Person']
        for dbname in dbnames:
            self.db.dropdb(dbname)
        psql.initdbs(dbnames=dbnames)

@unittest.skip("inspector")
class ModelIspector(unittest.TestCase):

    def setUp(self):
        class SampleModel(psql.Model):
            def __init__(self):
                super().__init__(__class__)
        self.m = SampleModel()

    # @unittest.skip("reason")
    def test__init(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        dbg.odict(obj=self.m)

    # @unittest.skip("reason")
    def test__connect(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        self.m.connect()
        dbg.odict(obj=self.m.conn)
        dbg.attrs(obj=self.m.conn)
        print(f"{'- '*25}\n cur.closed : {self.m.cur.closed}")
        print(f"{'- '*25}\n conn.closed : {self.m.conn.closed}")
        self.m.conn.close()
        print(f"{'- '*25}\n cur.closed : {self.m.cur.closed}")
        print(f"{'- '*25}\n conn.closed : {self.m.conn.closed}")

    @unittest.skip("reason")
    def test__cur(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        self.m.connect()
        cur = self.m.cur
        dbg.odict(obj=cur)
        dbg.attrs(obj=cur)
        print(f"{'- '*25}\n cur.closed : {cur.closed}")
        self.m.conn.close()
        print(f"{'- '*25}\n cur.closed : {cur.closed}")

    @unittest.skip("reason")
    def test__execute(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        try:
            self.m.connect()
            rv = self.m.cur.execute("CREATE TABLE test1 (id INTEGER PRIMARY KEY, name VARCHAR);")
        except psycopg2.DatabaseError or Exception as e:
            print('Error : %s' % e)
        else:
            print(f"rv (before commit) : {rv}")
            rv = self.m.conn.commit()
            print(f"rv (after commit) : {rv}")
        finally:
            if self.m.conn:
                self.m.conn.close()

# @unittest.skip("test_case")
class ModelTestCase(unittest.TestCase):

    def setUp(self):
        class SampleModel(psql.Model):
            def __init__(self, dbname):
                sql = f"CREATE TABLE {__class__.__name__} (id serial PRIMARY KEY, num integer, data varchar);"
                super().__init__(dbname=dbname, modelcls=__class__, sql=sql)
        self.dbname = 'sampledb'
        self.m = SampleModel(dbname=self.dbname)

    # @unittest.skip("reason")
    def test__init(self):
        self.assertEqual(self.m.user, 'sambong')
        self.assertEqual(self.m.dbname, 'sampledb')
        self.assertEqual(self.m.modelname, 'SampleModel')
        sql = [f"SELECT * FROM {self.m.modelname};"]
        self.m.select(sql=sql)

    @unittest.skip("reason")
    def test__execute__insert(self):
        print(f"\n{'='*50} {__class__} | {inspect.stack()[0][3]}")
        self.m.createdb(dbname=self.dbname)
        sqls = [f"INSERT INTO {self.m.modelname} (id, text) VALUES (100, 'test_sent');"]
        self.m.execute(sqls=sqls)
        self.m.dropdb(dbname=self.dbname)





if __name__ == '__main__':
    unittest.main()

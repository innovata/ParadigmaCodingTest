
import unittest
from pychall import psql

import pprint
pp = pprint.PrettyPrinter(indent=2)
import inspect
from pychall import dbg



@unittest.skip("inspector")
class PsqlModuleInspector(unittest.TestCase):

    def test__module(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        dbg.odict(obj=psql)
        dbg.attrs(obj=psql)

# @unittest.skip("test_case")
class DataBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.db = psql.DataBase()

    # @unittest.skip("reason")
    def test__createdb_dropdb(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        self.db.createdb(dbname='sampledb')
        self.db.dropdb(dbname='sampledb')

    # @unittest.skip("reason")
    def test__create_dbs(self):
        print(f"\n{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
        dbnames = ['places','people']
        for dbname in dbnames:
            self.db.dropdb(dbname=dbname)
        psql.create_dbs(dbnames=dbnames)


if __name__ == '__main__':
    unittest.main()

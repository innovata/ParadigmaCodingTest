
import unittest
from pychall import initdb, models, psql
import inspect


# @unittest.skip("test_case")
class LoadJsonTestCase(unittest.TestCase):

    @unittest.skip("reason")
    def test__load_json(self):
        print(f"\n{'='*50} {__class__} | {inspect.stack()[0][3]}")
        jsdata = initdb.load_json(filename='places.json')
        self.assertTrue(isinstance(jsdata, list))
        print(jsdata)

    # @unittest.skip("reason")
    def test__initialize__insert_many(self):
        print(f"\n{'='*50} {__class__} | {inspect.stack()[0][3]}")
        initdb.initialize()
        """Varify Place"""
        # place = models.Place()
        # rows = place.select(sql=f"SELECT * FROM {place.modelname}")
        # # self.assertTrue(isinstance(rows, list))
        # # if len(rows) is not 0:
        # #     self.assertTrue(isinstance(rows[0], tuple))
        # print(f"rows : {rows}\ntype : {type(rows)}")
        """Varify Person"""
        person = models.Person()
        rows = person.select(sql=f"SELECT * FROM {person.modelname}")
        # self.assertTrue(isinstance(rows, list))
        # if len(rows) is not 0:
        #     self.assertTrue(isinstance(rows[0], tuple))
        print(f"rows : {rows}\ntype : {type(rows)}")
        # """Clean DBs & TBLs"""
        # person.droptbl()
        # place.droptbl()
        # db = psql.DataBase()
        # db.dropdb(dbname='place')
        # db.dropdb(dbname='person')

@unittest.skip("test_case")
class PersonTestCase(unittest.TestCase):

    def setUp(self):
        self.p = models.Person()



if __name__ == '__main__':
    unittest.main()

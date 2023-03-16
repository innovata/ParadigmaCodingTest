
import unittest
from pychall import models, dbg
import inspect


# @unittest.skip("test_case")
class PlaceTestCase(unittest.TestCase):

    def setUp(self):
        print(f"\n{'='*50} {__class__} | {inspect.stack()[0][3]}")
        self.dbname = 'place'
        self.p = models.Place(dbname=self.dbname)

    def test__init(self):
        print(f"\n{'='*50} {__class__} | {inspect.stack()[0][3]}")
        self.assertEqual(self.p.user, 'sambong')
        self.assertEqual(self.p.dbname, self.dbname)
        self.assertEqual(self.p.modelname, self.dbname)

    # @unittest.skip("reason")
    def test__createtbl_droptbl(self):
        print(f"\n{'='*50} {__class__} | {inspect.stack()[0][3]}")
        self.p.modelname = 'place1'
        self.p.createtbl()
        row = self.p.select(sql=f"SELECT * FROM {self.p.modelname}")
        print(f"row : {row}")
        self.p.droptbl()

@unittest.skip("test_case")
class PersonTestCase(unittest.TestCase):

    def setUp(self):
        self.p = models.Person()



if __name__ == '__main__':
    unittest.main()

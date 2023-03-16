
import unittest
import requests


class GotTestCase(unittest.TestCase):

    url = "http://127.0.0.1:8083/v1/places/"

    def setUp(self):
        self.jsdata = requests.get(self.url).json()

    def test__jsdata(self):
        self.assertTrue(isinstance(self.jsdata, list))

    def test__datum(self):
        datum = self.jsdata[0]
        self.assertTrue(isinstance(datum, dict))
        self.assertTrue('people' in list(datum))

    def test__poeple(self):
        people = self.jsdata[0]['people']
        self.assertTrue(isinstance(people, list))
        person = people[0]
        self.assertTrue('placeId' not in list(person))



if __name__ == "__main__":
    unittest.main()

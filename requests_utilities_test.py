

import unittest
import requests_utilities


class Testrequests_utilities(unittest.TestCase):

    def setUp(self):
        self.weather_dict = {}

        self.params = {
            'access_key': 'e4eb60681cb3f243e72cafc0fd07df97',
            'query': 'new york'
        }

    def test_test_internet_connection(self):
        self.assertEqual(requests_utilities.test_internet_connection(), True)
        self.assertEqual(requests_utilities.test_internet_connection('http://gggvvddbfbt.co'), False)

    def test_user_location(self):
        pass

    def test_weather_by_location_json(self):
        pass

    def test_get_info_from_json(self):
        pass


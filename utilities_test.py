

import unittest
import utilities


class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.weather_dict = {
            'city_name': 'Tel Aviv-Yafo', 'local_time': '2020-07-19 13:47',\
                    'current_temp': 30, 'currnet_desc': 'Sunny', 'current_humidity': 59,\
                    'current_visibility': 7
        }

        self.params = {
            'access_key': 'e4eb60681cb3f243e72cafc0fd07df97',
            'query': 'new york'
        }

    def test_visibility_scale_to_desc(self):
        val_dict1 = {
            'city_name': 'Tel Aviv-Yafo', 'local_time': '2020-07-19 13:47', \
            'current_temp': 30, 'currnet_desc': 'Sunny', 'current_humidity': 59, \
            'current_visibility': 'Good'
        }
        self.assertEqual(utilities.visibility_scale_to_desc(self.weather_dict), val_dict1)
        self.weather_dict['current_visibility'] = 8
        val_dict1['current_visibility'] = 'Very good'
        self.assertEqual(utilities.visibility_scale_to_desc(self.weather_dict), val_dict1)

    def test_change_desc_to_alphabet_only(self):
        self.assertEqual(utilities.change_desc_to_alphabet_only('[Sunny]'), 'Sunny')
        self.assertEqual(utilities.change_desc_to_alphabet_only('[-=]'), '')
        self.assertEqual(utilities.change_desc_to_alphabet_only('Good'), 'Good')

    def test_make_string_for_weather(self):
        self.assertEqual(utilities.make_string_for_weather(self.weather_dict), 'now 2020-07-19 13:47 at Tel Aviv-Yafo the weather is Sunny. \ntemp is 30°C, humidity: 59% and the visibility is 7.')
        self.weather_dict['city_name'] = 'delhi'
        self.assertEqual(utilities.make_string_for_weather(self.weather_dict), 'now 2020-07-19 13:47 at delhi the weather is Sunny. \ntemp is 30°C, humidity: 59% and the visibility is 7.')
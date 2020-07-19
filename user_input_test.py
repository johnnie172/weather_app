import unittest
import mock
import user_input_utilities
import main

class TestInputUtilities(unittest.TestCase):

    def setUp(self):
        params = {
            'access_key': 'e4eb60681cb3f243e72cafc0fd07df97',
            'query': 'new york'
        }

    def test_choose_diffrent_city(self):
        with mock.patch('builtins.input', return_value="yes"):
            self.assertEqual(user_input_utilities.choose_diffrent_city(main.params), "d")

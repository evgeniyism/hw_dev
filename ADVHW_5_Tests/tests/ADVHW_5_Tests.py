import unittest
import Advanced.ADVHW_5_Tests.app as app
from unittest.mock import patch
import requests


class AppTest(unittest.TestCase):
    def setUp(self):
        app.directories = {"1": ["2207 876234", "11-2"],"2": ["10006"],"3": []}
        app.documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

    def test_get_all_doc_owners_names(self):
        app.get_all_doc_owners_names()
        self.assertTrue(type(app.get_all_doc_owners_names()) == set, 'Type error: set expected')
        self.assertTrue(len(app.get_all_doc_owners_names()) == len(app.documents), 'Wrong number of names')

    def test_add_new_shelf(self):
        initial_number_of_shelfs = len(app.directories)
        print(initial_number_of_shelfs)
        with patch('builtins.input', return_value='4'):
            app.add_new_shelf()
        self.assertIn('4', app.directories.keys())

    def test_move_doc_to_shelf(self):
        print(app.directories)
        with patch('builtins.input', side_effect=['2207 876234', '3']):
            app.move_doc_to_shelf()
        print(app.directories)
        self.assertIn('2207 876234', app.directories['3'])


class YandexTest(unittest.TestCase):

    def setUp(self):
        self.API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    def test_translator(self):
        params = {
            'key': self.API_KEY,
            'text': 'привет',
            'lang': 'en',
        }
        response = requests.get(self.URL, params=params)
        json_ = response.json()
        self.assertTrue(''.join(json_['text']) == 'hi')
        self.assertIsNot(response.status_code, '404')
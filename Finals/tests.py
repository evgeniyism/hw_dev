from Advanced.Finals_Advanced.VKinder_manager import VKinder_search
from pymongo import MongoClient
import unittest


class VKinder_search_Test(unittest.TestCase):
    def setUp(self):
        self.app = VKinder_search()

    def test_user(self):
        check_user = self.app.user
        self.assertTrue(check_user, 'User not accessible')

    def test_base(self):
        self.client = MongoClient()
        self.active_db = self.client['VKinder']
        ping = self.active_db.command('ping')
        self.assertTrue(ping == {u'ok': 1.0}, 'No connection with base')

    def test_search_first_page(self):
        search = self.app.search_first_page()
        print(type(search))
        self.assertTrue(len(search) == 10, 'API error')
        self.assertTrue(isinstance(search, list), 'Type error: list expected')

    def test_search_next_page(self):
        search = self.app.search_next_page()
        self.assertTrue(len(search) == 10, 'API error')
        self.assertTrue(isinstance(search, list), 'Type error: list expected')
        self.assertTrue(self.app.page % 10 == 0, 'Page error')


# class Methods_test(unittest.TestCase):
#     def setUp(self):
#         self.app = VKinder()
#
#     def make_request_test(self):
#         response = self.app.make_request('database.getCities', {'country_id': 1, 'q': 'Москва', 'count': 1})
#         self.assertTrue(response.status_code == 200, 'API error')
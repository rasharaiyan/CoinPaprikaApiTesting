import unittest
from infra.api_wrapper import APIWrapper
from logic.SearchService import SearchService
from api_tests.test_utils import TestBase

class TestSearchService(TestBase):
#Returns currencies, exchanges, icos, people, tags on coinpaprika.com for a given search query.

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = SearchService(APIWrapper("https://api.coinpaprika.com", None))

    def test_search(self):
        response = self.service.search('btc')
        print("Response:", response)  # Print the response to the console
        for category in ['currencies', 'icos', 'exchanges', 'people', 'tags']:
            self.assertIn(category, response)
            self.assertIsInstance(response[category], list)

    def test_search_detailed(self):
        query = 'btc'
        response = self.service.search(query)
        # Test detailed assertions for each category in the response
        # Currencies
        for currency in response['currencies']:
            self.assertIsInstance(currency['id'], str)
            self.assertIsInstance(currency['name'], str)
            self.assertIsInstance(currency['symbol'], str)
            self.assertIsInstance(currency['rank'], int)
            self.assertIsInstance(currency['is_new'], bool)
            self.assertIsInstance(currency['is_active'], bool)
            self.assertIsInstance(currency['type'], str)
        # ICOs
        for ico in response['icos']:
            self.assertIsInstance(ico['id'], str)
            self.assertIsInstance(ico['name'], str)
            self.assertIsInstance(ico['symbol'], str)
            self.assertIsInstance(ico['is_new'], bool)
        # Exchanges
        for exchange in response['exchanges']:
            self.assertIsInstance(exchange['id'], str)
            self.assertIsInstance(exchange['name'], str)
            self.assertIsInstance(exchange['rank'], int)
        # People
        for person in response['people']:
            self.assertIsInstance(person['id'], str)
            self.assertIsInstance(person['name'], str)
            self.assertIsInstance(person['teams_count'], int)
        # Tags
        for tag in response['tags']:
            self.assertIsInstance(tag['id'], str)
            self.assertIsInstance(tag['name'], str)
            self.assertIsInstance(tag['coin_counter'], int)
            self.assertIsInstance(tag['ico_counter'], int)
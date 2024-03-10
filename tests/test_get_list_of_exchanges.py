import unittest
from infra.api_wrapper import APIWrapper
from logic.ListExchanges import ListExchanges
from tests.test_utils import TestBase

class TestListExchanges(TestBase):
#Returns basic information about exchanges on coinpaprika.com
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = ListExchanges(APIWrapper("https://api.coinpaprika.com", None))

    def test_list_exchanges(self):
        response = self.service.list_exchanges()
        print("Response:", response)  # Print the response to the console
        self.assertIsInstance(response, list)
        for exchange in response:
            self.assertIsInstance(exchange['id'], str)
            self.assertIsInstance(exchange['name'], str)
            self.assertIsInstance(exchange['active'], bool)
            self.assertIsInstance(exchange['website_status'], bool)
            self.assertIsInstance(exchange['api_status'], bool)
            self.assertIsInstance(exchange['markets_data_fetched'], bool)
            if exchange['adjusted_rank'] is not None:
                self.assertIsInstance(exchange['adjusted_rank'], int)
            if exchange['reported_rank'] is not None:
                self.assertIsInstance(exchange['reported_rank'], int)
            self.assertIsInstance(exchange['currencies'], int)
            self.assertIsInstance(exchange['markets'], int)
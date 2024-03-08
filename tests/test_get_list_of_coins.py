import unittest
from infra.api_wrapper import APIWrapper
from logic.ListCoins import ListCoins
from tests.test_utils import TestBase

class TestListCoins(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = ListCoins(APIWrapper("https://api.coinpaprika.com", None))

    def test_list_coins(self):
        response = self.service.list_coins()
        self.assertIsInstance(response, list)
        for coin in response:
            self.assertIsInstance(coin['id'], str)
            self.assertIsInstance(coin['name'], str)
            self.assertIsInstance(coin['symbol'], str)
            self.assertIn(coin['type'], ['coin', 'token'])
            self.assertIsInstance(coin['rank'], int)
            self.assertIsInstance(coin['is_new'], bool)
            self.assertIsInstance(coin['is_active'], bool)
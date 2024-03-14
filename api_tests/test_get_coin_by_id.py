import unittest
from infra.api_wrapper import APIWrapper
from logic.GetCoinById import GetCoinByID
from logic.ListCoins import ListCoins
from api_tests.test_utils import TestBase


class TestGetCoinByID(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = GetCoinByID(
            APIWrapper("https://api.coinpaprika.com", None))


    def test_get_coin_by_id(self):
        coin_id = 'btc-bitcoin'
        response = self.service.get_coin_by_id(coin_id)
        print("Response:", response)  # Print the response to the console
        self.assertEqual(response['id'], coin_id)
        self.assertIsInstance(response['name'], str)
        self.assertIsInstance(response['symbol'], str)
        self.assertIsInstance(response['rank'], int)
        self.assertIsInstance(response['is_new'], bool)
        self.assertIsInstance(response['is_active'], bool)
        self.assertIn(response['type'], ['coin', 'token'])
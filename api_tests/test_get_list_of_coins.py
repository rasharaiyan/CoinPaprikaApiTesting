import unittest
from infra.api_wrapper import APIWrapper
from logic.ListCoins import ListCoins
from api_tests.test_utils import TestBase

class TestListCoins(TestBase):
    """
    This class contains the tests for the ListCoins service. It inherits from TestBase,
    providing common setup and teardown methods for all tests. The ListCoins service is
    responsible for fetching a list of cryptocurrencies from the CoinPaprika API.
    """

    @classmethod
    def setUpClass(cls):
        """
        Class-level setup function that runs once before any tests are executed.
        It initializes the ListCoins service with a wrapped version of the CoinPaprika API.
        """
        super().setUpClass()
        cls.service = ListCoins(APIWrapper("https://api.coinpaprika.com", None))

    def test_list_coins(self):
        response = self.service.list_coins()  # Call the list_coins method from the service
        print("Response:", response)  # Print the response to the console
        self.assertIsInstance(response, list)  # Check if the response is a list
        for coin in response:  # Iterate through each coin in the response
            # Validate types and values of each attribute of the coin
            self.assertIsInstance(coin['id'], str)
            self.assertIsInstance(coin['name'], str)
            self.assertIsInstance(coin['symbol'], str)
            self.assertIn(coin['type'], ['coin', 'token'])
            self.assertIsInstance(coin['rank'], int)
            self.assertIsInstance(coin['is_new'], bool)
            self.assertIsInstance(coin['is_active'], bool)
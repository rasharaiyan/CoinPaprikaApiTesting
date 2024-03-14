import unittest
from infra.api_wrapper import APIWrapper
from logic.ListCoins import ListCoins


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = ListCoins(APIWrapper("https://api.coinpaprika.com", None))

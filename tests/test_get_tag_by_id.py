import unittest
from infra.api_wrapper import APIWrapper
from logic.GetTagById import GetTagByID
from tests.test_utils import TestBase
 # Returns information about a given cryptocurrency tag
class TestGetTagById(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = GetTagByID(APIWrapper("https://api.coinpaprika.com", None))

    def test_get_tag_by_id(self):
        tag_id = 'blockchain-service'
        response = self.service.get_tag_by_id(tag_id)
        self.assertEqual(response['id'], tag_id)
        self.assertIsInstance(response['name'], str)
        self.assertIsInstance(response['coin_counter'], int)
        self.assertIsInstance(response['ico_counter'], int)
        self.assertIsInstance(response['description'], str)
        self.assertIsInstance(response['type'], str)
        self.assertIsInstance(response.get('coins', []), list)  # Checks if 'coins' is a list if present
        self.assertIsInstance(response.get('icos', []), list)  # Checks if 'icos' is a list if present


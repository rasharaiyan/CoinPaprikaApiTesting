import unittest
from infra.api_wrapper import APIWrapper
from logic.ListTags import ListTags
from tests.test_utils import TestBase

class TestListTags(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = ListTags(APIWrapper("https://api.coinpaprika.com", None))


    def test_list_tags(self):
        #Returns basic information about cryptocurrencies tags (categories)
        response = self.service.list_tags()
        print("Response:", response)  # Print the response to the console
        self.assertIsInstance(response, list)
        for tag in response:
            self.assertIsInstance(tag['id'], str)
            self.assertIsInstance(tag['name'], str)
            self.assertIsInstance(tag['coin_counter'], int)
            self.assertIsInstance(tag['ico_counter'], int)
            self.assertIsInstance(tag['description'], str)
            self.assertIsInstance(tag['type'], str)
            # If 'coins' and 'icos' are expected to be present
            self.assertIsInstance(tag.get('coins', []), list)  # Checks if 'coins' key exists and is a list
            self.assertIsInstance(tag.get('icos', []), list)  # Checks if 'icos' key exists and is a list
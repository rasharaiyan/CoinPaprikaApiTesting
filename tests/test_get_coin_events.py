from logic.GetCoinEvents import GetCoinEvents
from tests.test_utils import TestBase
from infra.api_wrapper import APIWrapper


class TestGetCoinEvents(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = GetCoinEvents(APIWrapper("https://api.coinpaprika.com", None))

    def test_get_coin_events_structure(self):
        coin_id = 'btc-bitcoin'
        events = self.service.get_coin_events(coin_id)
        self.assertIsInstance(events, list)
        for event in events:
            self.assertIsInstance(event['id'], str)
            self.assertIsInstance(event['date'], str)
            # 'date_to' can be a string or null
            self.assertTrue(isinstance(event['date_to'], str) or event['date_to'] is None)
            self.assertIsInstance(event['name'], str)
            self.assertIsInstance(event['description'], str)
            self.assertIsInstance(event['is_conference'], bool)
            # 'link' can be a string or null
            self.assertTrue(isinstance(event['link'], str) or event['link'] is None)
            # 'proof_image_link' can be a string or null
            self.assertTrue(isinstance(event['proof_image_link'], str) or event['proof_image_link'] is None)


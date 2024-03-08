from infra.api_wrapper import APIWrapper

class GetCoinEvents:

    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def get_coin_events(self, coin_id):
        endpoint = f"/v1/coins/{coin_id}/events"
        return self.api_wrapper.api_get_request(endpoint)

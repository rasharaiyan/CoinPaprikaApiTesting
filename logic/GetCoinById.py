class GetCoinByID:

    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def get_coin_by_id(self, coin_id):
        endpoint = f"/v1/coins/{coin_id}"
        print(coin_id)
        return self.api_wrapper.api_get_request(endpoint)

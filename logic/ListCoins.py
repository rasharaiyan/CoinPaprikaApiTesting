from infra.api_wrapper import APIWrapper


class ListCoins:
    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def list_coins(self):
        return self.api_wrapper.api_get_request("/v1/coins")

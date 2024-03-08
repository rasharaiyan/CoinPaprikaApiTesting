from infra.api_wrapper import APIWrapper

class ListExchanges:

    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def list_exchanges(self, quotes=''):
        endpoint = "/v1/exchanges"
        if quotes:
            endpoint += f"?quotes={quotes}"
        return self.api_wrapper.api_get_request(endpoint)

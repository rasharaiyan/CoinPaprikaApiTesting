from infra.api_wrapper import APIWrapper
class SearchService:

    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def search(self, query, categories='currencies,exchanges,icos,people,tags', limit=6):
        endpoint = f"/v1/search?q={query}&c={categories}&limit={limit}"
        return self.api_wrapper.api_get_request(endpoint)

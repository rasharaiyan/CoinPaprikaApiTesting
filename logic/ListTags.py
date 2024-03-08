from infra.api_wrapper import APIWrapper

class ListTags:

    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def list_tags(self, additional_fields=''):
        endpoint = "/v1/tags"
        if additional_fields:
            endpoint += f"?additional_fields={additional_fields}"
        return self.api_wrapper.api_get_request(endpoint)

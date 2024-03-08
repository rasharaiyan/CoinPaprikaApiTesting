from infra.api_wrapper import APIWrapper

class GetTagByID:

    def __init__(self, api_wrapper):
        self.api_wrapper = api_wrapper

    def get_tag_by_id(self, tag_id, additional_fields=''):
        endpoint = f"/v1/tags/{tag_id}"
        if additional_fields:
            endpoint += f"?additional_fields={additional_fields}"
        return self.api_wrapper.api_get_request(endpoint)

import requests

class APIWrapper:
    def __init__(self, base_url, api_key):
        self.BASE_URL = base_url
        self.headers = {'Authorization': api_key}

    def api_get_request(self, endpoint):
        full_url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(full_url, headers=self.headers)
        if response.ok:
            return response.json()  # Return JSON data if call successful
        else:
            return response.status_code  # Return HTTP status code if call fails
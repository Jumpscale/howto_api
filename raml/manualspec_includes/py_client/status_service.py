class StatusService:
    def __init__(self, client):
        self.client = client



    def status_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /status
        """
        uri = self.client.base_url + "/status"
        return self.client.get(uri, None, headers, query_params, content_type)


from .Status import Status
from .api_response import APIResponse
from .unmarshall_error import UnmarshallError

class StatusService:
    def __init__(self, client):
        self.client = client



    def status_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /status
        """
        uri = self.client.base_url + "/status"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            return APIResponse(data=Status(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        

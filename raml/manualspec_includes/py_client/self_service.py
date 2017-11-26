
from .User import User
from .api_response import APIResponse
from .unmarshall_error import UnmarshallError

class SelfService:
    def __init__(self, client):
        self.client = client



    def self_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /self
        """
        uri = self.client.base_url + "/self"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            return APIResponse(data=User(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        

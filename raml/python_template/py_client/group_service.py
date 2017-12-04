
from .Group import Group
from .api_response import APIResponse
from .unmarshall_error import UnmarshallError

class GroupService:
    def __init__(self, client):
        self.client = client



    def deleteGroup(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete group
        It is method for DELETE /group/{id}
        """
        uri = self.client.base_url + "/group/"+id
        resp = self.client.delete(uri, None, headers, query_params, content_type)
        try:
            return APIResponse(data=Group(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


    def getGroup(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get group, id=int
        It is method for GET /group/{id}
        """
        uri = self.client.base_url + "/group/"+id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            return APIResponse(data=Group(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


    def updateGroup(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update group
        It is method for POST /group/{id}
        """
        uri = self.client.base_url + "/group/"+id
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            return APIResponse(data=Group(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


    def group_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of groups
        It is method for GET /group
        """
        uri = self.client.base_url + "/group"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            resps = []
            for elem in resp.json():
                resps.append(Group(elem))
            return APIResponse(data=resps, response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


from .User import User
from .api_response import APIResponse
from .unmarshall_error import UnmarshallError

class UserService:
    def __init__(self, client):
        self.client = client



    def deleteUser(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete user
        It is method for DELETE /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        resp = self.client.delete(uri, None, headers, query_params, content_type)
        try:
            return APIResponse(data=User(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


    def getUser(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get user, id=int
        It is method for GET /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            return APIResponse(data=User(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


    def updateUser(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update user
        It is method for POST /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            return APIResponse(data=User(resp.json()), response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        


    def user_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of users
        It is method for GET /user
        """
        uri = self.client.base_url + "/user"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            resps = []
            for elem in resp.json():
                resps.append(User(elem))
            return APIResponse(data=resps, response=resp)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
        

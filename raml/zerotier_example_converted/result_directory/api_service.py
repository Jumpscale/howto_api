class ApiService:
    def __init__(self, client):
        self.client = client



    def TerminateCurrentSession(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Hitting this endpoint causes the user to be logged out. It has no effect when using token authentication, so it's mostly used by the UI.
        It is method for POST /api/auth/_logout
        """
        uri = self.client.base_url + "/api/auth/_logout"
        return self.client.post(uri, data, headers, query_params, content_type)


    def GetAllViewableNetworks(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get all networks for which you have at least read access.
        It is method for GET /api/network
        """
        uri = self.client.base_url + "/api/network"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GenerateaRandomToken(self, headers=None, query_params=None, content_type="application/json"):
        """
        This generates a random token suitable for use as an API token server-side using a secure random source. It does not actually modify the user record, just returns the token for use by API callers or the UI.
        It is method for GET /api/randomToken
        """
        uri = self.client.base_url + "/api/randomToken"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GetCurrentlyAuthenticatedUser(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get the currently authenticated user's user record.
        It is method for GET /api/self
        """
        uri = self.client.base_url + "/api/self"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GetStatusandConfigurationInformation(self, headers=None, query_params=None, content_type="application/json"):
        """
        Obtain information about this server and/or useful to the Central web UI.
        It is method for GET /api/status
        """
        uri = self.client.base_url + "/api/status"
        return self.client.get(uri, None, headers, query_params, content_type)


    def RetrieveaUser(self, userId, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /api/user/{userId}
        """
        uri = self.client.base_url + "/api/user/"+userId
        return self.client.get(uri, None, headers, query_params, content_type)


    def UpdateaUser(self, data, userId, headers=None, query_params=None, content_type="application/json"):
        """
        Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        It is method for POST /api/user/{userId}
        """
        uri = self.client.base_url + "/api/user/"+userId
        return self.client.post(uri, data, headers, query_params, content_type)


    def GetAllViewableUsers(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get all users for which you have at least read access.
        It is method for GET /api/user
        """
        uri = self.client.base_url + "/api/user"
        return self.client.get(uri, None, headers, query_params, content_type)

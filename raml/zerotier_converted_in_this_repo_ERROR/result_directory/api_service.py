class ApiService:
    def __init__(self, client):
        self.client = client



    def POST_api_auth_logout(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Terminate Current Session. Hitting this endpoint causes the user to be logged out. It has no effect when using token authentication, so it's mostly used by the UI.
        It is method for POST /api/auth/_logout
        """
        uri = self.client.base_url + "/api/auth/_logout"
        return self.client.post(uri, data, headers, query_params, content_type)


    def GET_api_network_networkId_member_nodeId(self, nodeId, networkId, headers=None, query_params=None, content_type="application/json"):
        """
        Retrieve a Member
        It is method for GET /api/network/{networkId}/member/{nodeId}
        """
        uri = self.client.base_url + "/api/network/"+networkId+"/member/"+nodeId
        return self.client.get(uri, None, headers, query_params, content_type)


    def POST_api_network_networkId_member_nodeId(self, data, nodeId, networkId, headers=None, query_params=None, content_type="application/json"):
        """
        Update or add a Member. New members can be added to a network by POSTing them.
        It is method for POST /api/network/{networkId}/member/{nodeId}
        """
        uri = self.client.base_url + "/api/network/"+networkId+"/member/"+nodeId
        return self.client.post(uri, data, headers, query_params, content_type)


    def DELETE_api_network_networkId(self, networkId, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a Network. Delete a network and all its related information permanently. Use extreme caution as this cannot be undone!
        It is method for DELETE /api/network/{networkId}
        """
        uri = self.client.base_url + "/api/network/"+networkId
        return self.client.delete(uri, None, headers, query_params, content_type)


    def GET_api_network_networkId(self, networkId, headers=None, query_params=None, content_type="application/json"):
        """
        Retrieve a Network
        It is method for GET /api/network/{networkId}
        """
        uri = self.client.base_url + "/api/network/"+networkId
        return self.client.get(uri, None, headers, query_params, content_type)


    def POST_api_network_networkId(self, data, networkId, headers=None, query_params=None, content_type="application/json"):
        """
        Update or create a Network. Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        New networks can be created by POSTing to `/api/network` with no networkId parameter. The server will create a random unused network ID and return the new network record.
        It is method for POST /api/network/{networkId}
        """
        uri = self.client.base_url + "/api/network/"+networkId
        return self.client.post(uri, data, headers, query_params, content_type)


    def GET_api_network(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get All Viewable Networks. Get all networks for which you have at least read access.
        It is method for GET /api/network
        """
        uri = self.client.base_url + "/api/network"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GET_api_randomToken(self, headers=None, query_params=None, content_type="application/json"):
        """
        Generate a Random Token. This generates a random token suitable for use as an API token server-side using a secure random source. It does not actually modify the user record, just returns the token for use by API callers or the UI.
        It is method for GET /api/randomToken
        """
        uri = self.client.base_url + "/api/randomToken"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GET_api_self(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get Currently Authenticated User. Get the currently authenticated user's user record.
        It is method for GET /api/self
        """
        uri = self.client.base_url + "/api/self"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GET_api_status(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get Status and Configuration Information. Obtain information about this server and/or useful to the Central web UI.
        It is method for GET /api/status
        """
        uri = self.client.base_url + "/api/status"
        return self.client.get(uri, None, headers, query_params, content_type)


    def GET_api_user_userId(self, userId, headers=None, query_params=None, content_type="application/json"):
        """
        Retrieve a User
        It is method for GET /api/user/{userId}
        """
        uri = self.client.base_url + "/api/user/"+userId
        return self.client.get(uri, None, headers, query_params, content_type)


    def POST_api_user_userId(self, data, userId, headers=None, query_params=None, content_type="application/json"):
        """
        Update a User. Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        It is method for POST /api/user/{userId}
        """
        uri = self.client.base_url + "/api/user/"+userId
        return self.client.post(uri, data, headers, query_params, content_type)


    def GET_api_user(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get All Viewable Users. Get all users for which you have at least read access.
        It is method for GET /api/user
        """
        uri = self.client.base_url + "/api/user"
        return self.client.get(uri, None, headers, query_params, content_type)

class NetworkService:
    def __init__(self, client):
        self.client = client



    def deleteNetwork(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete network
        It is method for DELETE /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.delete(uri, None, headers, query_params, content_type)


    def getNetwork(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get network, id=ZeroTier network ID (16 hex digits)
        It is method for GET /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.get(uri, None, headers, query_params, content_type)


    def updateNetwork(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update network
        It is method for POST /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.post(uri, data, headers, query_params, content_type)


    def getMember(self, id, networkid, headers=None, query_params=None, content_type="application/json"):
        """
        Get member, id=10-digit ZeroTier node ID (a.k.a. ZeroTier address)
        It is method for GET /network/{networkid}/member/{id}
        """
        uri = self.client.base_url + "/network/"+networkid+"/member/"+id
        return self.client.get(uri, None, headers, query_params, content_type)


    def updateMember(self, data, id, networkid, headers=None, query_params=None, content_type="application/json"):
        """
        Update member
        It is method for POST /network/{networkid}/member/{id}
        """
        uri = self.client.base_url + "/network/"+networkid+"/member/"+id
        return self.client.post(uri, data, headers, query_params, content_type)


    def network_byNetworkidmember_get(self, networkid, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of members
        It is method for GET /network/{networkid}/member
        """
        uri = self.client.base_url + "/network/"+networkid+"/member"
        return self.client.get(uri, None, headers, query_params, content_type)


    def network_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of networks
        It is method for GET /network
        """
        uri = self.client.base_url + "/network"
        return self.client.get(uri, None, headers, query_params, content_type)

"""
Auto-generated class for ControllerNetworkConfig
"""
from six import string_types

from . import client_support


class ControllerNetworkConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type activeMemberCount: float
        :type authTokens: list[str]
        :type authorizedMemberCount: float
        :type capabilities: list[dict]
        :type creationTime: float
        :type id: str
        :type lastModified: float
        :type multicastLimit: float
        :type name: str
        :type nwid: str
        :type objtype: str
        :type private: bool
        :type revision: float
        :type routes: list[dict]
        :type rules: list[dict]
        :type tags: list[dict]
        :type totalMemberCount: float
        :type v4AssignMode: dict
        :type v6AssignMode: dict
        :rtype: ControllerNetworkConfig
        """

        return ControllerNetworkConfig(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'ControllerNetworkConfig'
        data = json or kwargs

        # set attributes
        data_types = [float]
        self.activeMemberCount = client_support.set_property('activeMemberCount', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.authTokens = client_support.set_property('authTokens', data, data_types, False, [], True, False, class_name)
        data_types = [float]
        self.authorizedMemberCount = client_support.set_property('authorizedMemberCount', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.capabilities = client_support.set_property('capabilities', data, data_types, False, [], True, False, class_name)
        data_types = [float]
        self.creationTime = client_support.set_property('creationTime', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.lastModified = client_support.set_property('lastModified', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.multicastLimit = client_support.set_property('multicastLimit', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.nwid = client_support.set_property('nwid', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.objtype = client_support.set_property('objtype', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.private = client_support.set_property('private', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.revision = client_support.set_property('revision', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.routes = client_support.set_property('routes', data, data_types, False, [], True, False, class_name)
        data_types = [dict]
        self.rules = client_support.set_property('rules', data, data_types, False, [], True, False, class_name)
        data_types = [dict]
        self.tags = client_support.set_property('tags', data, data_types, False, [], True, False, class_name)
        data_types = [float]
        self.totalMemberCount = client_support.set_property('totalMemberCount', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.v4AssignMode = client_support.set_property('v4AssignMode', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.v6AssignMode = client_support.set_property('v6AssignMode', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

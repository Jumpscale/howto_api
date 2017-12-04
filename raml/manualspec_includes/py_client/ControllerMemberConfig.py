"""
Auto-generated class for ControllerMemberConfig
"""
from six import string_types

from . import client_support


class ControllerMemberConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type address: str
        :type authHistory: list[dict]
        :type authorized: bool
        :type capabilities: list[float]
        :type creationTime: float
        :type id: str
        :type identity: str
        :type ipAssignments: list[str]
        :type lastAuthorizedTime: float
        :type lastDeauthorizedTime: float
        :type noAutoAssignIps: bool
        :type nwid: str
        :type objtype: str
        :type physicalAddr: str
        :type revision: float
        :type tags: list[float]
        :rtype: ControllerMemberConfig
        """

        return ControllerMemberConfig(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'ControllerMemberConfig'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.address = client_support.set_property('address', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.authHistory = client_support.set_property('authHistory', data, data_types, False, [], True, False, class_name)
        data_types = [bool]
        self.authorized = client_support.set_property('authorized', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.capabilities = client_support.set_property('capabilities', data, data_types, False, [], True, False, class_name)
        data_types = [float]
        self.creationTime = client_support.set_property('creationTime', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.identity = client_support.set_property('identity', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.ipAssignments = client_support.set_property('ipAssignments', data, data_types, False, [], True, False, class_name)
        data_types = [float]
        self.lastAuthorizedTime = client_support.set_property('lastAuthorizedTime', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.lastDeauthorizedTime = client_support.set_property('lastDeauthorizedTime', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.noAutoAssignIps = client_support.set_property('noAutoAssignIps', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.nwid = client_support.set_property('nwid', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.objtype = client_support.set_property('objtype', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.physicalAddr = client_support.set_property('physicalAddr', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.revision = client_support.set_property('revision', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.tags = client_support.set_property('tags', data, data_types, False, [], True, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

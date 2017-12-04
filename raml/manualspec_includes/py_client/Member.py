"""
Auto-generated class for Member
"""
from .ControllerMemberConfig import ControllerMemberConfig
from six import string_types

from . import client_support


class Member(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type clientVersion: str
        :type clock: float
        :type config: ControllerMemberConfig
        :type controllerId: str
        :type description: str
        :type hidden: bool
        :type id: str
        :type lastOffline: float
        :type lastOnline: float
        :type name: str
        :type networkId: str
        :type nodeId: str
        :type offlineNotifyDelay: float
        :type online: bool
        :type physicalAddress: str
        :type physicalLocation: dict
        :type protocolVersion: float
        :type supportsCircuitTesting: bool
        :type supportsRulesEngine: bool
        :type type: str
        :rtype: Member
        """

        return Member(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Member'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.clientVersion = client_support.set_property('clientVersion', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.clock = client_support.set_property('clock', data, data_types, False, [], False, False, class_name)
        data_types = [ControllerMemberConfig]
        self.config = client_support.set_property('config', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.controllerId = client_support.set_property('controllerId', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.description = client_support.set_property('description', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.hidden = client_support.set_property('hidden', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.lastOffline = client_support.set_property('lastOffline', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.lastOnline = client_support.set_property('lastOnline', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.networkId = client_support.set_property('networkId', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.nodeId = client_support.set_property('nodeId', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.offlineNotifyDelay = client_support.set_property('offlineNotifyDelay', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.online = client_support.set_property('online', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.physicalAddress = client_support.set_property('physicalAddress', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.physicalLocation = client_support.set_property('physicalLocation', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.protocolVersion = client_support.set_property('protocolVersion', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.supportsCircuitTesting = client_support.set_property('supportsCircuitTesting', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.supportsRulesEngine = client_support.set_property('supportsRulesEngine', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.type = client_support.set_property('type', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

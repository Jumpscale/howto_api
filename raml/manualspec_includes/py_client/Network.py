"""
Auto-generated class for Network
"""
from .ControllerNetworkConfig import ControllerNetworkConfig
from .Permissions import Permissions
from six import string_types

from . import client_support


class Network(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type capabilitiesByName: dict
        :type circuitTestEvery: float
        :type clock: float
        :type config: ControllerNetworkConfig
        :type description: str
        :type id: str
        :type onlineMemberCount: float
        :type permissions: Permissions
        :type rulesSource: str
        :type tagsByName: dict
        :type type: str
        :type ui: dict
        :rtype: Network
        """

        return Network(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Network'
        data = json or kwargs

        # set attributes
        data_types = [dict]
        self.capabilitiesByName = client_support.set_property('capabilitiesByName', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.circuitTestEvery = client_support.set_property('circuitTestEvery', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.clock = client_support.set_property('clock', data, data_types, False, [], False, False, class_name)
        data_types = [ControllerNetworkConfig]
        self.config = client_support.set_property('config', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.description = client_support.set_property('description', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.onlineMemberCount = client_support.set_property('onlineMemberCount', data, data_types, False, [], False, False, class_name)
        data_types = [Permissions]
        self.permissions = client_support.set_property('permissions', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.rulesSource = client_support.set_property('rulesSource', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.tagsByName = client_support.set_property('tagsByName', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.type = client_support.set_property('type', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.ui = client_support.set_property('ui', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

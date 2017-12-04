"""
Auto-generated class for Status
"""
from six import string_types

from . import client_support


class Status(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type apiVersion: float
        :type clock: float
        :type clusterNode: str
        :type loginMethods: dict
        :type online: bool
        :type paidPlans: dict
        :type recaptchaSiteKey: str
        :type return_to: str
        :type smsEnabled: bool
        :type stripePublishableKey: str
        :type uptime: float
        :type user: dict
        :type version: str
        :rtype: Status
        """

        return Status(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Status'
        data = json or kwargs

        # set attributes
        data_types = [float]
        self.apiVersion = client_support.set_property('apiVersion', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.clock = client_support.set_property('clock', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.clusterNode = client_support.set_property('clusterNode', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.loginMethods = client_support.set_property('loginMethods', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.online = client_support.set_property('online', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.paidPlans = client_support.set_property('paidPlans', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.recaptchaSiteKey = client_support.set_property('recaptchaSiteKey', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.return_to = client_support.set_property('return_to', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.smsEnabled = client_support.set_property('smsEnabled', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.stripePublishableKey = client_support.set_property('stripePublishableKey', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.uptime = client_support.set_property('uptime', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.user = client_support.set_property('user', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.version = client_support.set_property('version', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

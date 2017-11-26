"""
Auto-generated class for User
"""
from .GlobalPermissions import GlobalPermissions
from .Permissions import Permissions
from six import string_types

from . import client_support


class User(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type auth: dict
        :type clock: float
        :type displayName: str
        :type email: str
        :type globalPermissions: GlobalPermissions
        :type id: str
        :type permissions: Permissions
        :type smsNumber: str
        :type subscriptions: dict
        :type tokens: list[str]
        :type type: str
        :type ui: dict
        :rtype: User
        """

        return User(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'User'
        data = json or kwargs

        # set attributes
        data_types = [dict]
        self.auth = client_support.set_property('auth', data, data_types, False, [], False, False, class_name)
        data_types = [float]
        self.clock = client_support.set_property('clock', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.displayName = client_support.set_property('displayName', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.email = client_support.set_property('email', data, data_types, False, [], False, False, class_name)
        data_types = [GlobalPermissions]
        self.globalPermissions = client_support.set_property('globalPermissions', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [Permissions]
        self.permissions = client_support.set_property('permissions', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.smsNumber = client_support.set_property('smsNumber', data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.subscriptions = client_support.set_property('subscriptions', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.tokens = client_support.set_property('tokens', data, data_types, False, [], True, False, class_name)
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

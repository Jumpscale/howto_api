"""
Auto-generated class for GlobalPermissions
"""

from . import client_support


class GlobalPermissions(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type a: bool
        :type d: bool
        :type m: bool
        :type r: bool
        :rtype: GlobalPermissions
        """

        return GlobalPermissions(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'GlobalPermissions'
        data = json or kwargs

        # set attributes
        data_types = [bool]
        self.a = client_support.set_property('a', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.d = client_support.set_property('d', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.m = client_support.set_property('m', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.r = client_support.set_property('r', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

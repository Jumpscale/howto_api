"""
Auto-generated class for RandomToken
"""
from six import string_types

from . import client_support


class RandomToken(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type clock: float
        :type raw: str
        :type token: str
        :rtype: RandomToken
        """

        return RandomToken(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'RandomToken'
        data = json or kwargs

        # set attributes
        data_types = [float]
        self.clock = client_support.set_property('clock', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.raw = client_support.set_property('raw', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.token = client_support.set_property('token', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

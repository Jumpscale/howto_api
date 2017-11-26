"""
Auto-generated class for Permissions
"""
from .id import id

from . import client_support


class Permissions(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type id: id
        :rtype: Permissions
        """

        return Permissions(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Permissions'
        data = json or kwargs

        # set attributes
        data_types = [id]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

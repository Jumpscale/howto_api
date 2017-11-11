"""
Auto-generated class for Network
"""
from .ControllerNetworkConfig import ControllerNetworkConfig
from .Permissions import Permissions

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
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'capabilitiesByName'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                setattr(self, 'capabilitiesByName', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'circuitTestEvery'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'circuitTestEvery', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'clock'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'clock', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'config'
        val = data.get(property_name)
        if val is not None:
            datatypes = [ControllerNetworkConfig]
            try:
                setattr(self, 'config', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'description'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'description', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'id'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'id', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'onlineMemberCount'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'onlineMemberCount', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'permissions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [Permissions]
            try:
                setattr(self, 'permissions', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'rulesSource'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'rulesSource', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'tagsByName'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                setattr(self, 'tagsByName', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'type'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'type', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ui'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                setattr(self, 'ui', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

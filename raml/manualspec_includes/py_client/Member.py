"""
Auto-generated class for Member
"""
from .ControllerMemberConfig import ControllerMemberConfig

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
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'clientVersion'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'clientVersion', client_support.val_factory(val, datatypes))
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
            datatypes = [ControllerMemberConfig]
            try:
                setattr(self, 'config', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'controllerId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'controllerId', client_support.val_factory(val, datatypes))
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

        property_name = 'hidden'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                setattr(self, 'hidden', client_support.val_factory(val, datatypes))
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

        property_name = 'lastOffline'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'lastOffline', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'lastOnline'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'lastOnline', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'name'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'name', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'networkId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'networkId', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'nodeId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'nodeId', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'offlineNotifyDelay'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'offlineNotifyDelay', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'online'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                setattr(self, 'online', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'physicalAddress'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                setattr(self, 'physicalAddress', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'physicalLocation'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                setattr(self, 'physicalLocation', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'protocolVersion'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                setattr(self, 'protocolVersion', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'supportsCircuitTesting'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                setattr(self, 'supportsCircuitTesting', client_support.val_factory(val, datatypes))
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'supportsRulesEngine'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                setattr(self, 'supportsRulesEngine', client_support.val_factory(val, datatypes))
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

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

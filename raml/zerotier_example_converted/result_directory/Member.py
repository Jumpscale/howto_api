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
    def create(clientVersion=None, clock=None, config=None, controllerId=None, description=None, hidden=None, id=None, lastOffline=None, lastOnline=None, name=None, networkId=None, nodeId=None, offlineNotifyDelay=None, online=None, physicalAddress=None, physicalLocation=None, protocolVersion=None, supportsCircuitTesting=None, supportsRulesEngine=None, type=None):
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

        return Member(
            clientVersion=clientVersion,
            clock=clock,
            config=config,
            controllerId=controllerId,
            description=description,
            hidden=hidden,
            id=id,
            lastOffline=lastOffline,
            lastOnline=lastOnline,
            name=name,
            networkId=networkId,
            nodeId=nodeId,
            offlineNotifyDelay=offlineNotifyDelay,
            online=online,
            physicalAddress=physicalAddress,
            physicalLocation=physicalLocation,
            protocolVersion=protocolVersion,
            supportsCircuitTesting=supportsCircuitTesting,
            supportsRulesEngine=supportsRulesEngine,
            type=type,
        )

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
                self.clientVersion = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'clock'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.clock = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'config'
        val = data.get(property_name)
        if val is not None:
            datatypes = [ControllerMemberConfig]
            try:
                self.config = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'controllerId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.controllerId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'description'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.description = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'hidden'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.hidden = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'id'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.id = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'lastOffline'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.lastOffline = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'lastOnline'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.lastOnline = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'name'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.name = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'networkId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.networkId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'nodeId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.nodeId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'offlineNotifyDelay'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.offlineNotifyDelay = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'online'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.online = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'physicalAddress'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.physicalAddress = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'physicalLocation'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.physicalLocation = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'protocolVersion'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.protocolVersion = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'supportsCircuitTesting'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.supportsCircuitTesting = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'supportsRulesEngine'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.supportsRulesEngine = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'type'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.type = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

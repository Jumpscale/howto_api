"""
Auto-generated class for ControllerMemberConfig
"""

from . import client_support


class ControllerMemberConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(address=None, authHistory=None, authorized=None, capabilities=None, creationTime=None, id=None, identity=None, ipAssignments=None, lastAuthorizedTime=None, lastDeauthorizedTime=None, noAutoAssignIps=None, nwid=None, objtype=None, physicalAddr=None, revision=None, tags=None):
        """
        :type address: str
        :type authHistory: list[dict]
        :type authorized: bool
        :type capabilities: list[float]
        :type creationTime: float
        :type id: str
        :type identity: str
        :type ipAssignments: list[str]
        :type lastAuthorizedTime: float
        :type lastDeauthorizedTime: float
        :type noAutoAssignIps: bool
        :type nwid: str
        :type objtype: str
        :type physicalAddr: str
        :type revision: float
        :type tags: list[float]
        :rtype: ControllerMemberConfig
        """

        return ControllerMemberConfig(
            address=address,
            authHistory=authHistory,
            authorized=authorized,
            capabilities=capabilities,
            creationTime=creationTime,
            id=id,
            identity=identity,
            ipAssignments=ipAssignments,
            lastAuthorizedTime=lastAuthorizedTime,
            lastDeauthorizedTime=lastDeauthorizedTime,
            noAutoAssignIps=noAutoAssignIps,
            nwid=nwid,
            objtype=objtype,
            physicalAddr=physicalAddr,
            revision=revision,
            tags=tags,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'ControllerMemberConfig'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'address'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.address = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'authHistory'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.authHistory = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'authorized'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.authorized = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'capabilities'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.capabilities = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'creationTime'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.creationTime = client_support.val_factory(val, datatypes)
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

        property_name = 'identity'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.identity = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ipAssignments'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.ipAssignments = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'lastAuthorizedTime'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.lastAuthorizedTime = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'lastDeauthorizedTime'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.lastDeauthorizedTime = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'noAutoAssignIps'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.noAutoAssignIps = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'nwid'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.nwid = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'objtype'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.objtype = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'physicalAddr'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.physicalAddr = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'revision'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.revision = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'tags'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.tags = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

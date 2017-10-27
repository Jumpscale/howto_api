"""
Auto-generated class for ControllerNetworkConfig
"""

from . import client_support


class ControllerNetworkConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(activeMemberCount=None, authTokens=None, authorizedMemberCount=None, capabilities=None, creationTime=None, id=None, lastModified=None, multicastLimit=None, name=None, nwid=None, objtype=None, private=None, revision=None, routes=None, rules=None, tags=None, totalMemberCount=None, v4AssignMode=None, v6AssignMode=None):
        """
        :type activeMemberCount: float
        :type authTokens: list[str]
        :type authorizedMemberCount: float
        :type capabilities: list[dict]
        :type creationTime: float
        :type id: str
        :type lastModified: float
        :type multicastLimit: float
        :type name: str
        :type nwid: str
        :type objtype: str
        :type private: bool
        :type revision: float
        :type routes: list[dict]
        :type rules: list[dict]
        :type tags: list[dict]
        :type totalMemberCount: float
        :type v4AssignMode: dict
        :type v6AssignMode: dict
        :rtype: ControllerNetworkConfig
        """

        return ControllerNetworkConfig(
            activeMemberCount=activeMemberCount,
            authTokens=authTokens,
            authorizedMemberCount=authorizedMemberCount,
            capabilities=capabilities,
            creationTime=creationTime,
            id=id,
            lastModified=lastModified,
            multicastLimit=multicastLimit,
            name=name,
            nwid=nwid,
            objtype=objtype,
            private=private,
            revision=revision,
            routes=routes,
            rules=rules,
            tags=tags,
            totalMemberCount=totalMemberCount,
            v4AssignMode=v4AssignMode,
            v6AssignMode=v6AssignMode,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'ControllerNetworkConfig'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'activeMemberCount'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.activeMemberCount = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'authTokens'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.authTokens = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'authorizedMemberCount'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.authorizedMemberCount = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'capabilities'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
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

        property_name = 'lastModified'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.lastModified = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'multicastLimit'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.multicastLimit = client_support.val_factory(val, datatypes)
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

        property_name = 'private'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.private = client_support.val_factory(val, datatypes)
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

        property_name = 'routes'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.routes = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'rules'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.rules = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'tags'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.tags = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'totalMemberCount'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.totalMemberCount = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'v4AssignMode'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.v4AssignMode = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'v6AssignMode'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.v6AssignMode = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

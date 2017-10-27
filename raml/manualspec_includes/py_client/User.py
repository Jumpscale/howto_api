"""
Auto-generated class for User
"""
from .GlobalPermissions import GlobalPermissions
from .Permissions import Permissions

from . import client_support


class User(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(auth=None, clock=None, displayName=None, email=None, globalPermissions=None, id=None, permissions=None, smsNumber=None, subscriptions=None, tokens=None, type=None, ui=None):
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

        return User(
            auth=auth,
            clock=clock,
            displayName=displayName,
            email=email,
            globalPermissions=globalPermissions,
            id=id,
            permissions=permissions,
            smsNumber=smsNumber,
            subscriptions=subscriptions,
            tokens=tokens,
            type=type,
            ui=ui,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'User'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'auth'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.auth = client_support.val_factory(val, datatypes)
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

        property_name = 'displayName'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.displayName = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'email'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.email = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'globalPermissions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [GlobalPermissions]
            try:
                self.globalPermissions = client_support.val_factory(val, datatypes)
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

        property_name = 'permissions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [Permissions]
            try:
                self.permissions = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'smsNumber'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.smsNumber = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'subscriptions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.subscriptions = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'tokens'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.tokens = client_support.list_factory(val, datatypes)
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

        property_name = 'ui'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.ui = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

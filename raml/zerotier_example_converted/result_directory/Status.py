"""
Auto-generated class for Status
"""

from . import client_support


class Status(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(apiVersion=None, clock=None, clusterNode=None, loginMethods=None, online=None, paidPlans=None, recaptchaSiteKey=None, return_to=None, smsEnabled=None, stripePublishableKey=None, uptime=None, user=None, version=None):
        """
        :type apiVersion: float
        :type clock: float
        :type clusterNode: str
        :type loginMethods: dict
        :type online: bool
        :type paidPlans: dict
        :type recaptchaSiteKey: str
        :type return_to: str
        :type smsEnabled: bool
        :type stripePublishableKey: str
        :type uptime: float
        :type user: dict
        :type version: str
        :rtype: Status
        """

        return Status(
            apiVersion=apiVersion,
            clock=clock,
            clusterNode=clusterNode,
            loginMethods=loginMethods,
            online=online,
            paidPlans=paidPlans,
            recaptchaSiteKey=recaptchaSiteKey,
            return_to=return_to,
            smsEnabled=smsEnabled,
            stripePublishableKey=stripePublishableKey,
            uptime=uptime,
            user=user,
            version=version,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Status'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'apiVersion'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.apiVersion = client_support.val_factory(val, datatypes)
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

        property_name = 'clusterNode'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.clusterNode = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'loginMethods'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.loginMethods = client_support.val_factory(val, datatypes)
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

        property_name = 'paidPlans'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.paidPlans = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'recaptchaSiteKey'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.recaptchaSiteKey = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'return_to'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.return_to = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'smsEnabled'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.smsEnabled = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'stripePublishableKey'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.stripePublishableKey = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'uptime'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.uptime = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'user'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.user = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'version'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.version = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

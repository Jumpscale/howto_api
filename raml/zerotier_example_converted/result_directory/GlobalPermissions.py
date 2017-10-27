"""
Auto-generated class for GlobalPermissions
"""

from . import client_support


class GlobalPermissions(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(a=None, d=None, m=None, r=None):
        """
        :type a: bool
        :type d: str
        :type m: bool
        :type r: bool
        :rtype: GlobalPermissions
        """

        return GlobalPermissions(
            a=a,
            d=d,
            m=m,
            r=r,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'GlobalPermissions'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'a'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.a = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'd'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.d = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'm'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.m = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'r'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.r = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

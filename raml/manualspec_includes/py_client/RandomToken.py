"""
Auto-generated class for RandomToken
"""

from . import client_support


class RandomToken(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(clock=None, raw=None, token=None):
        """
        :type clock: float
        :type raw: str
        :type token: str
        :rtype: RandomToken
        """

        return RandomToken(
            clock=clock,
            raw=raw,
            token=token,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'RandomToken'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'clock'
        val = data.get(property_name)
        if val is not None:
            datatypes = [float]
            try:
                self.clock = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'raw'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.raw = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'token'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.token = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

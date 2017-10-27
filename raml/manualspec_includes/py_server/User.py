
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from GlobalPermissions import GlobalPermissions
from Permissions import Permissions
from array import array
from double import double
from object import object
from object import object
from object import object


class User(Form):
    
    auth = FormField(object)
    clock = FormField(double)
    displayName = TextField(validators=[])
    email = TextField(validators=[])
    globalPermissions = FormField(GlobalPermissions)
    id = TextField(validators=[])
    permissions = FormField(Permissions)
    smsNumber = TextField(validators=[])
    subscriptions = FormField(object)
    tokens = FormField(array)
    type = TextField(validators=[])
    ui = FormField(object)

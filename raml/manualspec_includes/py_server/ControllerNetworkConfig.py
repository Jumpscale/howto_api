
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from array import array
from array import array
from array import array
from array import array
from array import array
from double import double
from double import double
from double import double
from double import double
from double import double
from double import double
from double import double
from object import object
from object import object


class ControllerNetworkConfig(Form):
    
    activeMemberCount = FormField(double)
    authTokens = FormField(array)
    authorizedMemberCount = FormField(double)
    capabilities = FormField(array)
    creationTime = FormField(double)
    id = TextField(validators=[])
    lastModified = FormField(double)
    multicastLimit = FormField(double)
    name = TextField(validators=[])
    nwid = TextField(validators=[])
    objtype = TextField(validators=[])
    private = BooleanField(validators=[])
    revision = FormField(double)
    routes = FormField(array)
    rules = FormField(array)
    tags = FormField(array)
    totalMemberCount = FormField(double)
    v4AssignMode = FormField(object)
    v6AssignMode = FormField(object)

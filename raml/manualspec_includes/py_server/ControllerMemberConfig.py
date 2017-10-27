
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from array import array
from array import array
from array import array
from array import array
from double import double
from double import double
from double import double
from double import double


class ControllerMemberConfig(Form):
    
    address = TextField(validators=[])
    authHistory = FormField(array)
    authorized = BooleanField(validators=[])
    capabilities = FormField(array)
    creationTime = FormField(double)
    id = TextField(validators=[])
    identity = TextField(validators=[])
    ipAssignments = FormField(array)
    lastAuthorizedTime = FormField(double)
    lastDeauthorizedTime = FormField(double)
    noAutoAssignIps = BooleanField(validators=[])
    nwid = TextField(validators=[])
    objtype = TextField(validators=[])
    physicalAddr = TextField(validators=[])
    revision = FormField(double)
    tags = FormField(array)

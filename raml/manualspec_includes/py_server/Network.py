
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from ControllerNetworkConfig import ControllerNetworkConfig
from Permissions import Permissions
from double import double
from double import double
from double import double
from object import object
from object import object
from object import object


class Network(Form):
    
    capabilitiesByName = FormField(object)
    circuitTestEvery = FormField(double)
    clock = FormField(double)
    config = FormField(ControllerNetworkConfig)
    description = TextField(validators=[])
    id = TextField(validators=[])
    onlineMemberCount = FormField(double)
    permissions = FormField(Permissions)
    rulesSource = TextField(validators=[])
    tagsByName = FormField(object)
    type = TextField(validators=[])
    ui = FormField(object)

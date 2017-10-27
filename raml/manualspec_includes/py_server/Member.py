
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from ControllerMemberConfig import ControllerMemberConfig
from double import double
from double import double
from double import double
from double import double
from double import double
from object import object


class Member(Form):
    
    clientVersion = TextField(validators=[])
    clock = FormField(double)
    config = FormField(ControllerMemberConfig)
    controllerId = TextField(validators=[])
    description = TextField(validators=[])
    hidden = BooleanField(validators=[])
    id = TextField(validators=[])
    lastOffline = FormField(double)
    lastOnline = FormField(double)
    name = TextField(validators=[])
    networkId = TextField(validators=[])
    nodeId = TextField(validators=[])
    offlineNotifyDelay = FormField(double)
    online = BooleanField(validators=[])
    physicalAddress = TextField(validators=[])
    physicalLocation = FormField(object)
    protocolVersion = FormField(double)
    supportsCircuitTesting = BooleanField(validators=[])
    supportsRulesEngine = BooleanField(validators=[])
    type = TextField(validators=[])


from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from double import double
from double import double
from double import double
from object import object
from object import object
from object import object


class Status(Form):
    
    apiVersion = FormField(double)
    clock = FormField(double)
    clusterNode = TextField(validators=[])
    loginMethods = FormField(object)
    online = BooleanField(validators=[])
    paidPlans = FormField(object)
    recaptchaSiteKey = TextField(validators=[])
    return_to = TextField(validators=[])
    smsEnabled = BooleanField(validators=[])
    stripePublishableKey = TextField(validators=[])
    uptime = FormField(double)
    user = FormField(object)
    version = TextField(validators=[])


from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of



class id(Form):
    
    a = BooleanField(validators=[])
    d = BooleanField(validators=[])
    m = BooleanField(validators=[])
    r = BooleanField(validators=[])
    t = TextField(validators=[])

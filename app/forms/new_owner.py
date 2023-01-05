from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField
from wtforms.validators import ValidationError, DataRequired, Email

def validate_length(form, field):
    # build a custom validator to make sure length is between 1 and 50!
    pass

# build a new owner form!

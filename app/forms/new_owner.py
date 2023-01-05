from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField
from wtforms.validators import ValidationError, DataRequired, Email

def validate_length(form, field):
    if 50 < len(field.data) or len(field.data) < 1:
        raise ValidationError("Length of names must be between 1 and 50 characters")

class NewOwnerForm(FlaskForm):
    first_name = StringField("First Name", [DataRequired(message="Please enter a first name"), validate_length])
    last_name = StringField("Last Name", [DataRequired(message="Please enter a last name"), validate_length])
    email = EmailField("Email address", [DataRequired(message="Please enter an email address"), Email(message="Please enter a valid email address")])
    submit = SubmitField("ADD NEW CAR!")
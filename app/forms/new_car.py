from app import dbfuncs
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired
import datetime

def validate_year(form, field):
    year = datetime.date.today().year + 1
    print(field.data)
    print(year)
    if int(year) < int(field.data) or int(field.data) < 1910:
        raise ValidationError(f"Year must be between 1910 and {year}")

owners = dbfuncs.get_all_owners()
owner_ids = [id for id, name, last, em in owners]

class NewCarForm(FlaskForm):
    manu_year = IntegerField("Manufacture Year", [DataRequired(message="Please enter a year"), validate_year])
    make = StringField("Make", [DataRequired(message="Please enter a make")])
    model = StringField("Model", [DataRequired(message="Please enter a model")])
    owner_id = SelectField("Owner ID", choices=owner_ids)
    submit = SubmitField("ADD NEW CAR!")
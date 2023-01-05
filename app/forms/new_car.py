from app import dbfuncs
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField

import datetime

def validate_year(form, field):
   # add custom validator that makes sure year is between 1910 and 2024
   pass

owners = dbfuncs.get_all_owners()
owner_ids = [id for id, name, last, em in owners]

class NewCarForm(FlaskForm):
    # add validators!
    manu_year = IntegerField("Manufacture Year", )
    make = StringField("Make", )
    model = StringField("Model", )
    owner_id = SelectField("Owner ID", )
    submit = SubmitField("ADD NEW CAR!")
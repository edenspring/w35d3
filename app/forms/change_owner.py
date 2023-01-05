from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, HiddenField
from app import dbfuncs

owners = dbfuncs.get_all_owners()
owner_ids = [id for id, name, last, em in owners]
cars = dbfuncs.get_all_cars()
car_ids = [id for id, man, yr, mod, make in cars]
class ChangeOwner(FlaskForm):
    car_id=SelectField("Car ID", choices=car_ids)
    owner_id = SelectField("Owner ID", choices=owner_ids)
    submit = SubmitField("CHANGE OWNER!")
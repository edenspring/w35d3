from app import dbfuncs
try:
    cars = dbfuncs.get_all_cars()
except:
    dbfuncs.seed()
    
from flask import Flask, redirect
from .config import Configuration
from app.forms import NewCarForm, ChangeOwner


app = Flask(__name__)

app.config.from_object(Configuration)


@app.route('/')
def home():
    info = {
        "title": "CARS CARS CARS",
        "header": "THIS IS THE CARS HOME PAGE!"
    }
    cars = dbfuncs.get_all_cars()
    pass


@app.route('/test')
def test():
    info = {
        "title": "Test page",
        "header": "This is the test page"
    }
    pass


@app.route('/form', methods=('GET', 'POST'))
def form():
    form = NewCarForm()
    if form.validate_on_submit():
        dbfuncs.add_new_car(form.manu_year.data, form.make.data,
                            form.model.data, form.owner_id.data)
        return redirect("/")
    info = {
        "title": "NEW CAR FORM!",
        "header": "ADD A NEW CAR 😎"
    }
    cars = dbfuncs.get_all_cars() 
    owners = dbfuncs.get_all_owners()  
    pass

@app.route("/change-owners",methods=('GET', 'POST'))
def change():
    form = ChangeOwner()
    if form.validate_on_submit():
        dbfuncs.change_car_owner(car_id=form.car_id.data, new_owner_id=form.owner_id.data)
        return redirect("/")
    cars = dbfuncs.get_all_cars()
    owners = dbfuncs.get_all_owners()
    info = {
        "title": "CHANGE OWNER FORM!",
        "header": "CHANGE A CAR'S OWNER 😎"
    }
    pass

from flask import Blueprint, redirect, render_template, session
from app.forms import NewCarForm, ChangeOwner, NewOwnerForm
from app import dbfuncs

app_routes = Blueprint("app", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@app_routes.route('/')
def home():
    if 'home_views' in session:
        session['home_views'] = session['home_views'] + 1
    else:
        session['home_views'] = + 1
    info = {
        "title": "CARS CARS CARS",
        "header": "THIS IS THE CARS HOME PAGE!"
    }
    cars = dbfuncs.get_cars_with_owners()
    owners = dbfuncs.get_all_owners()
    return render_template("page.html", cars=cars, info=info, owners=owners, session=session)


@app_routes.route('/test')
def test():
    info = {
        "title": "Test page",
        "header": "This is the test page"
    }
    return render_template('page.html', info=info)


@app_routes.route('/form', methods=('GET', 'POST'))
def form():
    form = NewCarForm()
    errors = []
    if form.validate_on_submit():
        if 'new_cars' in session:
            session['new_cars'] = session['new_cars'] + 1
        else:
            session['new_cars'] = + 1
        dbfuncs.add_new_car(form.manu_year.data, form.make.data,
                            form.model.data, form.owner_id.data)
        return redirect("/")
    elif len(form.errors) > 0:
        errors = validation_errors_to_error_messages(form.errors)
    info = {
        "title": "NEW CAR FORM!",
        "header": "ADD A NEW CAR 😎"
    }

    cars = dbfuncs.get_cars_with_owners()
    owners = dbfuncs.get_all_owners()
    return render_template("page.html", info=info, cars=cars, owners=owners, form=form, errors=errors)


@app_routes.route("/change-owners", methods=('GET', 'POST'))
def change():
    form = ChangeOwner()
    if form.validate_on_submit():
        if 'cars_traded' in session:
            session['cars_traded'] = session['cars_traded'] + 1
        else:
            session['cars_traded'] = + 1
        dbfuncs.change_car_owner(
            car_id=form.car_id.data, new_owner_id=form.owner_id.data)
        return redirect("/")
    cars = dbfuncs.get_cars_with_owners()
    owners = dbfuncs.get_all_owners()
    info = {
        "title": "CHANGE OWNER FORM!",
        "header": "CHANGE A CAR'S OWNER 😎"
    }
    return render_template("page.html", cars=cars, owners=owners, info=info, owner_form=form)


@app_routes.route("/add-owner", methods=('GET', 'POST'))
def new_owner():
    form = NewOwnerForm()
    errors = []
    if form.validate_on_submit():
        if 'new_owners' in session:
            session['new_owners'] = session['new_owners'] + 1
        else:
            session['new_owners'] = + 1
        dbfuncs.add_new_owner(form.first_name.data,
                              form.last_name.data, form.email.data)
        return redirect("/")
    elif len(form.errors) > 1:
        errors = validation_errors_to_error_messages(form.errors)
    info = {
        "title": "NEW OWNER FORM!",
        "header": "ADD A NEW OWNER 😎"
    }
    cars = dbfuncs.get_cars_with_owners()
    owners = dbfuncs.get_all_owners()
    return render_template("page.html", info=info, cars=cars, owners=owners, new_owner_form=form, errors=errors)

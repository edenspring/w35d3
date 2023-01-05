from app import dbfuncs
try:
    cars = dbfuncs.get_all_cars()
except:
    dbfuncs.seed()
    
from flask import Flask
from .config import Configuration
from app.routes import app_routes


app = Flask(__name__)

app.config.from_object(Configuration)

app.register_blueprint(app_routes, url_prefix="/")


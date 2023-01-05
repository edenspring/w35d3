import os

class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_FILE = os.environ.get("DB_FILE") or "dev.db"
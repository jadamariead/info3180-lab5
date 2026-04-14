import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hjdas9ou^!#haGYU3y89&@(3')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://lab5_user:1nfOl^b$@localhost/lab5').replace('postgres://', 'postgresql://')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
import os

#DEBUG = True
DEBUG = False

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
#USERNAME = 'admin'
#PASSWORD = 'admin'
#WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) # initialize app object
app.config.from_object('config') # link to config file
db = SQLAlchemy(app) # create db variable

from app import views, models
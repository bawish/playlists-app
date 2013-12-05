from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauth import OAuth # HOPE THIS WORKS

app = Flask(__name__) # initialize app object
app.config.from_object('config') # link to config file
db = SQLAlchemy(app) # create db variable
oauth = OAuth() # HOPE THIS WORKS

from app import views, models
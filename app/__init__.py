import os

from flask import Flask
from flask import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__) #create an instance of Flask class
app.config.from_object(Config)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models #from the app folder import the routes.py file
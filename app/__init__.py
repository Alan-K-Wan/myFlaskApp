from flask import Flask

app=Flask(__name__) #create an instance of Flask class

from app import routes #from the app folder import the routes.py file
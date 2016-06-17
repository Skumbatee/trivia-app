#This script runs the application using a development server


#creating flask object
from flask import Flask
from flask_sqlachemy import SQLAlchemy
app=Flask(__name__)

#create database object
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://elsis:elsis@localhost/triviapp'
db=SQLAlchemy(app)

#making the WSGI interface accessible at top level
wsgi_app=app.wsgi_app

#import all of our routes from routes routes.py
from routes import *;

#Launching our server
if __name__ == '__main__':
	import os
	HOST = os.environ.get('SERVER_HOST','localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT','5555'))
	except ValueError:
		PORT = 5555
	app.run(HOST,PORT)

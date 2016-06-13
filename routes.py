from flask import Flask
from app import app

#server/
@app.route('/')
def hello():
	return "Hello Geeks"

# server/question/<title>
@app.route('/question/<title>')
def question(title):
	return '<h2>' + title + '<h2>'

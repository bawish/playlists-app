from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, world!"
	
@app.route('/login')
def login():
	return render_template("login.html")
from flask import render_template
from rdio/rdio_consumer_credentials import *
from app import app

# this MIGHT be a way to initiate the rdio oauth interaction ????
rdio = oauth.remote_app('rdio',
	base_url = 'http://api.rdio.com/1/',
	request_token_url = 'http://api.rdio.com/oauth/request_token',
	access_token_url = ' http://api.rdio.com/oauth/access_token',
	authorize_url = 'https://www.rdio.com/oauth/authorize',
	consumer_key = RDIO_CONSUMER_KEY,
	consumer_secret = RDIO_CONSUMER_SECRET)

@app.route('/')
@app.route('/index')
def index():
	return "Hello, world!"
	
@app.route('/login')
def login():
	return render_template("login.html")
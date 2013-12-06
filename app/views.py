from flask import render_template, g, session, flash, redirect, request, Flask, url_for
from flask_oauth import OAuth
from rdio_consumer_credentials import *
from app import app

oauth = OAuth()

# this MIGHT be a way to initiate the rdio oauth interaction ????
rdio = oauth.remote_app('rdio',
	base_url = 'http://api.rdio.com/1/',
	request_token_url = 'http://api.rdio.com/oauth/request_token',
	access_token_url = ' http://api.rdio.com/oauth/access_token',
	authorize_url = 'https://www.rdio.com/oauth/authorize',
	consumer_key = RDIO_CONSUMER_KEY,
	consumer_secret = RDIO_CONSUMER_SECRET)

# not sure if this is necessary? but it's in the twitter example
@app.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

# this is essential for the handshake for reasons i don't understand
@rdio.tokengetter
def get_rdio_token():
	user = g.user
	if user is not None:
		return user.oauth_token, user.oauth_secret

@app.route('/')
@app.route('/index')
def index():
	return "Hello, world!"
	
@app.route('/login')
def login():
	return rdio.authorize(callback = url_for('oauth_authorized',
		next = request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@rdio.authorized_handler
def oauth_authorized(resp):
	try:
		next_url = request.args.get('next') or url_for('index')
		if resp is None:
			flash(u'You denied the request to sign in.')
			return redirect(next_url)
	except:
		flash(OAuthException.data)
	''' 
	user = User.query.filter_by(name=resp['screen_name']).first()
	
	# user never signed on
	if user is None:
		user = User(resp['screen_name'])
		db_session.add(user)
	
	user.oauth_token = resp['oauth_token']
	user.oauth_secret = resp['oauth_token_secret']
	db_session.commit()
	
	session['user_id'] = user.id
	flash('You were signed in')
	return redirect(next_url)
	'''
	flash(resp)
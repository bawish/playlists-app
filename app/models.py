from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), index = True, unique = True)
	oauth_token = db.Column(String(200))
	oauth_secret = db.Column(String(200))
	
	df __repr__(self):
		return '<User %r>' % (self.email)
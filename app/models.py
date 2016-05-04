from app import db, login_manager
from hashlib import sha1
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String)
    reserved = db.relationship('Reserved', backref='holder', lazy='dynamic')
    waitlist = db.relationship('Waitlist', backref='holder', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = sha1(password.encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

class Reserved(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    telescope = db.Column(db.String(140))
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Reserved %r>' % (self.body)

class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    telescope = db.Column(db.String(140))
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Waitlist %r>' % (self.body)

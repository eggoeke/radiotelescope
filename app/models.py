from app import db, login_manager
from hashlib import sha1
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String)
    reservedAshtarut = db.relationship('ReservedAshtarut', backref='holder', lazy='dynamic')
    reservedAstarte = db.relationship('ReservedAstarte', backref='holder', lazy='dynamic')
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

    def get_username(self):
        try:
            return str(self.username)
        except AttributeError:
            raise NotImplementedError('No `username` attribute - override `get_username`')


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


class ReservedAshtarut(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    starttime = db.Column(db.DateTime, index=True, unique=True)
    endtime = db.Column(db.DateTime, index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Reserved %r>' % (self.time)

    def get_time(self):
        try:
            return str(self.time)
       	except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


class ReservedAstarte(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    starttime = db.Column(db.DateTime, index=True, unique=True)
    endtime = db.Column(db.DateTime, index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Reserved %r>' % (self.time)

    def get_time(self):
        try:
            return str(self.time)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __init__(self, starttime, endtime, user_id):
        self.user_id = current_user.id
        self.starttime = starttime
        self.endtime = endtime



class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    telescope = db.Column(db.String(140))
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Waitlist %r>' % (self.time)

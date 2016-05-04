from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    reserved = db.relationship('Reserved', backref='holder', lazy='dynamic')
    waitlist = db.relationship('Waitlist', backref='holder', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

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

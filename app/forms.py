from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired
from app import db
from .models import User
from hashlib import sha1


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None


    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = db.session.query(User).filter_by(username=self.username.data).first()

        if user:
            self.username.errors.append('Some has already registered with that username')
            return False

        self.user = user
        return True

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = db.session.query(User).filter_by(
            username=self.username.data,
            password=sha1(self.password.data.encode('utf-8')).hexdigest()).first()

        if user is None:
            self.username.errors.append('Unknown user')
            return False

        self.user = user
        return True


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, current_user, logout_user


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'app.login'

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager.init_app(app)


def rendercalendar():
    import calendar 
    c = calendar.HTMLCalendar(calendar.SUNDAY) 
    return c.formatmonth(2017, 1)

from app import views, models

app.jinja_env.globals.update(rendercalendar=rendercalendar)

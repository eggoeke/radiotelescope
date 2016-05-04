from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, current_user, logout_user


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'app.login'

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager.init_app(app)


from app import views, models

from flask import render_template, Flask, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User
from .forms import RegisterForm, LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('index'))

    return render_template('register.html', current_user=current_user, register_form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(url_for('index'))
    return render_template('login.html', current_user=current_user, login_form=form)

@app.route('/calendar')
def calendar():
	date = {'date': 'Today'}
	return render_template('calendar.html',
				title = 'Calendar',
				date = date)
@app.route('/profile')
def profile():
	user = {'nickname': 'Miguel'}
	reserved = [  # fake array of posts
	{ 
            'telescope': 'Ashtarut', 
            'time': '10pm 8th of May' 
	},
	{ 
            'telescope': 'Astarte', 
            'time': '8pm 6th of May' 
	}
	]
	waitlist = [
	{
		'waitlist': 'Soon',
		'holder': {'nickname': 'Mary'},
		'priority': '1',
		'telescope': 'Ashtarut'
	},
	{
                'waitlist': 'less soon',
                'holder': {'nickname': 'Carter'},
                'priority': '1',
		'telescope': 'Astarte'
	}
]
        return render_template('profile.html',
                               	title = 'Profile',
                               	waitlist = waitlist,
				reserved = reserved,
				user = user)


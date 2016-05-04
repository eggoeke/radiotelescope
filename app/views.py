from flask import render_template, Flask, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'don' or request.form['password'] != 'nutmeg':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

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


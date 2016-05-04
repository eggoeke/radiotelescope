from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

from flask import render_template, Flask, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User, ReservedAstarte, ReservedAshtarut, Waitlist, db
from .forms import RegisterForm, LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


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
    if current_user.get_id() != None:
        if (current_user.get_username() == 'don'):
            return render_template('register.html', current_user=current_user, register_form=form)
        else:
            return render_template('permission.html')
    else:
        return render_template('permission.html')
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

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    reservedAshtarut = ReservedAshtarut.query.all();
    reservedAstarte = ReservedAstarte.query.all();
    users = User.query.all();
    if current_user.get_id() != None:
        return render_template('calendar.html',
	    			title = 'Schedule',
                                users = users,
                                reservedAstarte = reservedAstarte,
                                reservedAshtarut = reservedAshtarut)
    else:
        return render_template('permission.html')
@app.route('/profile')
def profile():
    reservedAshtarut = ReservedAshtarut.query.all();
    reservedAstarte = ReservedAstarte.query.all();
    waitlist = Waitlist.query.all();

    if current_user.get_id() != None:
        return render_template('profile.html',
                              	title = 'Profile',
                               	waitlist = waitlist,
				reservedAshtarut = reservedAshtarut,
                                reservedAstarte = reservedAstarte)
    else:
        return render_template('permission.html')


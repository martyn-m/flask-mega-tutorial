from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    # define some dummy data for testing until we set up a proper datasource
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Its too late to be doing this carp!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'What the hell is going on, where are my pants?'
        },
        {
            'author': {'username': 'Martyn'},
            'body': 'Who are you people, what am I doing here?'
        }
    ]
    return render_template('index.html', title='Home Page', posts=posts)

# enable POST method for this view to recieve submitted forms (default is GET only)
@app.route('/login', methods=['GET', 'POST']) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): # returns false if no form was submitted or data validation failed
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next') # get the redirect arg added by @login_required
        # check if there was a next request, and if so was it relative (OK), or absolute (bad)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
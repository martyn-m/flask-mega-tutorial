from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # define some dummy data for testing until we set up a proper datasource
    user = {'username': 'Martyn'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

# enable POST method for this view to recieve submitted forms (default is GET only)
@app.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit(): # returns false if no form was submitted or data validation failed
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Look for most config values in the environment variables, use defaults if not present

    # Key for Flask-WTF forms for CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CorrectHorseBatteryStaple'

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
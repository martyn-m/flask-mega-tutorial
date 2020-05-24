import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Look for most config values in the environment variables, use defaults if not present

    # Key for Flask-WTF forms for CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CorrectHorseBatteryStaple'

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email error handler
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['martyn.myers@gmail.com']
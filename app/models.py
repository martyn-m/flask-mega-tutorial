# defines the app database schema
from app import db

# Classes represent a table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unqiue=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # The __repr__ method defines how instances of this class are printed
    def __repr__(self):
        return '<User {}>'.format(self.username)

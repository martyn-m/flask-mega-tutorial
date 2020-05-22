from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    # return the error page template and a response code 404 (not found)
    # for normal views where not specified the default response code 200 (OK) is used
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    # rollback any uncommitted db transactions in case it's a db error
    db.session.rollback()
    return render_template('500.html'), 500
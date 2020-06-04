from flask import render_template
from app import db
from app.errors import bp # import the module blueprint

@bp.app_errorhandler(404) # use the blueprints app decorator rather than the apps for portability
def not_found_error(error):
    # return the error page template and a response code 404 (not found)
    # for normal views where not specified the default response code 200 (OK) is used
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    # rollback any uncommitted db transactions in case it's a db error
    db.session.rollback()
    return render_template('errors/500.html'), 500
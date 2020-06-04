from flask import Blueprint

bp = Blueprint('errors', __name__)

# I'm at the bottom to avoid circular dependencies
from app.errors import handlers
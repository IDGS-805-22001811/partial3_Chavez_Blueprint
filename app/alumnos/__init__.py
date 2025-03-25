from flask import Blueprint

alumnos_bp = Blueprint('alumnos', __name__, template_folder='templates')

from . import routes  # Esta línea debe estar al final
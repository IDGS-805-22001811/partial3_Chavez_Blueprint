from flask import Blueprint

# Crea el blueprint aquí directamente
examenes_bp = Blueprint('examenes', __name__, template_folder='templates')

# Importa las rutas después de crear el blueprint
from . import routes
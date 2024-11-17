from flask import Blueprint, render_template 
# Crear un Blueprint 
perros = Blueprint('perros', __name__, url_prefix='/perros')
# Definir rutas y vistas dentro del Blueprint 
@perros.route('/l') 
def login(): 
    return 'Manada de perros'

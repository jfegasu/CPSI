# imports
from flask import Blueprint, jsonify, request, abort,redirect, url_for
from flask import render_template
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

centros = Blueprint('centros', __name__, url_prefix='/centro',
                        template_folder='templates')
@centros.route('/l', methods=['GET'])
def new_ppal():
    return "Centros de Formacion"
from flask import Blueprint, jsonify, request, abort,redirect, url_for
from flask import render_template
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

sede = Blueprint('sede', __name__, url_prefix='/sede',
                        template_folder='templates')
@sede.route('/l', methods=['GET'])
def new_ppal():
    return "sedes del centro de formacion"
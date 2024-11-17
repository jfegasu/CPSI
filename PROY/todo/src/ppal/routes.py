# imports
from flask import Blueprint, jsonify, request, abort,redirect, url_for
from flask import render_template
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

ppal = Blueprint('ppal', __name__, url_prefix='/ppl',
                        template_folder='templates')

# If user exist
def existing_regin(ppal):
    return 'Existe'

@ppal.route('/l', methods=['GET'])
def new_ppal():
    return render_template("uno.html",N=0)

@ppal.route('/')
def show():
    return render_template("uno.html",N=0)
@ppal.route("/h",methods=["GET"])
def nivel():
    return render_template("acerca.html",N=1000)

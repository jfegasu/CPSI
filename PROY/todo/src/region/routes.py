from flask import Blueprint, jsonify, request, abort,redirect, url_for
from flask import render_template
from datetime import datetime, timedelta # for the user registration time
import hashlib # to make a hash of the user's password (strongly recommended)

region = Blueprint('region', __name__, url_prefix='/reg',
                        template_folder='templates')
@region.route('/l', methods=['GET'])
def new_ppal():
    return render_template("region.html",N=0)
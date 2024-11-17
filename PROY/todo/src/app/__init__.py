# imports
from flask import Flask
from flask_cors import CORS

# Here we're gonna import the blueprints
from ppal.routes import ppal
from region.routes import region
from centros.routes import centros
from sede.routes import sede


# function than create a flask app with CORS
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Here we're gonna register the blueprints
    app.register_blueprint(ppal)
    app.register_blueprint(region)
    app.register_blueprint(centros)
    app.register_blueprint(sede)


    return app
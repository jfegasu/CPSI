from flask import Flask 
from flask_cors import CORS
from PERROS.routes import perros 
# importar el Blueprint 
# Crear la aplicación Flask 
app = Flask(__name__) 

# Registrar el Blueprint en la aplicación 
app.register_blueprint(perros)

if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')

from flask import Flask, jsonify,request,session,redirect,render_template,url_for
import json
# https://jwt.io/#debugger-io
# pip install Flask PyJWT Flask-JWT-Extended

from models import *
from databases import *
from peewee import  DoesNotExist
import jwt
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

class validacion:
    @classmethod
    def Valide(pal):
        jwt.decode(pal, "secret", algorithms=["HS256"])  

app=Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mi_clave_secreta"
jwt = JWTManager(app)
# Ruta para iniciar sesión (autenticación)
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del usuario
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    # Aquí normalmente validarías las credenciales en la base de datos
    if username != "admin" or password != "1234":
        return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401
    
    # Crear un token de acceso para el usuario
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
    
@app.route("/")
def Raiz():
 return "<center><h1>CONDOMINIOS PALMANOVA SINSONTE<br>VILLETA CUNDINAMARCA<h1>"
@app.route("/t")
def ListaUnidad():
    unidades = Unidad.select()
    resultado = []
    for unidad in unidades:
        resultado.append({
            "idunidad": unidad.idunidad,
            "nomunidad": unidad.nomunidad
        })
    return json.dumps(resultado)

# Consultar una unidad por ID
@app.route("/t/<int:id>")
def ListaUnaUnidad(id):
    unidad = Unidad.get(Unidad.idunidad == id)
    resultado = {
        "idunidad": unidad.idunidad,
        "nomunidad": unidad.nomunidad
    }
    return json.dumps(resultado)

# Eliminar una unidad por ID
@app.route("/t/d/<int:id>", methods=['DELETE'])
def EliminaUnidad(id):
    unidad = Unidad.get(Unidad.idunidad == id)
    unidad.delete_instance()
    return "200"

# Insertar una nueva unidad
@app.route("/t/i", methods=['POST'])
def InsertaUnidad():
    datos = request.get_json()
    nom = datos.get('nombre')
    try:
        Unidad.create(nomunidad=nom)
    except Exception as e:
        return f"Database error: {e}", 500
    return "200"

# Actualizar una unidad por ID
@app.route("/t/u", methods=['PUT'])
def ActualizaUnaUnidad():
    datos = request.get_json()
    id = datos['id']
    nom = datos['nombre']
    try:
        unidad = Unidad.get(Unidad.idunidad == id)
        unidad.nomunidad = nom
        unidad.save()
    except Exception as e:
        return f"Database error: {e}", 500
    return "200"
from flask import Flask, jsonify
from models import Apartamento  # Import the Apartamento model

@app.route("/a")
def ListaApartamentos():
    apartamentos = Apartamento.select()  # Query to get all apartments
    
    resultado = []
    
    if apartamentos:  # Ensure there are results before iterating
        for apartamento in apartamentos:
            # Create a dictionary for each apartment
            resultado.append({
                "idapartamento": apartamento.idapartamento,  # Correct field name
                "nomapto": apartamento.nomapto,
                "idunidad": apartamento.unidad_id,
                "observacion":apartamento.observacion,
                "celular":apartamento.celular,
                "contacto":apartamento.contacto,
                "correo":apartamento.correo,
            })
    else:
        return jsonify({"error": "No apartments found"}), 404  # Return a 404 if no apartments are found
    
    return json.dumps(resultado)

# Consultar apartamentos por ID de unidad
@app.route("/a/<int:id>")
def ListaAptos(id):
    apartamento = Apartamento.get(Apartamento.idapartamento == id)
    resultado = []
    resultado.append({
                "idapartamento": apartamento.idapartamento,  
                "nomapto": apartamento.nomapto,
                "idunidad": apartamento.unidad_id,
                "observacion":apartamento.observacion,
                "celular":apartamento.celular,
                "contacto":apartamento.contacto,
                "correo":apartamento.correo,
        })
    return json.dumps(resultado)
@app.route("/a/i", methods=['POST'])
def InsertaApto():
    datos = request.get_json()
    nomapto = datos.get('nomapto')
    unidad_id = datos.get('unidad_id')
    observacion = datos.get('observacion')
    celular = datos.get('celular')
    contacto = datos.get('contacto')
    correo = datos.get('correo')
    try:
        apartamento = Apartamento.create(
            nomapto=nomapto,
            unidad_id=unidad_id,  
            observacion=observacion,
            celular=celular,
            contacto=contacto,
            correo=correo
        )
    except Exception as e:
        return f"Database error: {e}", 500
    return "200"

@app.route("/a/d/<int:id>", methods=['DELETE'])
def EliminaApto(id):
    apartamento = Apartamento.get(Apartamento.idapartamento == id)
    apartamento.delete_instance()
    return "200"


@app.route("/a/u", methods=['PUT'])
def ActualizaUnApto():
    try:
        # Get the JSON data sent in the request body
        datos = request.get_json()

        # Extract data from the JSON
        id = datos['idapartamento']
        nomapto = datos.get('nomapto')
        unidad_id = datos.get('unidad_id')
        observacion = datos.get('observacion')
        celular = datos.get('celular')
        contacto = datos.get('contacto')
        correo = datos.get('correo')

        # Find the apartamento by ID
        apartamento = Apartamento.get(Apartamento.idapartamento == id)

        # Check if the Unidad exists before assigning it
        try:
            unidad = Unidad.get(Unidad.idunidad == unidad_id)  # Verify that the Unidad exists
        except DoesNotExist:
            return jsonify({"error": "Unidad not found"}), 404

        # Update the fields
        apartamento.nomapto = nomapto
        apartamento.unidad_id = unidad_id  # Assign the full Unidad object, not just the ID
        apartamento.observacion = observacion
        apartamento.celular = celular
        apartamento.contacto = contacto
        apartamento.correo = correo

        # Save the updated apartment record
        apartamento.save()

        # Return a success response with status code 200
        return jsonify({"message": "Apartamento Actualizado correctamente", "idapartamento": apartamento.idapartamento}), 200

    except DoesNotExist:
        return jsonify({"error": "Apartamento no existe"}), 404  # Return 404 if the apartment doesn't exist
    except Exception as e:
        # If an error occurs, return a 500 error with the error message
        return jsonify({"error": f"Database error: {str(e)}"}), 500
@app.route("/c")
def ListaAutomotor():
    automotores = Automotor.select()  # Query to get all apartments
    
    resultado = []
    
    if automotores:  # Ensure there are results before iterating
        for automotore in automotores:
            # Create a dictionary for each apartment
            resultado.append({
                "idautomotor": automotore.idautomotor,  # Correct field name
                "apartamento_id": automotore.apartamento_id,
                "placa":automotore.placa,
                "tipo":automotore.tipo
                
            })
    else:
        return jsonify({"error": "No hay apartmentos "}), 404  # Return a 404 if no apartments are found
    
    return json.dumps(resultado)

@app.route("/c/<int:id>")
def ListaAutos(id):
    automotore = Automotor.get(Automotor.idautomotor == id)
    resultado = []
    resultado.append({
                "idautomotor": automotore.idautomotor,  # Correct field name
                "apartamento_id": automotore.apartamento_id,
                "placa":automotore.placa,
                "tipo":automotore.tipo,
        })
    return json.dumps(resultado)

@app.route("/c/i", methods=['POST'])
def InsertaAuto():
    datos = request.get_json()
    auto_id = datos.get('placa')
    vtipo = datos.get('tipo')
    apartamento_id = datos.get('apartamento_id')
    try:
        Auto = Automotor.create(
            placa=auto_id,
            tipo=vtipo,
            apartamento_id=apartamento_id,
            FECHA=dt.datetime.now()
            
        )
    except Exception as e:
        print(f"Database error: {e}")
        return f"Database error: {e}", 500
    return "200"
@app.route("/in", methods=['POST'])
def InsertaIngresa():
    datos = request.get_json()
    auto_id = datos.get('automotor_id')
    vtipo = datos.get('tipo')
    try:
        Auto = Ingresos.create(
            automotor_id=auto_id,
            tipo=vtipo,
            FECHA=dt.datetime.now()
            
        )
    except Exception as e:
        print(f"Database error: {e}")
        return f"Database error: {e}", 500
    return "200"
@app.route("/lin")
def ListaIngresos():
    ingresos = Ingresos.select()  # Query to get all apartments
    
    resultado = []
    
    if ingresos:  # Ensure there are results before iterating
        for ingreso in ingresos:
            # Create a dictionary for each apartment
            resultado.append(
                {
                    "idingreso":ingreso.idingreso,
                    "automotor_id":ingreso.automotor_id,
                    "tipo":ingreso.tipo,
                    "FECHA":str(ingreso.FECHA)
                }
            )
    else:
        return jsonify({"error": "No hay apartmentos "}), 404  # Return a 404 if no apartments are found
    
    return json.dumps(resultado)

if __name__ == '__main__':
    DATABASE.connect()  # Conectar a la base de datos
    app.run(debug=True, port=8000, host='0.0.0.0')



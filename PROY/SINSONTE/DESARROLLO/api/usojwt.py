from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Crear la aplicación Flask
app = Flask(__name__)

# Clave secreta para firmar los JWT
app.config["JWT_SECRET_KEY"] = "mi_clave_secreta"  # Cambia esto por una clave más segura

# Inicializar el JWTManager
jwt = JWTManager(app)

# Ruta pública para probar
@app.route('/publico', methods=['GET'])
def publico():
    return jsonify(message="Este es un recurso público")

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

# Ruta protegida por JWT
@app.route('/protegida', methods=['GET'])
@jwt_required()
def protegida():
    # Obtener la identidad del usuario desde el JWT
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)

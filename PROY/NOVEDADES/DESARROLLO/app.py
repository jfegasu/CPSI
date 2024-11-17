from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS
import json

def create_app():
    app=Flask(__name__)
    CORS(app)
    return app
app = create_app() # CREATE THE FLASK APP
app.ruta="http://127.0.0.1:8000/"

class Usuario:
    
    res=None
    data=None
    def __init__(self):
        self.url=app.ruta
        print("---->",app.ruta)


    def ListarTodos(self,clave="/ln"):
        
        self.res=requests.get(self.url+clave)
        data1=json.loads(self.res.content)
        return data1
    
    def ListarUno_a(self,cual):    
        self.res=requests.get(self.url+"/ppa/"+str(cual))
        data1=json.loads(self.res.content)
        if data1!=[]:
            return(data1)
        else:
            return False  
    def ListarJson(self,clave):    
        self.res=requests.get(self.url+clave)
        data1=json.loads(self.res.content)
        if data1!=[]:
            return(data1)
        else:
            return False  
    def Inserte(self,data,clave="/i"):
        print(self.url+clave)
        response = requests.post(self.url+clave, json=data)
    def Borra(self,cual,clave):
        response = requests.delete(self.url+clave+str(cual))
    def Actualiza(self,data,clave="/u"):
        response = requests.put(self.url+clave, json=data)


@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/menu")
def menu():
    return render_template("menu.html")
@app.route("/banner")
def banner():
    return render_template("banner.html")
@app.route("/centro")
def centro():
    return render_template("centro.html")
@app.route("/footer")
def footer():
    return render_template("footer.html")
@app.route("/novedada")
def novedada():
    u1=Usuario()
    cadena=u1.ListarJson("/ln/a/1")
    llenos=1
    msg="NOVEDADES ABIERTAS"
    if cadena==False:
        return render_template("novedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("novedades.html",cadena=cadena,hay=1,msg=msg)
@app.route("/novedadp")
def novedadp():
    u1=Usuario()
    cadena=u1.ListarJson("/ln/p/1")
    msg="NOVEDADES EN PROCESO"
    
    if cadena==False:
        return render_template("novedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("novedades.html",cadena=cadena,hay=1,msg=msg)
@app.route("/lr/l/<id>")
def lnovedadp(id):
    
    u1=Usuario()
    cadena=u1.ListarJson("/ln/l/"+id)
    
    msg="TRAMITES REALIZADAS DE LA NOVEDAD"
    

    if cadena==False:
        return render_template("lnovedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("lnovedades.html",cadena=cadena,hay=1,msg=msg)

@app.route("/novedadc")
def novedadc():
    u1=Usuario()
    cadena=u1.ListarJson("/ln/c/1")
    llenos=1
    msg="NOVEDADES CERRADAS"
    
    if cadena==False:
        return render_template("novedades.html",cadena=cadena,hay=0,msg=msg)
    return render_template("novedades.html",cadena=cadena,hay=1,msg=msg)

@app.route("/r/<amb>")
def resumen(amb):
    u1=Usuario()
    cadena=u1.ListarJson("/e/1")
    llenos=1
    msg="RESUMEN EQUIPAMIENTO DEL AMBIENTE"
    if cadena==False:
        return render_template("resumen.html",cadena=cadena,hay=0,msg=msg)
    return render_template("resumen.html",cadena=cadena,hay=1,msg=msg)

@app.route("/r/a/<amb>")
def equipamiento(amb):
    u1=Usuario()
    cadena=u1.ListarJson("/e/a/1")
    llenos=1
    msg=" EQUIPAMIENTO DEL AMBIENTE"
    
    if cadena==False:
        return render_template("equipamiento.html",cadena=cadena,hay=0,msg=msg)
    return render_template("equipamiento.html",cadena=cadena,hay=1,msg=msg)
@app.route("/res/<nov>")
def respuestanov(nov):
    u1=Usuario()
    cadena=u1.ListarJson("/n/"+nov)
    llenos=1
    msg=" RESPUESTA A NOVEDAD"
    
    if cadena==False:
        return render_template("novprocesa.html",cadena=cadena,msg=msg)
    return render_template("novprocesa.html",cadena=cadena,msg=msg)
    return render_template("novprocesa.html",cadena=cadena,msg=msg)
@app.route("/n/i",methods=['POST'])
def salvarespuestanov():
    # u1=Usuario()
    # cadena=u1.ListarJson("/n/"+nov)
    # llenos=1
    idN=request.form.get("NOVEDADES")
    idA=request.form.get("AMBIENTE")
    estado=request.form.get("ESTADO")
    cuentadante=request.form.get("CUENTADANTE")
    respuesta=request.form.get("respuesta").upper()
    descri1=request.form.get("DESCRI1").upper()
    if estado==0:
        estado=1
    else:
        estado=1
    
    
    datos={
            "idAMBIENTE":idA,
            "idNOVEDADES":idN,
            "DESCRIPCION":respuesta,
            "ESTADO":estado,
            "PADRE":idA,
            "DESCRI1":descri1
        }
    print(datos)
    
    response = requests.post(app.ruta+"n/i", json=datos)
    # response = requests.post("/usua/i", json=datos)
    msg=" RESPUESTA A LA NOVEDAD GRABADA CORRECTAMENTE..."
    
    # if cadena==False:
    #     return render_template("alertas.html",msg=msg)
    return render_template("alertas.html",msgito=msg,regreso="/centro")
@app.route("/n/d",methods=['POST','GET'])
def cierrarespuestanov():
    # u1=Usuario()
    # cadena=u1.ListarJson("/n/"+nov)
    # llenos=1
    idN=request.form.get("NOVEDADES")
    idA=request.form.get("AMBIENTE")
    estado=request.form.get("ESTADO")
    cuentadante=request.form.get("CUENTADANTE")
    respuesta=request.form.get("respuesta").upper()
    if estado==0:
        estado=1
    else:
        estado=1
    
    
    datos={
            "idAMBIENTE":idA,
            "idNOVEDADES":idN,
            "DESCRPCION":respuesta,
            "ESTADO":estado,
            "PADRE":idA
        }
    print(datos)
    
    response = requests.post("http://127.0.0.1:8000/n/d", json=datos)
    # response = requests.post("/usua/i", json=datos)
    msg=" LA NOVEDAD CERRADA CORRECTAMENTE..."
    
    # if cadena==False:
    #     return render_template("alertas.html",msg=msg)
    return render_template("alertas.html",msgito=msg,regreso="/centro")



if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=5000)
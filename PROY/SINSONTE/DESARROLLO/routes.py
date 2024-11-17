
from flask import Flask,render_template,request,redirect
import requests
from flask_cors import CORS
from api.apicnx import *
from api.config import configura
def create_app():
    app=Flask(__name__)
    CORS(app)
    return app

app = create_app() # CREATE THE FLASK APP
@app.route("/")
def inicio():
    return render_template("otro.html")
@app.route("/logo")
def inilogocio():
    return render_template("banner.html")
@app.route("/logo1")
def inilogocio1():
    return render_template("banner1.html")
@app.route("/menu")
def menup():
    return render_template("menu.html")
@app.route("/unidad")
def Unidad():
    u1=Usuario()
    cadena=u1.ListarJson("/t")
    print(cadena)
    if cadena==None:
        cadena=[]
        v=0
    else:
        v=1
    N=0
    if cadena==None:
        return render_template("unidad.html",N=N,url=configura['PUERTOREST'],V=v)
    else:
        return render_template("unidad.html",N=N,url=configura['PUERTOREST'],cadena=list(cadena),V=v)
        
@app.route("/u/d/<id>")
def BorraUnidad3(id):
    print("*****>",id)
    N=3
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'],ID=id)
@app.route("/u/d31",methods=["POST","DELETE"])
def BorraUnidad31():
    N=31
    u1=Usuario()
    id=request.form['idu']
    u1.BorraAPI(id,'/t/d/')
    
    cadena=u1.ListarJson("/t")
    if cadena==None:
        cadena=[]
        v=0
    else:
        v=1
    return render_template("unidad.html",N=N,url=configura['PUERTOREST'],cadena=cadena,V=v,msg="Borrado")
@app.route("/u/i")
def NuevaUnidad():
    N=1   
    return render_template("unidad.html",N=N)
@app.route("/u/ii",methods=["POST"])
def SalvaNuevaUnidad():
    N=11
    nom=request.form.get('nomunidad')
    datos={
        "nombre":nom.upper()
    }
    u1=Usuario()
    u1.InserteAPI(datos,'/t/i')
    return  render_template("unidad.html",N=N)
    # response = requests.post("/t/i", json=datos)
    # return render_template("unidad.html",N=N)
    # return "200"
@app.route("/u/u/<id>")
def ActualizaUnidad(id):
    N=2 
    u1=Usuario()  
    cadena=u1.ListarJson("/t/"+str(id))
    return render_template("unidad.html",N=N,id=id,cadena=cadena)
@app.route("/u/uu",methods=['POST'])
def GuardaUnidad():
    id=request.form.get('idunidad')
    nom=request.form.get('nomunidad')
    datos={
        "id":id,
        "nombre":nom.upper()
    }
    N=21 
    u1=Usuario()  
    cadena=u1.ActualizaAPI(datos,"/t/u")
    return render_template("unidad.html",N=N)

@app.route("/ap/<id>")
def ListarAptos(id):
    u1=Usuario()
    cadena=u1.ListarJson("/a/"+str(id))

    N=0
    if cadena==None:
        cadena=[]
        v=0
    else:
        v=1

    if cadena==None:
        return render_template("aptos.html",N=N,url=configura['PUERTOREST'],V=v)
    else:
        return render_template("aptos.html",N=N,url=configura['PUERTOREST'],cadena=list(cadena),V=v)
    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
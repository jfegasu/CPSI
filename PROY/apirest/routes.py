from flask import Flask, jsonify,request,redirect, url_for,session
import json,requests
from flask import render_template
from services.apicnx import *   
from config import configura 

app=Flask(__name__)
app.secret_key="*a6#45$bb"   
#session['bd']=configura['DB']
@app.route("/niveles/i",methods=["POST"])
def creausuario():
    try:
        nom=request.form.get('nom')
        ape=request.form.get('ape')
        
        datos={
            "NOMBRE":nom.upper(),
            "APELLIDO":ape.upper()
        }
        response = requests.post(configura['SERVER_API']+"/usua/i", json=datos)
        id=0
        msgitos="Centro editado satisfactoriamente"
    except Exception as e:
        msgitos="** Error"+response
    return render_template("alertas.html",msgito=msgitos)


@app.route("/niveles/u",methods=["POST"])
def nivelactualiza():
    try:
        id=request.form.get('id')
        nom=request.form.get('nom')
        ape=request.form.get('ape')
        
        datos={
        "IDUSUARIO":id,"NOMBRE":nom.upper(),"APELLIDO":ape.upper()
        }
        response = requests.put(configura['SERVER_API']+"/usua/u", json=datos)
        id=0
        msgitos="Usuario editado satisfactoriamente"
    except Exception as e:
        msgitos="** Error"+response
    return render_template("alertas.html",msgito=msgitos)


@app.route("/niveles/e/<id>",methods=["GET"])
def nivelEdita(id):
    u1= Usuario()
    cadena=u1.ListarUno_a(id)
    return render_template("EditarUsuario.html",cadena=cadena)
    
@app.route("/niveles/d/<id>",methods=["POST"])
def nivelBorra(id):
    BorraAPI(id,"/usua/d/")
    msgitos="Usuario borrado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos,regresa="/niveles/l")


@app.route("/",methods=["GET"])
@app.route("/ppa",methods=["GET"])
def Lista():
    u1= Usuario()
    cadena=u1.ListarJson("/ppa/menus")
    return render_template("index.html",cadena=cadena)
    

@app.route("/niveles/l",methods=["GET"])
def ListarTodos():
    u1= Usuario()
    cadena=list(u1.ListarJson("/ppa/l"))
    can=len(cadena)
    id=0
    return render_template("pusuarios.html",N=0,cadena=cadena)
@app.route("/centros",methods=["GET"])
def ListarCentros():
    #cadena = requests.get(configura['SERVER_API']+"/ppa/centros")    
    u1= Usuario()
    cadena=u1.ListarJson("/ppa/centros")
    return render_template("pcentros.html",cadena=cadena)
@app.route("/centros/e/<id>",methods=["GET"])
def nivelEditaCentros(id):
    u1= Usuario()
    cadena=u1.ListarJson("/ppa/centros/"+str(id))
    return render_template("editarCentros.html",cadena=cadena)
    
@app.route("/centros/u",methods=["POST"])
def centroactualiza():
    try:
        id=request.form.get('id')
        nom=request.form.get('nom')
        
        datos={
            "IDUSUARIO":id,"NOMBRE":nom.upper()
        }
        response = requests.put(configura['SERVER_API']+"/ppa/centros/u", json=datos)
        id=0
        msgitos="Centro editado satisfactoriamente"
    except Exception as e:
        msgitos="** Error"+response
    return render_template("alertas.html",msgito=msgitos,regreso="/centros")

@app.route("/centro/d/<id>",methods=["POST"])
def BorraCentros(id):
    
    #response = requests.delete(configura['SERVER_API']+"/usua/d/"+id)
    BorraAPI(id,"/ppa/centros/d/")
    msgitos="Centro borrado satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos)

@app.route("/niveles/1000",methods=["GET"])
def acerca():
    #pyautogui.confirm(text="Mensaje",title="xxxx",buttons=["OK","CANCEL"])
    return render_template("acerca.html")
@app.route("/sedes/<N>/<id>",methods=["GET","POST"])
def ListaSedes(N,id):
    centros0=ListarJson("/ppa/centros/0")
    centros=ListarJson("/ppa/centros/"+id)
    
    if N=="2":
        sedes=ListarJson("/ppa/sedes/e/"+id)
    else:
        sedes=ListarJson("/ppa/sedes/"+id)
    
    
    


 
    return render_template("psedes.html",centros=centros,sedes=sedes,N=N,centros0=centros0)
@app.route("/sedes/u",methods=["GET","POST"])
def EditaSedes():
    try:
        id=request.form.get('idsede')
        nom=request.form.get('nom')
        
        datos={
            "IDSEDE":id,"NOMBRE":nom.upper()
        }
        ActualizaAPI(datos,"/ppa/sedes/u")
        # response = requests.put(configura['SERVER_API']+"/ppa/sedes/u", json=datos)
        
        msgitos="Sede editada satisfactoriamente"
    except Exception as e:
        msgitos="** Error"+response
    return render_template("alertas.html",msgito=msgitos,regreso="/sedes/0/0")
@app.route("/sedes/i",methods=["GET","POST"])
def CreaSedes():
    
    id=request.form.get('idcentro')
    nom=request.form.get('nom')
    
    datos={
        "IDCENTRO":id,"NOMBRE":nom
    }
    print("++++++++>",datos)
    InserteAPI(datos,"/ppa/sedes/i")
    # response = requests.post(configura['SERVER_API']+"/ppa/sedes/i", json=datos)
    msgitos="Sede Creada satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos,regreso="/sedes/0/0")
@app.route("/sedes/d/<id>",methods=["POST"])
def BorraSede(id):
    
    BorraAPI(id,"/ppa/sedes/d/")
    # response = requests.delete(configura['SERVER_API']+"/ppa/sedes/d/"+id)
    
    msgitos="Sede borrada satisfactoriamente"
    return render_template("alertas.html",msgito=msgitos,regreso="/sedes/0/0")

@app.route("/Aulas/<N>/<id>",methods=["GET","POST"])
def ListaAulas(N,id):
    centros0=ListarJson("/ppa/centros/0")
    centros=ListarJson("/ppa/centros/"+id)
    
    if N=="2":
        sedes=ListarJson("/ppa/sedes/e/"+id)
    else:
        sedes=ListarJson("/ppa/sedes/"+id)
    return render_template("aulas.html",N=N)

if __name__=='__main__':
    app.run(debug=True,port=8000) 
    
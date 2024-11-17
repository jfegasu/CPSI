from flask import Flask, jsonify,request

import json

#from services.apicnx import cnxsqlite
from api.cnxSqlite import cnxsqlite  
from config import configura 
app=Flask(__name__)
bd="./db/horario.db"
@app.route("/")
def inicio():
    return "Hola"
@app.route("/reg")
def ListaRegional():
    sql="select * from REGIONAL" 
    con=cnxsqlite()   
    todo=con.Consultar(bd,sql)
    return json.dumps(todo)
@app.route("/centro")
def ListaCentro():
    sql="select * from CENTRO" 
    con=cnxsqlite()   
    todo=con.Consultar(bd,sql)
    return json.dumps(todo)
@app.route("/centro/<idc>")
def ListaCentro1(idc):
    sql="select * from CENTRO c,regional r where c.idregion=r.idregional and idcentro="+idc 
    con=cnxsqlite()   
    todo=con.Consultar(bd,sql)
    return json.dumps(todo)
@app.route("/sede")
def ListaSede():
    sql="select * from SEDE s, CENTRO c where s.idcentro=c.idcentro " 
    con=cnxsqlite()   
    todo=con.Consultar(bd,sql)
    return json.dumps(todo)
@app.route("/sede/<ids>")
def ListaSede1(ids):
    sql="select * from SEDE s, CENTRO c where s.idcentro=c.idcentro and s.idsede="+ids 
    con=cnxsqlite()   
    todo=con.Consultar(bd,sql)
    return json.dumps(todo)

if __name__=='__main__':
    app.run(debug=True,port=configura['PUERTOREST'],host='0.0.0.0')
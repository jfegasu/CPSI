from flask import Flask, jsonify,request
import json
import sqlite3
bd="sinsonte.db"



def ConsultarJson(sql):
        con = sqlite3.connect("api/sinsonte.db")
        todo=[]     
        cur = con.cursor()  
        res=cur.execute(sql)
        nombres_columnas = [descripcion[0] for descripcion in cur.description]
        primer_resultado = res.fetchall()
    
        for i,valor in enumerate(primer_resultado):
            aux1=valor
            aux2= nombres_columnas
            aux3=dict(zip(aux2,aux1))   
            todo.append(aux3)
        con.close() 
        return list(todo)  

    
app=Flask(__name__)
@app.route("/")
def Inicio():
    return "SINSONTE"
@app.route("/t")
def ListaUnidad():
    sql="select * from unidad"
    todo=ConsultarJson(sql)    
    return json.dumps(todo)

@app.route("/t/<id>")
def ListaUnaUnidad(id):
    sql="select * from UNIDAD where IDUNIDAD="+str(id)
    todo=ConsultarJson(sql)
    return json.dumps(todo)

@app.route("/t/d/<id>",methods=['DELETE'])
def EliminaUnidad(id):
    sql="delete from UNIDAD where IDUNIDAD="+str(id)
    con = sqlite3.connect("api/sinsonte.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    return "200"
@app.route("/t/i",methods=['POST',])
def InsertaUnidad():
    datos = request.get_json()
    nom = datos.get('nombre')
    sql = "INSERT INTO UNIDAD (nombre) VALUES (?)"
    try:
        con = sqlite3.connect("api/sinsonte.db")
        cur = con.cursor()
        cur.execute(sql, (nom,))
        con.commit()
    except sqlite3.Error as e:
        return f"Database error: {e}", 500
    finally:
        con.close()
    return "200"
@app.route("/t/u",methods=['PUT',])
def ActualizaUnaUnidad():
    datos = request.get_json()    
    id = datos['id']
    nom = datos['nombre']
    sql = "update unidad set nombre=? where idunidad=?"
    try:
        con = sqlite3.connect("api/sinsonte.db")
        cur = con.cursor()
        cur.execute(sql, (nom,id,))
        con.commit()
    except sqlite3.Error as e:
        return f"Database error: {e}", 500
    finally:
        con.close()
    return "200"
@app.route("/a/<id>")
def ListaAptos(id):
    
    sql="select a.idapartamento,a.nomapto apt,u.nomunidad torre,a.contacto from apartamento a join unidad u using(nomunidad) where u.idunidad="+str(id)
    # sql="select a.idapartamento,a.nomapto apt,u.nomunidad torre,a.contacto from apartamento a join unidad u using(nomunidad) where where u.idunidad="+str(id)
    todo=ConsultarJson(sql)    
    return json.dumps(todo)
        

if __name__=='__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')

from flask import Flask, jsonify,request
import json
import sqlite3
from CrearORM import *
from peewee import MySQLDatabase
DATABASE = MySQLDatabase(
        'sinsonte',
        user='root',
        password='',
        host='localhost',
        port=3306  # Usualmente 3306 para MySQL
    )

app=Flask(__name__)
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

# Consultar apartamentos por ID de unidad
@app.route("/a/<int:id>")
def ListaAptos(id):
    apartamentos = (Apartamento
                    .select(Apartamento, Unidad)
                    .join(Unidad)
                    .where(Unidad.idunidad == id))
    
    resultado = []
    for apto in apartamentos:
        resultado.append({
            "idapartamento": apto.idapartamento,
            "nomapto": apto.nomapto,
            "torre": apto.unidad.nomunidad,
            "contacto": apto.contacto
        })
    return json.dumps(resultado)

if __name__ == '__main__':
    DATABASE.connect()  # Conectar a la base de datos
    app.run(debug=True, port=8000, host='0.0.0.0')


# def ConsultarJson(sql):
#         con = sqlite3.connect("api/sinsonte.db")
#         todo=[]     
#         cur = con.cursor()  
#         res=cur.execute(sql)
#         nombres_columnas = [descripcion[0] for descripcion in cur.description]
#         primer_resultado = res.fetchall()
    
#         for i,valor in enumerate(primer_resultado):
#             aux1=valor
#             aux2= nombres_columnas
#             aux3=dict(zip(aux2,aux1))   
#             todo.append(aux3)
#         con.close() 
#         return list(todo)  

    
# app=Flask(__name__)
# @app.route("/")
# def Inicio():
#     return "SINSONTE"
# @app.route("/t")
# def ListaUnidad():
#     sql="select * from unidad"
#     todo=ConsultarJson(sql)    
#     return json.dumps(todo)

# @app.route("/t/<id>")
# def ListaUnaUnidad(id):
#     sql="select * from UNIDAD where IDUNIDAD="+str(id)
#     todo=ConsultarJson(sql)
#     return json.dumps(todo)

# @app.route("/t/d/<id>",methods=['DELETE'])
# def EliminaUnidad(id):
#     sql="delete from UNIDAD where IDUNIDAD="+str(id)
#     con = sqlite3.connect("api/sinsonte.db")
#     cur = con.cursor()
#     cur.execute(sql)
#     con.commit()
#     con.close()
#     return "200"
# @app.route("/t/i",methods=['POST',])
# def InsertaUnidad():
#     datos = request.get_json()
#     nom = datos.get('nombre')
#     sql = "INSERT INTO UNIDAD (nombre) VALUES (?)"
#     try:
#         con = sqlite3.connect("api/sinsonte.db")
#         cur = con.cursor()
#         cur.execute(sql, (nom,))
#         con.commit()
#     except sqlite3.Error as e:
#         return f"Database error: {e}", 500
#     finally:
#         con.close()
#     return "200"
# @app.route("/t/u",methods=['PUT',])
# def ActualizaUnaUnidad():
#     datos = request.get_json()    
#     id = datos['id']
#     nom = datos['nombre']
#     sql = "update unidad set nombre=? where idunidad=?"
#     try:
#         con = sqlite3.connect("api/sinsonte.db")
#         cur = con.cursor()
#         cur.execute(sql, (nom,id,))
#         con.commit()
#     except sqlite3.Error as e:
#         return f"Database error: {e}", 500
#     finally:
#         con.close()
#     return "200"
# @app.route("/a/<id>")
# def ListaAptos(id):
    
#     sql="select a.idapartamento,a.nomapto apt,u.nomunidad torre,a.contacto from apartamento a join unidad u using(nomunidad) where u.idunidad="+str(id)
#     # sql="select a.idapartamento,a.nomapto apt,u.nomunidad torre,a.contacto from apartamento a join unidad u using(nomunidad) where where u.idunidad="+str(id)
#     todo=ConsultarJson(sql)    
#     return json.dumps(todo)
        

# if __name__=='__main__':
#     app.run(debug=True,port=8000,host='0.0.0.0')

# Ejemplo de inserción de datos
# Insertar una nueva unidad
# nueva_unidad = Unidad.create(nomunidad="Unidad A")

# Insertar un nuevo apartamento
# nuevo_apartamento = Apartamento.create(
#     nomapto="101", 
#     piso=1, 
#     nomunidad=nueva_unidad, 
#     observacion=1, 
#     celular="123456789", 
#     contacto="Juan Pérez", 
#     correo="juanperez@example.com"
# )

# Insertar un nuevo automotor
# nuevo_automotor = Automotor.create(
#     placa="ABC123", 
#     tipo=1, 
#     idapartamento=nuevo_apartamento
# )

# Insertar un nuevo ingreso
# from datetime import datetime
# nuevo_ingreso = Ingreso.create(
#     fecha=datetime.now(), 
#     idautomotor=nuevo_automotor, 
#     tipo=1
# )

# Cerrar la conexión
DATABASE.close()

# nueva_unidad = Unidad.create(nomunidad="Unidad A")

# # Insertar un nuevo apartamento
# nuevo_apartamento = Apartamento.create(
#     nomapto="101", 
#     piso=1, 
#     nomunidad=nueva_unidad, 
#     observacion=1, 
#     celular="123456789", 
#     contacto="Juan Pérez", 
#     correo="juanperez@example.com"
# )

# # Insertar un nuevo automotor
# nuevo_automotor = Automotor.create(
#     placa="ABC123", 
#     tipo=1, 
#     idapartamento=nuevo_apartamento
# )

# # Insertar un nuevo ingreso
# from datetime import datetime
# nuevo_ingreso = Ingreso.create(
#     fecha=datetime.now(), 
#     idautomotor=nuevo_automotor, 
#     tipo=1
# )

# # Cerrar la conexión
# DATABASE.close()
import sqlite3
configura={
    "STATIC_FOLDERS":"static",
    "TEMPLATE_FOLDER":"templates",
    "DEBUG":True,
    "SERVER_NAME":"http://127.0.0.1",
    "SERVER_API":"http://127.0.0.1:5000",
    "PUERTOREST":5000,
    "PUERTOAPP":8000,
    "MODULO":"salud",
    "SMBD":"SQLITE",
    "DB":"./nov.db"
}
class Usuario:
    
    res=None
    data=None
    def __init__(self,bd):
        self.bd=bd
        
        
    def ConsultarJson(self,sql):
            con = sqlite3.connect(self.bd)
            todo=[]
            cur = con.cursor()
            res=cur.execute(sql)
            nombres_columnas = [descripcion[0] for descripcion in cur.description]
            print(nombres_columnas)
            primer_resultado = res.fetchall()
        
            for i,valor in enumerate(primer_resultado):
                aux1=valor
                aux2= nombres_columnas
                aux3=dict(zip(aux2,aux1))   
                todo.append(aux3)
            con.close() 
            return list(todo)  
  
    def Inserte(self,data,clave="/i"):
        print(self.url+clave)
        response = requests.post(self.url+clave, json=data)
    def Borra(self,cual,clave):
        response = requests.delete(self.url+clave+str(cual))
    def Actualiza(self,data,clave="/u"):
        response = requests.put(self.url+clave, json=data)
############################################################


# def ListarTodos(clave="/to"):
#     res=requests.get(url+clave)
#     data1=json.loads(res.content)
#     return data1
# def ListarUno_a(cual):    
#     res=requests.get(url+"/ppa/"+str(cual))
#     data1=json.loads(res.content)
#     if data1!=[]:
#         return(data1)
#     else:
#         return False  
def ListarJson(clave):    
    res=requests.get(url+clave)
    data1=json.loads(res.content)
    if data1!=[]:
        return(data1)
    else:
        return False  
def InserteAPI(data,clave):
    print(url+clave)
    response = requests.post(url+clave, json=data)
def BorraAPI(cual,clave):
    try:
        response = requests.delete(url+clave+str(cual))
    except Exception as e:
        ValueError('Ocurrio un erro'+e)

def ActualizaAPI(data,clave):
    response = requests.put(url+clave, json=data)

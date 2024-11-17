import json,requests
from .config import configura

class Usuario:
    def __init__(self):
        self.url=configura['SERVER_NAME']+":"+str(configura['PUERTOREST'])

    def ListarJson(self,clave):    
        res=requests.get(self.url+clave)
        data1=json.loads(res.content)
        if data1!=[]:
            return(data1)
        else:
            return None  
    def InserteAPI(self,data,clave):
        print(self.url+clave)
        response = requests.post(self.url+clave, json=data)
    def BorraAPI(self,cual,clave):
        try:
            response = requests.delete(self.url+clave+str(cual))
        except Exception as e:
            ValueError('Ocurrio un erro'+e)

    def ActualizaAPI(self,data,clave):
        response = requests.put(self.url+clave, json=data)

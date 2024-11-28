from flask import request
import logging
import os
from datetime import datetime
import re
import string

class Auditor():
    logger=None
    def __init__(self):
        
        fecha=datetime.now()
        fe=str(fecha.year)+str(fecha.month)+str(fecha.day)
        # print("** Inicia **")
        os.makedirs('/log/'+fe,exist_ok=True)
        logger = logging.getLogger('werkzeug')
        self.logger =logger 
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s ',filename='/log/'+fe+'/login.log', encoding='utf-8',level=logging.WARNING)
        self.logger.setLevel(logging.WARNING  )
        # self.logger.warning("inicia")

    def logstart(self):
        return self.logger
    
    def registra(self,tipo,msg,usua="-"):
        client_ip = request.remote_addr
        if tipo==10:
            self.logger.debug(client_ip+' '+msg+' ['+usua+']')
        elif tipo==20:
            # print(client_ip+' '+msg+' '+usua)
            self.logger.info(client_ip+' '+msg+' '+usua)
        elif tipo==30:
            self.logger.warning(client_ip+' '+msg+' '+usua)
        elif tipo==40:
            # print(client_ip+' '+msg+' '+usua)
            self.logger.error(client_ip+' '+msg+' ['+usua+']')
        elif tipo==50:
            self.logger.critical(client_ip+' '+msg+' '+usua)
        elif tipo==60:
            self.logger.exception(client_ip+' '+msg+' '+usua)

class Utiles(Auditor):
    
    @classmethod
    def ConsistenciaClave(cs,datos):
            
            mayusculas = len([c for c in datos if c.isupper()])
            minusculas = len([c for c in datos if c.islower()])
            numeros = len([c for c in datos if c.isdigit()])
            canti=len(datos)
            
            espe=0
            caracteres = ['@', '#', '!', '*']
            for ca in datos:
                if ca not in string.ascii_letters and ca not in string.digits:
                    for char in caracteres:
                        cuenta = datos.count(char)
                        if cuenta:
                            espe+=1                
            print(f"datos={datos},mayusculas={mayusculas},minusculas={minusculas}, numeros={numeros}, longitud={canti},especiales={espe}")
            if mayusculas>=1 and minusculas>=1 and numeros>=1 and canti>=12 and espe>=1:
                return True
            else:
                return False
    @classmethod
    def Inyeccion(cs,dato,donde=" " ):
        Au=Auditor()
        patron=["--",';','union',"'"," or "," and ", "drop ",'1=1','1 = 1','"']
        for cadena in patron:
            resultado = re.search(cadena, dato.lower())   
            if resultado:
                 Au.registra(40,'Posible ataque de inyeccion sql ['+dato+'] '+donde)
                 return 'Posible ataque de inyeccion sql ['+dato+'] '+donde
        return 'x'                     

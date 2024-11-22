from flask import request
import logging
import os
from datetime import datetime
class Auditor():
    logger=None
    def __init__(self):
        
        fecha=datetime.now()
        fe=str(fecha.year)+str(fecha.month)+str(fecha.day)
        print("** Inicia **")
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

from flask import request
import logging
import os
class Auditor():
    logger=None
    def __init__(self):
        os.makedirs('log',exist_ok=True)
        logger = logging.getLogger('werkzeug')
        self.logger =logger 
        logging.basicConfig(format='%(asctime)s %(message)s ',filename='log/login.log', encoding='utf-8',level=logging.INFO)
        self.logger.setLevel(logging.ERROR)
        
    
    def logstart(self):
        return self.logger
    
    def registra(self,tipo,msg,usua="-"):
        client_ip = request.remote_addr
        if tipo==10:
            self.logger.debug(client_ip+' '+msg+' '+usua)
        elif tipo==20:
            self.logger.info(client_ip+' '+msg+' '+usua)
        elif tipo==30:
            self.logger.warning(client_ip+' '+msg+' '+usua)
        elif tipo==40:
            self.logger.error(client_ip+' '+msg+' '+usua)
        elif tipo==50:
            self.logger.critical(client_ip+' '+msg+' '+usua)

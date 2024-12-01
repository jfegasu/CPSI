import psutil
# for proc in psutil.process_iter():
#     print(proc.name(), proc.pid)
# https://nssm.cc/download

# C:\nssm\nssm.exe install "CheckSystemService" python C:\ruta\a\tu\putil.py
# https://tecnobillo.com/sections/python-en-windows/servicios-windows-python/servicios-windows-python.html
import psutil
import logging
import os
from datetime import datetime

fecha=datetime.now()
fe1=str(fecha.year)+str(fecha.month)+str(fecha.day)+"-"+str(fecha.hour)+"-"+str(fecha.minute)
fe=str(fecha.year)+str(fecha.month)+str(fecha.day)
print(fe)
os.makedirs('/log/'+fe,exist_ok=True)

# Configuración básica de registro
# logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s ',filename='/log/'+fe+'/login.log', encoding='utf-8',level=logging.WARNING)
        
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s ',filename="/log/"+fe+"/system_check.log", level=logging.INFO)
print("/log/"+fe+"/system_check.log")
# Función para verificar los discos
def check_disks():
    logging.info("Verificando discos duros..."+fe1)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        logging.info(f"Disco {partition.device}: Total {usage.total} Bytes, Usado {usage.used} Bytes, Libre {usage.free} Bytes, Porcentaje {usage.percent}%")

# Función para verificar la memoria RAM
def check_memory():
    logging.info("Verificando memoria RAM...")
    memory = psutil.virtual_memory()
    logging.info(f"Memoria total: {memory.total} Bytes, Usada: {memory.used} Bytes, Libre: {memory.available} Bytes, Porcentaje: {memory.percent}%")

# Función principal
def main():
    check_disks()
    check_memory()

if __name__ == "__main__":
    main()

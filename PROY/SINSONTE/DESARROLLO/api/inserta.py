from models import *
from databases import *
from peewee import  DoesNotExist

Unidad.create(
   nomunidad="TORRE B" 
)

Apartamento.create(
    nomapto="1110",
    unidad_id=2,
    observacion="",
    celular="3103057128",
    contacto="Jose Fegasu",
    correo="jgalindos@sena.edu.co"
)
Automotor.create(
   placa="IKK123",
   tipo=1,
   apartamento_id=1
)
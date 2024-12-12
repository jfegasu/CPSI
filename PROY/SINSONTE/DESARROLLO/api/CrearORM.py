from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField, DateTimeField, SqliteDatabase,AutoField
from peewee import MySQLDatabase
from databases import *
from flask import session
# Definir la base de datos (cambia estos parámetros por los de tu configuración de MySQL)
# DATABASE = MySQLDatabase(
#         'sinsonte',
#         user='root',
#         password='',
#         host='localhost',
#         port=3306  # Usualmente 3306 para MySQL
#     )
# Definir la clase base

class BaseModel(Model):
    class Meta:
        database = DATABASE

# Definir las clases para las tablas

class Unidad(BaseModel):
    idunidad = AutoField()
    nomunidad = TextField()

class Apartamento(BaseModel):
    idapartamento = AutoField()
    nomapto = CharField(max_length=4)
    piso = IntegerField()
    idunidad = ForeignKeyField(Unidad, backref='apartamentos')
    observacion = IntegerField()
    celular = TextField()
    contacto = TextField()
    correo = TextField()

class Automotor(BaseModel):
    idautomotor = AutoField()
    placa = TextField()
    tipo = IntegerField()
    idapartamento = ForeignKeyField(Apartamento, backref='automotores')

class Ingreso(BaseModel):
    idingreso = AutoField()
    fecha = DateTimeField()
    idautomotor = ForeignKeyField(Automotor, backref='ingresos')
    tipo = IntegerField()

# # Conectar a la base de datos
if __name__=='__main__':
    DATABASE.connect()
# # Crear las tablas en la base de datos si no existen
    DATABASE.create_tables([Unidad, Apartamento, Automotor, Ingreso])

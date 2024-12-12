
from flask import Flask,session, jsonify,request,render_template,redirect,url_for
from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField, DateTimeField, SqliteDatabase
from peewee import MySQLDatabase

# Definir la base de datos (puedes cambiarla según tu configuración)
app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sinsonte'

app.config['SECRET_KEY'] = "akDFJ34mdfsYMH567sdf" # this must be set in order to use sessions
try:
    DATABASE = MySQLDatabase(
        'sinsonte',
        user='root',
        password='',
        host='localhost',
        port=3306  # Usualmente 3306 para MySQL
    )
except Exception as e:
    print("Base de datos no existe")

class BaseModel(Model):
    class Meta:
        database = DATABASE

# Definir las clases para las tablas

class Unidad(BaseModel):
    idunidad = IntegerField(primary_key=True)
    nomunidad = TextField()

class Apartamento(BaseModel):
    idapartamento = IntegerField(primary_key=True)
    nomapto = CharField(max_length=4)
    piso = IntegerField()
    nomunidad = ForeignKeyField(Unidad, backref='apartamentos')
    observacion = IntegerField()
    celular = TextField()
    contacto = TextField()
    correo = TextField()

class Automotor(BaseModel):
    idautomotor = IntegerField(primary_key=True)
    placa = TextField()
    tipo = IntegerField()
    idapartamento = ForeignKeyField(Apartamento, backref='automotores')

class Ingreso(BaseModel):
    idingreso = IntegerField(primary_key=True)
    fecha = DateTimeField()
    idautomotor = ForeignKeyField(Automotor, backref='ingresos')
    tipo = IntegerField()

# Conectar a la base de datos
DATABASE.connect()

# Crear las tablas en la base de datos si no existen
DATABASE.create_tables([Unidad, Apartamento, Automotor, Ingreso])

# Ejemplo de inserción de datos
# Insertar una nueva unidad
nueva_unidad = Unidad.create(nomunidad="Unidad A")

# Insertar un nuevo apartamento
nuevo_apartamento = Apartamento.create(
    nomapto="101", 
    piso=1, 
    nomunidad=nueva_unidad, 
    observacion=1, 
    celular="123456789", 
    contacto="Juan Pérez", 
    correo="juanperez@example.com"
)

# Insertar un nuevo automotor
nuevo_automotor = Automotor.create(
    placa="ABC123", 
    tipo=1, 
    idapartamento=nuevo_apartamento
)

# Insertar un nuevo ingreso
from datetime import datetime
nuevo_ingreso = Ingreso.create(
    fecha=datetime.now(), 
    idautomotor=nuevo_automotor, 
    tipo=1
)

# Cerrar la conexión
DATABASE.close()
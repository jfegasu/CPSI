from peewee import Model, TextField, CharField, IntegerField, ForeignKeyField, BooleanField
from playhouse.sqlite_ext import SqliteExtDatabase
import sqlite3

# Assuming you're using SQLite, replace with your database of choice if needed
db = SqliteExtDatabase('./my_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class COORDINACION(BaseModel):
    nom = TextField(verbose_name="Nombre de la coordinación")

class AREA(BaseModel):
    nom = CharField(max_length=4, verbose_name="Nombre del area")
    descripcion = TextField()
    idcoordina = ForeignKeyField(COORDINACION, null=True, backref='areas', on_delete='SET NULL')

class TITULACION(BaseModel):
    cod = IntegerField(verbose_name="codigo de la titulacion")
    nom = TextField()
    idarea = ForeignKeyField(AREA, null=True, backref='titulaciones', on_delete='SET NULL')

class FICHA(BaseModel):
    nom = TextField()
    estado = IntegerField(default=0)
    idtitulacion = ForeignKeyField(TITULACION, null=True, backref='fichas', on_delete='SET NULL')

class NCL(BaseModel):
    cod = TextField()
    nom = TextField()
    des = TextField()
    idtitulacion = ForeignKeyField(TITULACION, null=True, backref='ncls', on_delete='SET NULL')

class RAP(BaseModel):
    cod = TextField()
    nom = TextField()
    idncl = ForeignKeyField(NCL, null=True, backref='raps', on_delete='SET NULL')

class ACTIVIDAD(BaseModel):
    nom = TextField()
    estado = IntegerField(default=0)
    horas = IntegerField(default=0)

class RAP_ACTIVIDAD(BaseModel):
    idrap = ForeignKeyField(RAP, null=True, backref='rap_actividades', on_delete='SET NULL')
    idactividad = ForeignKeyField(ACTIVIDAD, null=True, backref='rap_actividades', on_delete='SET NULL')

class FICHAS_ACTIVIDAD(BaseModel):
    idfichas = ForeignKeyField(FICHA, null=True, backref='fichas_actividades', on_delete='SET NULL')
    idactividad = ForeignKeyField(ACTIVIDAD, null=True, backref='fichas_actividades', on_delete='SET NULL')
db.connect()
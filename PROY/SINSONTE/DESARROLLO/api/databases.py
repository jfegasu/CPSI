from peewee import MySQLDatabase
from peewee import SqliteDatabase
# from peewee import PostgresqlDatabase


MYSQL = MySQLDatabase(
        'sinsonte',
        user='root',
        password='',
        host='localhost',
        port=3306  # Usualmente 3306 para MySQL
    )

SQLITE = SqliteDatabase('sinsonte.db')

# POSTGRES=PostgresqlDatabase(
#     'Analitica', 
#     host='192.168.134.56', 
#     port=5432, 
#     user='root', 
#     password='root')

DATABASE=MYSQL


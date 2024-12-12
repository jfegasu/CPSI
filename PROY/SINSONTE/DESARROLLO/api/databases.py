from peewee import MySQLDatabase
from peewee import SqliteDatabase
MYSQL = MySQLDatabase(
        'sinsonte',
        user='root',
        password='',
        host='localhost',
        port=3306  # Usualmente 3306 para MySQL
    )

SQLITE = SqliteDatabase('sinsonte.db')

DATABASE=MYSQL


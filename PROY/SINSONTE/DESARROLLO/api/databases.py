from peewee import MySQLDatabase
MYSQL = MySQLDatabase(
        'sinsonte',
        user='root',
        password='',
        host='localhost',
        port=3306  # Usualmente 3306 para MySQL
    )


import xlrd
import pandas as pd
import sqlite3
import sqldf
xx=pd.read_excel("MASIVA.xlsx",sheet_name=0)
def resetea(nombre):
    cnx = sqlite3.connect("api\sinsonte.db")
    cursor=cnx.cursor()
    cursor.execute("delete from "+nombre)
    cnx.commit()
    sql="update sqlite_sequence set seq=0 where name='"+nombre+"'"
    cursor.execute(sql)
    cnx.commit()
    cnx.close()
con = sqlite3.connect("api\sinsonte.db")
cursor=con.cursor()


# cursor.execute("update sqlite_sequence set seq=0 where name='UNIDAD' ")
resetea('UNIDAD')
DM_UNIDAD=sqldf.run("select distinct torre from xx")
print(DM_UNIDAD)
for i in range(len(DM_UNIDAD)):
    sql="INSERT INTO UNIDAD(nomunidad) values('"+DM_UNIDAD.loc[i][0]+"')"
    print(sql)
    cursor.execute(sql)
    con.commit()


cursor.execute("delete from apartamento")
con.commit()
resetea('APARTAMENTO')
x=xx
for i in range(len(xx)):
    sql="INSERT INTO APARTAMENTO(nomapto,piso,nomunidad,celular,contacto,correo) values('"+str(x.loc[i][1])+"','"+str(x.loc[i][2])+"','"+x.loc[i][0]+"','"+str(x.loc[i][4])+"','"+str(x.loc[i][3])+"','"+str(x.loc[i][5])+"')"
    cursor.execute(sql)
    con.commit()
    



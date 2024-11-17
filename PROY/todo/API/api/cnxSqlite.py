import sqlite3
class cnxsqlite:
    def Consultar(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        todo=res.fetchall()
        con.close() 
        return todo   
    def ConsultarUno(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        todo = res.fetchone()[0]
        con.close() 
        return todo   
    def Ejecutar(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        con.commit()
        con.close()
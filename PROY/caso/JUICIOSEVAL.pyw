import tkinter as tk
from tkinter import filedialog,messagebox
import pandas as pd
from pandasql import sqldf
from tkinter import *
from shutil import rmtree
import shutil
from tkinter.ttk import *
import time
import os

os.system ("cls")
filename1=""
XCabeza=pd.DataFrame(columns=(['Titulo']))

class rutinas:
    __archi  =""  
    workbook=""
    Datos={}
    def setArchivo(self,archi):
        self.__archi=archi
        print("->",archi)
    def getArchivo(self):
        return self.__archi      
    def diff_month(self,d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    def CrearCarpeta(self,ficha,a,cual):
        os.makedirs('./FICHAS/'+ficha+'/'+a[cual], exist_ok=True);    print('Creado .....',a[cual]) 

    def Cambiar(self,df,col,cambia):
        for x in cambia:
            df[col] = df[col].str.replace(r'\s*'+x+'\s*', ' ', regex=True)
    def AEXCEL(self,ruta,df,nom):
        #print(ruta)
        df.to_excel(ruta+"/"+nom+".xlsx", index=False)  
    def AEXCELibroInicio(self,nombre):
        libro=pd.ExcelWriter(nombre)
        return libro
    def AEXCELibro(self,libro,ruta,df,nom):
        #print(ruta)
        df.to_excel(ruta+"/"+nom+".xlsx", index=False)  

    def LeaArchivo(self,cual):
        self.workbook = pd.read_excel(cual)
        

    def SacaPorcion(self,ri,rs):
        x=pd.DataFrame(self.workbook[ri:rs])
        return x
    def SacaFicha(self):
        # x=pd.DataFrame(self.workbook[1:2])
        # print(x)
        # self.ficha=int(x['Unnamed: 2'])
        x=self.workbook.iloc[1]
        self.ficha=x[2]
        self.Datos["Ficha"]=x[2]
        x=self.workbook.iloc[0]
        self.ficha=x[2]
        self.Datos["FReporte"]=x[2]
        x=self.workbook.iloc[2]
        self.ficha=x[2]
        self.Datos["CProgra"]=x[2]
        x=self.workbook.iloc[8]
        self.ficha=x[2]
        self.Datos["Modo"]=x[2]
        x=self.workbook.iloc[9]
        self.ficha=x[2]
        self.Datos["Regional"]=x[2]
        x=self.workbook.iloc[10]
        self.ficha=x[2]
        self.Datos["Centro"]=x[2]
               
        
        
        
        
    def FechaInicio(self):
        x=self.workbook.iloc[6]
        self.FInicio=x[2]
        self.Datos["FInicia"]=x[2]
    def FechaFin(self):
        x=self.workbook.iloc[7]
        self.FFin=x[3]
        self.Datos["FFin"]=x[2]
    def Estado(self):
        x=self.workbook.iloc[5]
        self.FEstado=x[2]
        self.Datos["Estado"]=x[2]
    def FPrograma(self):
        x=self.workbook.iloc[4]
        self.FEstado=x[2]
        self.Datos["Programa"]=x[2]
    def FModalidad(self):
        x=self.workbook.iloc[8]
        self.FModalidad=x[2]
        self.Datos["Modalidad"]=x[2]
    def Encabezado(self):
        self.SacaFicha()
        self.FechaInicio()
        self.FechaFin()
        self.Estado()
        self.FModalidad()
        self.FPrograma()      

    def SacaFila(self,linea,columna):
        f=self.workbook.loc[linea:columna]
        return f

    def EscribeUnaLinea(self,df,que):
        df.loc[len(df)]=que

    def Extrae(self,data1,sql):
        DM=pd.DataFrame(sqldf(sql))
        DM.drop_duplicates(inplace=True)
        DM['id']=range(1,len(DM)+1)
        DM.set_index('id',inplace=True)
        return DM
    def BorrarCarpeta(self,cual):
        if os.path.exists('./FICHAS/'):
            rmtree('./FICHAS/')
    def CrearCarpetas(self,cual):
        os.makedirs(cual, exist_ok=True)
    def SacaColumna(self,df,cual):
        DM=df[cual]
        DM.drop_duplicates(inplace=True)
        return DM
    def Extrae(self,df,sql):
        data1=df
        DM=pd.DataFrame(sqldf(sql))
        DM.drop_duplicates(inplace=True)
        DM['id']=range(1,len(DM)+1)
        DM.set_index('id',inplace=True)
        return DM

root = tk.Tk()
root.title("JUICIOS EVALUATIVOS SENA - CGMLTI - V1.0 jgalindos@sena.edu.co")
root.geometry("550x70+500+50")
root.resizable(0,0)

archi=""
rutinas=rutinas()  

def open_file_dialog():
    TOPE=10
    PASO=0
    filena=""
    while len(rutinas.getArchivo())==0:
        filename=filedialog.askopenfilename(title="Seleccion juicio de evaluacion", filetypes=[("Excel97 files", "*.xls"),("Excel files", "*.xlsx"),("Todos", "*.*")])
        filename1=os.path.dirname(filename)
        rutinas.setArchivo(filename)
        
    bar=Progressbar(root,orient=HORIZONTAL,length=350)
    bar.place(x=60, y=60, width=350)
    bar.pack(pady=2,padx=2)
    # bar['value']+=0
    root.geometry("400x100")
    
    # bar['value']+=10
    # PASO+=1
    # root.update_idletasks()
    rutinas.LeaArchivo(rutinas.getArchivo())
    open_button.pack_forget()
    root.update_idletasks()
    
    
    rutinas.Encabezado()
    os.system ("cls")
    
    bar['value']+=20
    PASO+=1
    time.sleep(1)
    root.update_idletasks()
    data1=rutinas.workbook.drop(range(0,12),axis=0)
    data1['id']=range(1,len(data1)+1)
    #data1.rename(columns={'Reporte de Juicios de Evaluación':'TDOC',1:'DNI',2:'NOMBRE',3:'APELLIDOS',4:'ESTADO',5:'COMPETENCIA',6:'RAP',7:'JUICIO',8:'INSTRUCTOR'},inplace=True)
    data1.rename(columns={'Reporte de Juicios de Evaluación':'TDOC','Unnamed: 1':'DNI','Unnamed: 2':'NOMBRE','Unnamed: 3':'APELLIDOS','Unnamed: 4':'ESTADO','Unnamed: 5':'COMPETENCIA','Unnamed: 6':'RAP','Unnamed: 7':'JUICIO','Unnamed: 9':'FECHA','Unnamed: 10':'INSTRUCTOR'},inplace=True)
    data1 = data1.drop(columns=['Unnamed: 8'])
    cmalo=[':','\t','\n','\r','%','#']    
    rutinas.Cambiar(data1,'RAP',cmalo)

    data1.set_index('id',inplace=True)
    bar['value']+=20
    PASO+=1
    time.sleep(1)
    root.update_idletasks()
    DM_JUICIO=rutinas.SacaColumna(data1, 'JUICIO')
    DM_AUX=pd.DataFrame(data1,columns=['COMPETENCIA','RAP'])
    DM_AUX.drop_duplicates(inplace=True)
    DM_AUX['ABIERTA']="0";DM_AUX['CERRADA']="0";DM_AUX['ARTICULADA']="0";DM_AUX['ASIGNADO']="NO ASIGNADA"
    os.system('cls')
    
    DM_DNIF=rutinas.Extrae(data1,"select TDOC,DNI,NOMBRE,APELLIDOS,ESTADO FROM data1 WHERE ESTADO='EN FORMACION'")
    DM_CANCELADO=rutinas.Extrae(data1,"select TDOC,DNI,NOMBRE,APELLIDOS,ESTADO FROM data1 WHERE ESTADO='CANCELADO'")
    DM_DNINF=rutinas.Extrae(data1,"select TDOC,DNI,NOMBRE,APELLIDOS,ESTADO FROM data1 WHERE ESTADO NOT IN('EN FORMACION')")
    DM_COMPETENCIA=rutinas.Extrae(data1,"SELECT COMPETENCIA FROM data1 WHERE ESTADO ='EN FORMACION'  GROUP BY COMPETENCIA ")
    DM_RAP=rutinas.Extrae(data1,"SELECT RAP FROM data1 WHERE ESTADO ='EN FORMACION' GROUP BY RAP")
    DM_ESTADO=rutinas.Extrae(data1,"select DISTINCT ESTADO from data1")
    DM_INSTRUCTOR=rutinas.Extrae(data1,"select DISTINCT INSTRUCTOR FROM data1 WHERE INSTRUCTOR NOT IN('  -   ')")
    ENFORMACION=rutinas.Extrae(data1,"select * FROM data1 WHERE ESTADO IN('EN FORMACION')")
    ENFORMACIONU=rutinas.Extrae(data1,"select DISTINCT DNI FROM data1 WHERE ESTADO IN('EN FORMACION','CONDICIONADO')")
    ENFORMACIONC=rutinas.Extrae(data1,"select DISTINCT DNI FROM data1 WHERE ESTADO IN('CANCELADO')")
    ENFORMACIONK=rutinas.Extrae(data1,"select DISTINCT DNI FROM data1 WHERE ESTADO IN('CONDICIONADO')")
    ENFORMACIONR=rutinas.Extrae(data1,"select DISTINCT DNI FROM data1 WHERE ESTADO IN('RETIRO VOLUNTARIO')")
    APROBADOS=rutinas.Extrae(data1,"select * FROM data1 WHERE JUICIO IN('APROBADO')")
    POREVALUAR=rutinas.Extrae(data1,"select * FROM data1 WHERE JUICIO IN('POR EVALUAR') AND ESTADO IN ('EN FORMACION')")
    POREVALUAR1=rutinas.Extrae(data1,"select COMPETENCIA,RAP,JUICIO,COUNT(*) CANT FROM data1 WHERE ESTADO IN ('EN FORMACION') GROUP BY COMPETENCIA,RAP,JUICIO")
    # XEVALUARAPRENDIZ=rutinas.Extrae(data1,"select DNI,NOMBRE,APELLIDOS,COUNT(*) POREVALUAR FROM data1 WHERE JUICIO IN('POR EVALUAR')  AND ESTADO IN ('EN FORMACION','CONDICIONADO') GROUP BY DNI,NOMBRE,APELLIDOS ORDER BY 1,2")
    XEVALUARAPRENDIZ=rutinas.Extrae(data1,"select DNI,NOMBRE,APELLIDOS,COUNT(*) POREVALUAR FROM data1 WHERE JUICIO IN('POR EVALUAR') GROUP BY DNI,NOMBRE,APELLIDOS ORDER BY 1,2")
    KAUX="select DNI,NOMBRE,APELLIDOS,ESTADO,COUNT(*) APROBADA FROM data1 WHERE JUICIO IN('APROBADO') AND ESTADO IN ('EN FORMACION','CONDICIONADO') GROUP BY DNI"
    APROBADOSXAPRENDIZ=rutinas.Extrae(data1,KAUX)
    bar['value']+=20
    PASO+=1
    time.sleep(1)
    root.update_idletasks()
    RESUMENAPRENDIZ=pd.merge(XEVALUARAPRENDIZ,APROBADOSXAPRENDIZ,left_on="DNI",right_on="DNI",how="left")
    rutas="./FICHAS/"+str(rutinas.Datos['Ficha'])+"/"
    rutas=filename1+"/"
    XCabeza.loc[len(XCabeza)]=['Fecha del reporte: '+str(rutinas.Datos["FReporte"])]
    XCabeza.loc[len(XCabeza)]=['Ficha: '+str(rutinas.Datos["Ficha"])]
    XCabeza.loc[len(XCabeza)]=['Código Programa: '+str(rutinas.Datos["CProgra"])]
    XCabeza.loc[len(XCabeza)]=['Programa: '+str(rutinas.Datos["Programa"])]
    XCabeza.loc[len(XCabeza)]=['Fecha Inicio: '+str(rutinas.Datos["FInicia"])]
    XCabeza.loc[len(XCabeza)]=['Fecha Finalización: '+str(rutinas.Datos["FFin"])]
    XCabeza.loc[len(XCabeza)]=['Estado: '+str(rutinas.Datos["Estado"])]
    XCabeza.loc[len(XCabeza)]=['Modalidad: '+str(rutinas.Datos["Modo"])]
    XCabeza.loc[len(XCabeza)]=['Regional: '+str(rutinas.Datos["Regional"])]
    XCabeza.loc[len(XCabeza)]=['Centro: '+str(rutinas.Datos["Centro"])]
    XCabeza.loc[len(XCabeza)]=['Competencias: '+str(len(DM_COMPETENCIA))]
    XCabeza.loc[len(XCabeza)]=['Resultados de aprendizaje: '+str(len(DM_RAP))]
    XCabeza.loc[len(XCabeza)]=['En formación: '+str(len(ENFORMACIONU))]
    XCabeza.loc[len(XCabeza)]=['Condicionados: '+str(len(ENFORMACIONK))]
    XCabeza.loc[len(XCabeza)]=['Cancelados: '+str(len(ENFORMACIONC))]
    XCabeza.loc[len(XCabeza)]=['Retiros Voluntario: '+str(len(ENFORMACIONR))]
        
    with pd.ExcelWriter(rutas+str(rutinas.Datos['Ficha'])+".xlsx") as writer:
        
        XCabeza.to_excel(writer,sheet_name="INICIO", index=False)
        RESUMENAPRENDIZ.to_excel(writer,sheet_name="RESUMEN", index=False)
        APROBADOSXAPRENDIZ.to_excel(writer,sheet_name="APROBADOSXAPRENDIZ", index=False)
        data1.to_excel(writer,sheet_name="FICHA", index=False) 
        POREVALUAR.to_excel(writer,sheet_name="POREVALUAR", index=False) 
        POREVALUAR1.to_excel(writer,sheet_name="POREVALUARJUICIO", index=False) 
        ENFORMACION.to_excel(writer,sheet_name="ENFORMACION", index=False) 
        APROBADOS.to_excel(writer,sheet_name="APROBADOS", index=False) 
        DM_RAP.to_excel(writer,sheet_name="DM_RAP", index=False) 
        DM_COMPETENCIA.to_excel(writer,sheet_name="DM_COMPETENCIA", index=False) 
        DM_DNIF.to_excel(writer,sheet_name="DM_DNIF", index=False) 
        DM_DNINF.to_excel(writer,sheet_name="NOVEDADES", index=False) 
        paso1=sqldf("SELECT COMPETENCIA,RAP,ESTADO,JUICIO,COUNT(*) CANTIDAD FROM data1 group by COMPETENCIA,RAP,ESTADO")
        paso1['ID']=range(1,len(paso1)+1)
        paso1.set_index('ID',inplace=True)
        paso1.to_excel(writer,sheet_name="RESUMENXNCLYRAP", index=False)
        for i in DM_DNINF.DNI:    
            XRAP=data1[(data1['ESTADO']=='CANCELADO') & (data1['DNI']==i)]
            del XRAP['COMPETENCIA']
            del XRAP['RAP']
            XRAP.drop_duplicates(inplace=True)
        for i in DM_DNINF.DNI:    
            XRAP=data1[(data1['ESTADO']=='TRASLADADO') & (data1['DNI']==i)]
            del XRAP['COMPETENCIA']
            del XRAP['RAP']
            XRAP.drop_duplicates(inplace=True)
            # XRAP.to_excel(writer,sheet_name="TRASLADADO", index=False)
    
    bar['value']+=40
    PASO+=2    
    label = Label(root, text="DATOS DE LA FICHA").pack(anchor=NW)
    label = Label(root, text="Programa:"+rutinas.Datos['Programa']).pack(anchor=NW)
    label = Label(root, text="Ficha: "+str(rutinas.Datos['Ficha'])).pack(anchor=NW)
    label = Label(root, text="Codigo Programa: "+str(rutinas.Datos['CProgra'])).pack(anchor=NW)
    label = Label(root, text="Fecha Reporte: "+str(rutinas.Datos['FReporte'])).pack(anchor=NW)
    label = Label(root, text="Fecha Inicio: "+str(rutinas.Datos['FInicia'])).pack(anchor=NW)
    label = Label(root, text="Fecha Finalización: "+str(rutinas.Datos['FFin'])).pack(anchor=NW)
    label = Label(root, text="Estado:"+rutinas.Datos['Estado']).pack(anchor=NW)
    label = Label(root, text="Modalidad:"+rutinas.Datos['Modalidad']).pack(anchor=NW)
    os.system('cls')
    root.update_idletasks()
        
    root.geometry("400x270+300+50")    
    messagebox.showinfo(message="Proceso Terminado: ", title="Finalización del proceso")
    print("-->",filename1)
    print("Finalización del proceso")
    os.system ("cls")
    root.destroy()
        

icono_chico = tk.PhotoImage(file="sena.png")
icono_grande = tk.PhotoImage(file="sena.png")

root.iconphoto(False, icono_grande, icono_chico)
open_button = tk.Button(root, text="ABRIR JUICIO EVALUATIVO", command=open_file_dialog,foreground="#ff0000",background="white",cursor="mouse")
open_button.pack(padx=20, pady=3)



# messagebox.showinfo(message=archi, title="Título")
 



root.mainloop()   
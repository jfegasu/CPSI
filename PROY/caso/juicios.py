import xlrd
import pandas as pd
import os
import shutil


import sys
from pathlib import Path
import errno
import sqlite3
from pandasql import sqldf
import webbrowser
from datetime import datetime, timedelta
import rutinas
#os.system('cls')
print("ESTADO DE RESULTADOS DE APRENDIZAJE POR FICHA\nCENTRO DE GESTION DE MERCADOS,LOGÍSTICA Y TI")
print("JUICIOS EVALUATIVO POR FICHAS DE FORMACION\nFEGASU 2023 V1.0.0.2\njgalindos@sena.edu.co\n")
a=['0-RESUMENES','1-ENFORMACION','2-CANCELADOS','3-RETIROSV','4-TRASLADOS','5-APROBADOSCL','6-APROBADOSRAP','7-POREVALUARCL','8-POREVALUARAP','9-POREVALUARDNI','10-PORINSTRUCTOR','11-TODO']
contenido = os.listdir('../Archivos')
if len(sys.argv)>1:
    if sys.argv[1]=="-h":
        print("Uselo así:")
        print("python juicios.py ","Ejecuta los juicios de evaluacion que hay en la carperta Archivos")
        sys.exit(0)

    
rutinas.BorrarCarpeta('./FICHAS/')
rutinas.CrearCarpetas('./ZIP')
rutinas.CrearCarpetas('./FICHAS')
ii=0 

for ii in range(len(contenido)):
    workbook = rutinas.LeaArchivo("../Archivos/"+contenido[ii])
    ficha=rutinas.SacaPorcion(workbook,1,2)
    # ficha1=ficha['Unnamed: 2']
    # aux=str(ficha1[1])
    aux=str(rutinas.SacaFila(ficha, 1, 'Unnamed: 2'))
    ficha1=rutinas.SacaFila(workbook, 6, 'Unnamed: 2')
    dd1=pd.to_datetime(ficha1,format= "%YYYY/%m/%d %H:%M:%S") 
    ficha1=rutinas.SacaFila(workbook, 7, 'Unnamed: 2')
    dd2=pd.to_datetime(ficha1,format= "%YYYY/%m/%d %H:%M:%S") 
    
    print("->",dd1,"->",dd2)
    trimestre=(rutinas.diff_month(dd2,dd1)/3)

    miruta=aux
    print("Procesando la ficha:",aux)
    os.makedirs('./FICHAS/'+aux, exist_ok=True)
    # def CrearCarpeta(ficha,cual):
    #     os.makedirs('./FICHAS/'+ficha+'/'+a[cual], exist_ok=True);    print('Creado .....',a[cual]) 
    dir = aux
   
    # for files in os.listdir(dir):
    #     path = os.path.join(dir, files)
    #     try:
    #         shutil.rmtree(path)
    #     except OSError:
    #         os.remove(path)
  
    for i in range(len(a)):
        rutinas.CrearCarpeta(aux,a,i)

    # Ficha de Caracterización:
    info=pd.DataFrame(workbook[0:11])
    del(info['Unnamed: 1'])
    del(info['Unnamed: 3'])
    del(info['Unnamed: 4'])
    del(info['Unnamed: 5'])
    del(info['Unnamed: 6'])
    del(info['Unnamed: 7'])
    del(info['Unnamed: 8'])
    info.rename(columns={'Reporte de Juicios de Evaluación':'TIPO','Unnamed: 2':'DESCRIPCION'},inplace=True)
    #sys.exit(1)
    data1=workbook.drop(range(0,12),axis=0)
    data1['id']=range(1,len(data1)+1)
    #data1.rename(columns={'Reporte de Juicios de Evaluación':'TDOC',1:'DNI',2:'NOMBRE',3:'APELLIDOS',4:'ESTADO',5:'COMPETENCIA',6:'RAP',7:'JUICIO',8:'INSTRUCTOR'},inplace=True)
    data1.rename(columns={'Reporte de Juicios de Evaluación':'TDOC','Unnamed: 1':'DNI','Unnamed: 2':'NOMBRE','Unnamed: 3':'APELLIDOS','Unnamed: 4':'ESTADO','Unnamed: 5':'COMPETENCIA','Unnamed: 6':'RAP','Unnamed: 7':'JUICIO','Unnamed: 8':'INSTRUCTOR'},inplace=True)
    cmalo=[':','\t','\n','\r','%','#']
    # def Cambiar(df,col,cambia):
    #     for x in cambia:
    #         df[col] = df[col].str.replace(r'\s*'+x+'\s*', ' ', regex=True)
    
    rutinas.Cambiar(data1,'RAP',cmalo)
    def Extrae(sql):
        DM=pd.DataFrame(sqldf(sql))
        DM.drop_duplicates(inplace=True)
        DM['id']=range(1,len(DM)+1)
        DM.set_index('id',inplace=True)
        return DM
    
    
    data1.set_index('id',inplace=True)

    DM_JUICIO=rutinas.SacaColumna(data1, 'JUICIO')
    DM_AUX=pd.DataFrame(data1,columns=['COMPETENCIA','RAP'])
    DM_AUX.drop_duplicates(inplace=True)
    DM_AUX['ABIERTA']="0";DM_AUX['CERRADA']="0";DM_AUX['ARTICULADA']="0";DM_AUX['ASIGNADO']="NO ASIGNADA"

    DM_DNIF=rutinas.Extrae(data1,"select TDOC,DNI,NOMBRE,APELLIDOS,ESTADO FROM data1 WHERE ESTADO='EN FORMACION'")
    DM_CANCELADO=rutinas.Extrae(data1,"select TDOC,DNI,NOMBRE,APELLIDOS,ESTADO FROM data1 WHERE ESTADO='CANCELADO'")
    DM_DNINF=rutinas.Extrae(data1,"select TDOC,DNI,NOMBRE,APELLIDOS,ESTADO FROM data1 WHERE ESTADO NOT IN('EN FORMACION')")
    DM_COMPETENCIA=rutinas.Extrae(data1,"SELECT COMPETENCIA FROM data1 WHERE ESTADO ='EN FORMACION'  GROUP BY COMPETENCIA ")
    DM_RAP=rutinas.Extrae(data1,"SELECT RAP FROM data1 WHERE ESTADO ='EN FORMACION' GROUP BY RAP")
    DM_ESTADO=rutinas.Extrae(data1,"select DISTINCT ESTADO from data1")
    DM_INSTRUCTOR=rutinas.Extrae(data1,"select DISTINCT INSTRUCTOR FROM data1 WHERE INSTRUCTOR NOT IN('  -   ')")
    ENFORMACION=rutinas.Extrae(data1,"select * FROM data1 WHERE ESTADO IN('EN FORMACION')")
    APROBADOS=rutinas.Extrae(data1,"select * FROM data1 WHERE JUICIO IN('APROBADO')")
    POREVALUAR=rutinas.Extrae(data1,"select * FROM data1 WHERE JUICIO IN('POR EVALUAR') AND ESTADO IN ('EN FORMACION')")
    XEVALUARAPRENDIZ=rutinas.Extrae(data1,"select DNI,NOMBRE,APELLIDOS,COUNT(*) POREVALUAR FROM data1 WHERE JUICIO IN('POR EVALUAR')  AND ESTADO IN ('EN FORMACION') GROUP BY DNI,NOMBRE,APELLIDOS")
    KAUX="select DNI,COUNT(*) APROBADA FROM data1 WHERE JUICIO IN('APROBADO') AND ESTADO IN ('EN FORMACION') GROUP BY DNI"
    APROBADOSXAPRENDIZ=rutinas.Extrae(data1,KAUX)
    fichas="./FICHAS/"+aux
    RESUMENAPRENDIZ=pd.merge(XEVALUARAPRENDIZ,APROBADOSXAPRENDIZ,left_on="DNI",right_on="DNI",how="left")
    
 
    with pd.ExcelWriter(fichas+".xlsx") as writer:
        RESUMENAPRENDIZ.to_excel(writer,sheet_name="RESUMEN", index=False) 
        APROBADOSXAPRENDIZ.to_excel(writer,sheet_name="APROBADOSXAPRENDIZ", index=False) 
        data1.to_excel(writer,sheet_name="FICHA", index=False) 
        POREVALUAR.to_excel(writer,sheet_name="POREVALUAR", index=False) 
        ENFORMACION.to_excel(writer,sheet_name="ENFORMACION", index=False) 
        APROBADOS.to_excel(writer,sheet_name="APROBADOS", index=False) 
        DM_RAP.to_excel(writer,sheet_name="DM_RAP", index=False) 
        DM_COMPETENCIA.to_excel(writer,sheet_name="DM_COMPETENCIA", index=False) 
        DM_DNIF.to_excel(writer,sheet_name="DM_DNIF", index=False) 
        DM_DNINF.to_excel(writer,sheet_name="DM_DNINF", index=False) 
        DM_AUX.to_excel(writer,sheet_name="DM_ESTADO", index=False) 
        DM_INSTRUCTOR.to_excel(writer,sheet_name="DM_INSTRUCTOR", index=False) 
        paso1=sqldf("SELECT COMPETENCIA,RAP,ESTADO,JUICIO,COUNT(*) CANTIDAD FROM data1 group by COMPETENCIA,RAP,ESTADO")
        paso1['ID']=range(1,len(paso1)+1)
        paso1.set_index('ID',inplace=True)
        paso1.to_excel(writer,sheet_name="RESUMENXNCLYRAP", index=False) 
        for i in DM_RAP.RAP:    
            au=i[0:70]
            XRAP=ENFORMACION[(ENFORMACION['JUICIO']=='POR EVALUAR') & (ENFORMACION['ESTADO']=='EN FORMACION') & (ENFORMACION['RAP']==i)]
            XRAP=XRAP.replace(":","")
            j=len(XRAP)
            if j>0:
                # XRAP.to_excel("./FICHAS/"+aux+"/8-POREVALUARAP/"+au+".xlsx", index=False)
                XRAP.to_excel(writer,sheet_name="RAP"+str(j)+"XEVALUAR", index=False) 
        
        for i in DM_DNINF.DNI:    
            XRAP=data1[(data1['ESTADO']=='CANCELADO') & (data1['DNI']==i)]
            j=len(XRAP)
            if j>0:
                XRAP.to_excel("CANCELADOS"+i, index=False)
        for i in DM_DNINF.DNI:    
            XRAP=data1[(data1['ESTADO']=='TRASLADADO') & (data1['DNI']==i)]
            j=len(XRAP)
            if j>0:
                XRAP.to_excel(writer,sheet_name="TRASLADOS"+i, index=False)
        
    
    
    
    rutinas.AEXCEL(fichas,DM_JUICIO,'DM_JUICIO')  
    
    rutinas.EscribeUnaLinea(info,{'TIPO': 'NCL', 'DESCRIPCION':len(DM_COMPETENCIA)})
    
    rutinas.EscribeUnaLinea(info,{'TIPO': 'RAP', 'DESCRIPCION':len(DM_RAP)})

    rutinas.EscribeUnaLinea(info,{'TIPO': 'APRENDICES EN FORMACION', 'DESCRIPCION':len(DM_DNIF)})

    rutinas.EscribeUnaLinea(info,{'TIPO': 'RAP APROBADAS', 'DESCRIPCION':len(APROBADOS)})
    CAN=rutinas.Extrae(data1,"SELECT DISTINCT(RAP) FROM data1 WHERE ESTADO='EN FORMACION' AND JUICIO='APROBADO'")

    rutinas.EscribeUnaLinea(info,{'TIPO': 'RAP POR APROBAR', 'DESCRIPCION':len(CAN)})
   
    
    paso1=sqldf("SELECT COMPETENCIA,RAP,ESTADO,JUICIO,COUNT(*) CANTIDAD FROM data1 group by COMPETENCIA,RAP,ESTADO")
    paso1['ID']=range(1,len(paso1)+1)
    paso1.set_index('ID',inplace=True)
    rutinas.AEXCEL(fichas+"/0-RESUMENES",paso1,'RESUMENXNCLYRAP')  
    
    for i in DM_RAP.RAP:    
        au=i[0:70]
        XRAP=ENFORMACION[(ENFORMACION['JUICIO']=='POR EVALUAR') & (ENFORMACION['ESTADO']=='EN FORMACION') & (ENFORMACION['RAP']==i)]
        XRAP=XRAP.replace(":","")
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/8-POREVALUARAP/"+au+".xlsx", index=False)
            #rutinas.AEXCEL(aux,XRAP,'POREVALUARAP') 
    for i in DM_RAP.RAP:    
        au=i[0:60]
        # print("DM_RAP",au)
        ENFORMACION=ENFORMACION.replace(":","")
        ENFORMACION=ENFORMACION.replace(chr(10),"")
        
        ku="SELECT * FROM ENFORMACION WHERE JUICIO='APROBADO' AND ESTADO ='EN FORMACION' AND RAP='"+i+"'"
        # print(ku)

        XRAP=Extrae("SELECT * FROM ENFORMACION WHERE JUICIO='APROBADO' AND ESTADO ='EN FORMACION' AND RAP='"+i+"'")
        j=len(XRAP)
        if j>1:
            ka="./FICHAS/"+aux+"/APROBADOSRAP/"+au+".xlsx"
            XRAP.to_excel("./FICHAS/"+aux+"/6-APROBADOSRAP/"+au+".xlsx", index=False)
        j=0

    for i in DM_COMPETENCIA.COMPETENCIA:    
        au=i[0:70]
        #print("DM_COMPETENCIA")
        XRAP=ENFORMACION[(ENFORMACION['JUICIO']=='APROBADO') & (ENFORMACION['ESTADO']=='EN FORMACION') & (ENFORMACION['COMPETENCIA']==i)]
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/5-APROBADOSCL/"+au+".xlsx", index=False)

    sql="SELECT * FROM ENFORMACION WHERE (JUICIO='POR EVALUAR') AND (ESTADO ='EN FORMACION') and COMPETENCIA = '"+i+"'"
    ruta="./FICHAS/"+aux+"/POREVALUARCL/"+au

    for i in DM_COMPETENCIA.COMPETENCIA:    
        au=i[0:70]
        XRAP=Extrae("SELECT * FROM ENFORMACION WHERE (JUICIO='POR EVALUAR') AND (ESTADO ='EN FORMACION') and COMPETENCIA = '"+i+"'")
        j=len(XRAP)
        if j>0:
              XRAP.to_excel("./FICHAS/"+aux+"/7-POREVALUARCL/"+au+".xlsx", index=False)           


    for i in DM_DNIF.DNI:    
        XRAP=ENFORMACION[(ENFORMACION['JUICIO']=='POR EVALUAR') & (ENFORMACION['ESTADO']=='EN FORMACION') & (ENFORMACION['DNI']==i)]
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/9-POREVALUARDNI/"+i+".xlsx", index=False)
    for i in DM_DNINF.DNI:    
        XRAP=data1[(data1['ESTADO']=='CANCELADO') & (data1['DNI']==i)]
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/2-CANCELADOS/"+i+".xlsx", index=False)
            
    for i in DM_DNINF.DNI:    
        XRAP=data1[(data1['ESTADO']=='RETIRO VOLUNTARIO') & (data1['DNI']==i)]
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/3-RETIROSV/"+i+".xlsx", index=False)
    for i in DM_DNINF.DNI:    
        XRAP=data1[(data1['ESTADO']=='TRASLADADO') & (data1['DNI']==i)]
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/4-TRASLADOS/"+i+".xlsx", index=False)
            
    for i in DM_INSTRUCTOR.INSTRUCTOR:    
        XRAP=ENFORMACION[(ENFORMACION['JUICIO']=='APROBADO') & (ENFORMACION['ESTADO']=='EN FORMACION') & (ENFORMACION['INSTRUCTOR']==i)]
        j=len(XRAP)
        if j>0:
            XRAP.to_excel("./FICHAS/"+aux+"/10-PORINSTRUCTOR/"+i+".xlsx", index=False)
    shutil.copy("../Archivos/"+contenido[ii], "./FICHAS/"+aux+"/"+contenido[ii])

    CAN=rutinas.Extrae(data1,"SELECT DISTINCT(DNI) FROM data1 WHERE ESTADO='CANCELADO'")
    rutinas.EscribeUnaLinea(info,{'TIPO': 'CANCELADOS', 'DESCRIPCION':len(CAN)})
    CAN=rutinas.Extrae(data1,"SELECT DISTINCT(DNI) FROM data1 WHERE ESTADO='TRASLADADO'")
    rutinas.EscribeUnaLinea(info,{'TIPO': 'TRASLADADOS', 'DESCRIPCION':len(CAN)})
    CAN=rutinas.Extrae(data1,"SELECT DISTINCT(DNI) FROM data1 WHERE ESTADO='RETIRO VOLUNTARIO'")
    rutinas.EscribeUnaLinea(info,{'TIPO': 'RETIRO VOLUNTARIO', 'DESCRIPCION':len(CAN)})
    rutinas.EscribeUnaLinea(info,{'TIPO':'DURACION', 'DESCRIPCION':trimestre})
    rutinas.EscribeUnaLinea(info,{'TIPO':'PRODUCTIVA', 'DESCRIPCION': 2})
    rutinas.EscribeUnaLinea(info,{'TIPO':'LECTIVA', 'DESCRIPCION': trimestre-2})
    info.to_excel("./FICHAS/"+aux+"/0-RESUMENES/INFORMACION.xlsx", index=False)

    shutil.make_archive("./ZIP/"+aux,'zip',"./FICHAS/"+aux)
webbrowser.open_new_tab(os.getcwd()+"/FICHAS")
print("PROCESO FINALIZADO *******")

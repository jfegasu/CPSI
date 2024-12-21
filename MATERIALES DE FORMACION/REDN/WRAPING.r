xtraer <- function(DATOS, Cual) {
  # Ensure DM_CATEGORIA is defined and exists in the global environment
  if (!exists("DM_CATEGORIA")) {
    DM_CATEGORIA <- data.frame()
  }
 
  # Extract and process the table from DATOS using the specified Cual
  II <- data.frame(html_table(DATOS[[Cual]], fill = TRUE))
 
  # Update DM_CATEGORIA with the first row and first two columns of II
  DM_CATEGORIA <<- rbind(DM_CATEGORIA, II[1, c(1, 2)])
 
  # Remove unwanted columns and the first row from II
  II <- II[, -c(3:5)]
  II <- II[-1, ]
 
  # Rename columns in II
  colnames(II) <- c('CODIGO', 'DESCRIPCION')
 
  # Add the INMOV column based on the presence of 'INMOVILIZACIÓN: SI' in DESCRIPCION
  II$INMOV <- ifelse(grepl('INMOVILIZACIÓN: SI', II$DESCRIPCION), 'SI', 'NO')
 
  # Return the processed data |frame
  return(II)
}

#x=read.csv("Informaci_n_estad_stica_de_inmovilizaci_n_veh_culos_20240731.csv",header = TRUE)
#names(x)[4]<-"NOMCIUDAD"
#x$NOMCIUDAD<-toupper(x$NOMCIUDAD)
w <- "https://www.okatwork.co/listado-infracciones-de-transito-colombia-resolucion-3027-de-2010.html"
DATOS <- read_html(w)
DATOS <- html_nodes(DATOS, "table")
A=B=C=D=E=F=G=H=0
DA=c(A,B,C,D,E,F,G,H,I)
for (i in DA){
A<-Extraer(DATOS,1)
}

B<-Extraer(DATOS,2)
C<-Extraer(DATOS,3)
D<-Extraer(DATOS,4)
E<-Extraer(DATOS,5)
F<-Extraer(DATOS,6)
G<-Extraer(DATOS,7)
H<-Extraer(DATOS,8)
I<-Extraer(DATOS,9)

DM_INFRACCIONES<- A
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,B)
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,C)
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,D)
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,E)
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,F)
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,G)
DM_INFRACCIONES<-rbind(DM_INFRACCIONES,H)
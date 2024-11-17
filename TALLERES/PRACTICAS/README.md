<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<h1><b>CENTRO DE PRODUCCION DE SOLUCIONES INTELIGENTES</b></h1>
<link href="http://siomi.datasena.com/analitica/Estilo.css" rel="stylesheet" type="text/css" />

<img src="https://blogger.googleusercontent.com/img/a/AVvXsEimdqxynaYJeDRuTUp3lzEWFnnQSC2KTVSxvnV70I2eZ5tOCfjwdNnExSTSm2tCf1xBFHVHwsN80OCpDCO0J80UTNWxPC86s7s5aB8rnizg7guNowqTxhr5Fd9WH48n7pn8uLZNFTgXuSGUH6BNncmfQEpOz9pAe_T0zD8n2-aGZk8-C_l6GWk-aq60fQ=s960">
<br>
<div class="container-md">
<h2><b>INSTALACION DE SISTEMAS MANEJADORES DE BASE DE DATOS EN DOCKER </b></h2>
<table border="1" class="table table-success table-striped mp-4">
    <th>SMBD</th>
    <th>IMAGEN</th>
    <th width="40%">CONTENEDOR</th>
    <th>SOFTWARE</th>
    </tr>
    <tr>
        <td>POSTGRES</td>
        <td>docker pull postgres</td>
        <td>docker run -e POSTGRES_PASSWORD=root -e POSTGRES_USER=root -e POSTGRES_DB=Analitica -p 5432:5432 --name pgsqlsena -d postgres</td>
        <td><a href="https://sourceforge.net/projects/pgsqlportable/files/latest/download" target="xxx">POSTGRES PORTABLE</a><br>
        <a href="https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe" target="xxx">DBEAVER</a></td>
        </td>
    </tr>
    <tr>
        <td>MONGODB</td>
        <td>docker pull mongo</td>
        <td>docker run -p 27017:27017 --name mongosena -d mongo</td>
        <td><a href="https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.1-signed.msi" target="xxx">MONGO SERVER</a><br>
            <a href="https://downloads.mongodb.com/compass/mongodb-compass-1.32.6-win32-x64.exe" target="xxx">MONGO COMPAS</a><br>
            </td>
    </tr>
    <tr>
        <td>MARIADB</td>
        <td>docker pull mariadb</td>
        <td>docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root --name mariadbsena -d mariadb
        <td><a href="https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe" target="xxx">DBEAVER</a></td>
        </td>
    </tr>
    <tr>
        <td>SQLSERVER</td>
        <td>docker pull mcr.microsoft.com/mssql/server</td>
        <td>docker run --name "misqlserver" -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=SQL#1234" -p 1433:1433 -d mcr.microsoft.com/mssql/server</td>
        <td><a href="https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe" target="xxx">DBEAVER</a><br>
            <a href="https://aka.ms/ssmsfullsetup" target="xxx">SQL SERVER MANADEMENT STUDIO</a></td>
        </td>
    </tr>
    <tr>
        <td>ORACLE</td>
        <td>docker pull container-registry.oracle.com/database/free </td>
        <td>docker run --name "misqlserver" -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=SQL#1234" -p 1433:1433 -d mcr.microsoft.com/mssql/server</td>
        <td><a href="https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe" target="xxx">DBEAVER</a><br>
            <a href="https://download.oracle.com/otn_software/java/sqldeveloper/sqldeveloper-23.1.1.345.2114-x64.zip" target="xxx">SQLDEVELOPER</a></td>
        </td>
    </tr>
    
</table>
</div>
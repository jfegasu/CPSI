
create user 'prueba'@'localhost' identified by 'prueba';
create user 'juanchotv123'@'localhost' identified by '123';
create user 'admin'@'localhost' identified by '123';

CREATE ROLE 'ADMIN';
    grant select,insert,update,delete ON fabrica.* TO admin;


CHECK TABLE db;
REPAIR TABLE db;





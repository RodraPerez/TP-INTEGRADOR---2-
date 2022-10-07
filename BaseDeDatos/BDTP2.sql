#ESCRIBIR ACA LOS SCRIPTS PARA CREAR LA BASE DE DATOS:::

#Crear Database:

CREATE DATABASE disqueria
DEFAULT CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_0900_ai_ci';


use disqueria;

create table genero (
    id_genero int not null auto_increment primary key,
    nombre varchar(50) unique
);

create table discografica(
    id_discografica int not null auto_increment primary key,
    nombre varchar(50) unique
);

create table formato(
    id_formato int not null auto_increment primary key,
    tipo varchar(50) unique
);

create table interprete(
    id_interprete int not null auto_increment primary key,
    nombre varchar(50),
    apellido varchar(50),
    nacionalidad varchar(50),
    foto varchar(200),
    CONSTRAINT interprete_unico UNIQUE (nombre,apellido)
);

create table album(
    id_album int auto_increment primary key,
    cod_album VARCHAR(45) unique not null,
    nombre varchar(100) not null,
    id_interprete int not null,
    id_genero int not null,
    cant_temas int not null,
    id_discografica int not null,
    id_formato int not null,
    fec_lanzamiento year,
    precio decimal(10,2) not null,
    cantidad int not null,
    caratula varchar(200),
    foreign key(id_genero) references genero(id_genero),
    foreign key(id_discografica) references discografica(id_discografica),
    foreign key(id_formato) references formato(id_formato)
    ); 

create table tema(
        id_tema int auto_increment primary key,
        track_num int null,
        titulo varchar(100),
        duracion time not null,
        autor varchar(100) not null,
        compositor varchar(100) not null,
        id_album int not null,
        id_interprete int not null,
        foreign key(id_album) references album(id_album),
        foreign key(id_interprete) references interprete(id_interprete)
    );

#--------------------------
# Carga de datos de Prueba:
#--------------------------
    
# Carga de Interpretes: 
# Interprete:                  id_interprete,nombre,apellido,nacionalidad,foto
insert into interprete values (null,'Laura','Pausini','Italia','https://i.discogs.com/9ZvfGO3Z2QpAcJD6cjIEopZncvSpd_PI2EA_HuEHcBc/rs:fit/g:sm/q:90/h:640/w:555/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTgwODk0/LTE2MTI4OTM3NjIt/MzY0MC5qcGVn.jpeg');
insert into interprete values (null,'Raúl','DiBlasio','Argentina','https://i.discogs.com/wfDT6pozjDg3rlHvNj-C4N5GktOQb1nEnrdq1qR9AoY/rs:fit/g:sm/q:90/h:376/w:354/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTkwNTUz/MC0xNTQxNjAxMjAy/LTM3OTAucG5n.jpeg');
insert into interprete values (null,'Richard','Clayderman','Francia','https://i.discogs.com/QcDYuXwaRVpUPOJnOMZ-RWPs3zOvgmKqGRKCsHv5FXA/rs:fit/g:sm/q:90/h:800/w:585/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTE2ODY4/NC0xNTIxMTE5NzEw/LTQ2MzUuanBlZw.jpeg');
insert into interprete values (null,'Enya','Brennan','Irlanda','https://i.discogs.com/pHUFxlUDubrF0-7XfWmct0D7sHh8WSrdaJ-Hju-tGcE/rs:fit/g:sm/q:90/h:599/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTk4MDct/MTU2MjkyMDE4MC02/NTEzLmpwZWc.jpeg');
insert into interprete values (null,'Vangelis','Papathanasiouss','Grecia','https://i.discogs.com/B7S_0ifknepFZRVL_ZDFiedhGJ4JD4FQYKqDD0j8mxQ/rs:fit/g:sm/q:90/h:392/w:518/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTcwMjct/MTI0MDE1NjE0OS5q/cGVn.jpeg');
insert into interprete values (null,'Jean Michel','Jarre','Francia','https://i.discogs.com/JvEyuFufRpZnhn4kiJY33VWc547UoYXUO02FMeBiMdM/rs:fit/g:sm/q:90/h:696/w:582/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTIwOTQx/NS0xNTE3MDAyODYy/LTQ2NDEuanBlZw.jpeg');
insert into interprete values (null,'La Mona','Gimenez','Argentina','https://i.discogs.com/9cUw0qSnjS9OGkKfPz0Id-iCprA8E6smcoeX8cJLYTE/rs:fit/g:sm/q:90/h:450/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTEyMDQ5/MjctMTQ1MDAxOTA3/Ny00ODk4LmpwZWc.jpeg');
insert into interprete values (null,'Chaqueño','Palavecino','Argentina','https://i.discogs.com/qN1xls0Bkl4TtzG5P0J24ETw4YjW3sb-2xH5YQ6NBS8/rs:fit/g:sm/q:90/h:399/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTQ0OTA5/MjEtMTQ0Nzk1MjUw/Mi0zOTgwLmpwZWc.jpeg');
insert into interprete values (null,'Hermanos','Pimpinela','Argentina','https://i.discogs.com/eSaBq8TxohPse8CgGL5ntugYyqx8hYV-uqHorZtbWzg/rs:fit/g:sm/q:90/h:450/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTk2MjAx/My0xNDc4NDU4MzEz/LTM3MTkuanBlZw.jpeg');
insert into interprete values (null,'Ulises','Bueno','Argentina','https://i.discogs.com/SaKA1tZeb03bz-ktM8dVHsEvCfOy3H1mwtJyvcU8Y3g/rs:fit/g:sm/q:90/h:400/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTU0MjEw/MjEtMTU4MzI2OTM0/My05NzY5LmpwZWc.jpeg');
insert into interprete values (null,'Leo','Mattioli','Argentina','https://i.discogs.com/drkHvOIJm0J1fhrh7wlCBrrYM0thbJW218GuTARuvME/rs:fit/g:sm/q:90/h:387/w:327/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTI5OTk3/MDAtMTU4MDk2NTE3/Ny03Nzg5LnBuZw.jpeg');
insert into interprete values (null,'Carlos','Gardel','Argentina','https://i.discogs.com/YhoNw0Qm-hKgNwr8NLdbI9PgqRZaN6ZKPhdBEiOqzbU/rs:fit/g:sm/q:90/h:627/w:513/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM5Mjc3/OS0xMzYwNDc1Mzg3/LTY3ODguanBlZw.jpeg');
insert into interprete values (null,'Aztor','Piazzolla','Argentina','https://i.discogs.com/S19BSBNeZC9mxmcAvDekRr35-VahSlU1q1UqblgFeps/rs:fit/g:sm/q:90/h:367/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTE2MjU2/NC0xNjA0MzY0NTU5/LTIxMjMuanBlZw.jpeg');
insert into interprete values (null,'Michael','Jackson','USA','https://i.discogs.com/10-puAu0pWTplVoYjyZ1LfFRZKZkL3bYj3XiUt74z2s/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTE1ODg1/LTE1NDY1OTA3NDYt/NDc4Ni5qcGVn.jpeg');
insert into interprete values (null,'Luis Miguel','Gallego Basteri','Mexico','https://i.discogs.com/9qDr-wBzScFY39x6DH-sIJ1wovsi8-1MhoaK8YKRMMk/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTkyNzkz/LTE2NTY4OTk3NjMt/ODM5My5qcGVn.jpeg');
insert into interprete values (null,'José Luis','Perales','España','https://i.discogs.com/zs8EECy0HdtZTGWJhnRvm2QoROrIn7ScR1Vxtq9g1og/rs:fit/g:sm/q:90/h:353/w:351/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTMxNDc2/Ni0xNTI2NjE3MzE0/LTg0MDAucG5n.jpeg');
insert into interprete values (null,'Julio','Iglesias','España','https://i.discogs.com/aEnhIuIlX6IpgxtGsqU_LyL5J9r3cC_bd7RWy_WJleA/rs:fit/g:sm/q:90/h:600/w:596/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE3NzQ4/NDQtMTI1NzMxMDQ2/Mi5qcGVn.jpeg');
insert into interprete values (null,'Rosana','Arbelo Gopar','España','https://i.discogs.com/gsXBxD3Y7_jHAaBvqAuqyH3brakTLY5OpY0dzxu4nM8/rs:fit/g:sm/q:90/h:346/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTkzMjc5/NS0xNTEzMzYzODkw/LTkzNzguanBlZw.jpeg');


# Carga de Discográficas:
# Discográfica:                 id_album, nombre

insert into discografica values (null,'BMG'),(null,'Sony Music'),(null,'WEA'),(null,'Universal'),(null,'Independiente'),(null,'Epic');


#Carga de Géneros Musicales:
#Genero:				   id_genero, nombre
insert into genero values (null, 'Alternativo'), (null, 'Blues'), (null, 'Bolero'), (null, 'Bossa Nova'), (null, 'Country'), (null, 'Cuarteto');
insert into genero values (null, 'Cumbia'), (null, 'Dance'), (null, 'Disco'), (null, 'Dubstep'), (null, 'Electro'), (null, 'Electrónica');
insert into genero values (null, 'Epic Music'), (null, 'EuroDance'), (null, 'Evevergreen'), (null, 'Experimental'), (null, 'Film Score');
insert into genero values (null, 'Flamenco'), (null, 'Folclore'), (null, 'Folk'), (null, 'Funk'), (null, 'Grunge'), (null, 'Góspel');
insert into genero values (null, 'Gótico'), (null, 'Hard rock'), (null, 'Hardcore'), (null, 'Heavy Metal'), (null, 'Hip hop/Rap');
insert into genero values (null, 'Indie'), (null, 'Industrial'), (null, 'Instrumental'), (null, 'J-Pop'), (null, 'J-Rock'), (null, 'Jazz');
insert into genero values (null, 'K-Pop'), (null, 'MPB'), (null, 'Mambo'), (null, 'Marchas/Himnos'), (null, 'Mariachi'), (null, 'Merengue');
insert into genero values (null, 'Metal'), (null, 'Música Clásica'), (null, 'Música Infantil'), (null, 'Música Instrumental');
insert into genero values (null, 'Música Psicodélica'), (null, 'Música Religiosa'), (null, 'Música Romántica'), (null, 'Música Relajante');
insert into genero values (null, 'Música Melódica'), (null, 'New Age'), (null, 'New Wave'), (null, 'Pop'), (null, 'Pop Rock'), (null, 'Post-Rock');
insert into genero values (null, 'Power-Pop'), (null, 'Punk Rock'), (null, 'R&B'), (null, 'Ranchera'), (null, 'Reggae'), (null, 'Reggaeton');
insert into genero values (null, 'Regional'), (null, 'Rock'), (null, 'Rock Progresivo'), (null, 'Rock and Roll'), (null, 'Rockabilly');
insert into genero values (null, 'Salsa'), (null, 'Samba'), (null, 'Score'), (null, 'Sertanejo'), (null, 'Ska'), (null, 'Soft Rock');
insert into genero values (null, 'Soul'), (null, 'Soundtrack'), (null, 'Tango'), (null, 'Techno'), (null, 'Tecnopop'), (null, 'World Music'), (null,'Zamba');

#Formatos de Musica:
insert into formato values (null,'Compact Disc'),(null,'Cassette'),(null,'Long Play'),(null,'Digital');


# Album:                  id_album, cod_album,   nombre,   id_interprete, id_genero, cant_temas, id_discografica,  id_formato,  fec_lanzamiento,  precio,cantidad,  caratula

insert into album values (null,1234567,'Lêttre à ma Mère'   ,3,31,10,5,3,'1979',1000,2,'https://i.discogs.com/ysGLv4Vy4NY1RNgJDNdcwh76guKX1DOW1XFxKeKA0bo/rs:fit/g:sm/q:90/h:600/w:594/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE0OTk5/NjM3LTE1ODk2NjM2/NzgtMTgxMy5qcGVn.jpeg');
insert into album values (null,1234568,'Las Cosas Que Vives',1,52,12,3,1,'1996',1000,1,'https://i.discogs.com/jZHMPfsMSihrVJOcWG0uVXbxnIv1gDb_akXX87puUbM/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1OTky/ODgtMTIzMTI3OTM4/Ni5qcGVn.jpeg');
insert into album values (null,1234569,'En Tiempo de Amor'  ,2,31,10,1,1,'1993',1000,1,'https://i.discogs.com/hBQ5Rv1hfBuekUxclsrpeGcwqTijuOp9uT8xpdTNh7Q/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTU4MDA3/MzYtMTQwMzAyNjE5/Ny0zNDE0LmpwZWc.jpeg');
insert into album values (null,1234570,'El Piano de América',2,31,10,1,1,'1994',1000,1,'https://i.discogs.com/AsKNRgEy2Sufm2KtIPDMhcS8tVj8cYi2Wv4gmrDpu7U/rs:fit/g:sm/q:90/h:596/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTg3ODE1/OTktMTQ2ODY1NjU4/OS03NDE0LmpwZWc.jpeg');
insert into album values (null,'QE 38112','Thriller'        ,14,52,9,6,3,'1982',1200,5 ,'https://i.discogs.com/t3Gzrzp1_DT27bSfVynl5bCmqWqddfUT5ohPHuUDtyE/rs:fit/g:sm/q:90/h:600/w:597/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE2NTk1/MjctMTY2NDIwNDcy/Mi05NDU4LmpwZWc.jpeg');


# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Lêttre à ma Mère','00:40:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,2,"Mariage D'Amour",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,3,"Souvenirs D'Enfance",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,4,"Nostalgie",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);

# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Wanna Be Startin Somethin','00:06:02','Michael Jackson','Michael Jackson',5,14);
insert into tema values (null,2,'Baby Be Mine','00:04:20','Michael Jackson','Rod Temperton',5,14);
insert into tema values (null,3,'The Girl Is Mine','00:03:42','Michael Jackson','Michael Jackson',5,14);
insert into tema values (null,4,'Thriller','00:05:57','Michael Jackson','Rod Temperton',5,14);
insert into tema values (null,5,'Beat It','00:04:17','Michael Jackson','Michael Jackson',5,14);
insert into tema values (null,6,'Billie Jean','00:04:57','Michael Jackson','Michael Jackson',5,14);
insert into tema values (null,7,'Human Nature','00:04:05','Michael Jackson','John Bettis, Steve Porcaro',5,14);
insert into tema values (null,8,'P.Y.T. (Pretty Young Thing)','00:03:58','Michael Jackson','James Ingram, Quincy Jones',5,14);
insert into tema values (null,9,'The Lady In My Life','00:04:57','Michael Jackson','Rod Temperton',5,14);

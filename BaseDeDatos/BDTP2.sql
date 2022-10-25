#Crear Database:

CREATE DATABASE disqueria			  #CREATE DATABASE devispc_tp2  online
DEFAULT CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_0900_ai_ci';         #COLLATE 'utf8mb4_general_ci'; online

use disqueria;                        #use devispc_tp2; online

create table genero (
    id_genero int not null auto_increment primary key,
    nombre varchar(50) unique not null
);

create table discografica(
    id_discografica int not null auto_increment primary key,
    nombre varchar(50)  unique not null
);

create table formato(
    id_formato int not null auto_increment primary key,
    tipo varchar(50)  unique not null
);

create table interprete(
    id_interprete int not null auto_increment primary key,
    nombre varchar(50) not null,
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
        foreign key(id_album) references album(id_album) ON DELETE CASCADE,
        foreign key(id_interprete) references interprete(id_interprete)
    );
    
ALTER TABLE album ENGINE = InnoDB;
ALTER TABLE discografica ENGINE = InnoDB;
ALTER TABLE formato ENGINE = InnoDB;
ALTER TABLE genero ENGINE = InnoDB;
ALTER TABLE interprete ENGINE = InnoDB;
ALTER TABLE tema ENGINE = InnoDB;

#--------------------------
# Carga de datos de Prueba:
#--------------------------
    
# Carga de Interpretes: 
# Interprete:                  id_interprete,nombre,apellido,nacionalidad,foto
insert into interprete values (null,'Laura','Pausini','Italia','https://lastfm.freetls.fastly.net/i/u/770x0/e90924a4fcee47c683f5193715c53081.jpg');
insert into interprete values (null,'Raúl','DiBlasio','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/281a4b35cd584e1da0af361ae9e70616.jpg');
insert into interprete values (null,'Richard','Clayderman','Francia','https://lastfm.freetls.fastly.net/i/u/770x0/bc39ff172a4d4385ba0bb14214afde72.jpg');
insert into interprete values (null,'Enya','Brennan','Irlanda','https://lastfm.freetls.fastly.net/i/u/770x0/9db4f5d707fe42f0860f9c7b6a0b6c1c.jpg');
insert into interprete values (null,'Vangelis','Papathanassiou','Grecia','https://lastfm.freetls.fastly.net/i/u/770x0/3cf7ec36b82b477b974bfb1f85be3c4f.jpg');
insert into interprete values (null,'Jean Michel','Jarre','Francia','https://lastfm.freetls.fastly.net/i/u/770x0/5cd57aa712dc6ea50361d04e6b9cfd9a.jpg');
insert into interprete values (null,'La Mona','Gimenez','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/db3a080b493a49e28a072e8f688a1f4f.jpg');
insert into interprete values (null,'Chaqueño','Palavecino','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/f0e4468250021c53a36fcfdcab0139ec.jpg');
insert into interprete values (null,'Hermanos','Pimpinela','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/21f47f78fa16f13812d280faf17939ff.jpg');
insert into interprete values (null,'Ulises','Bueno','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/315ae4bbadbfc2543e34e21be555ae07.jpg');
insert into interprete values (null,'Leo','Mattioli','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/772163ad3d85c54388117095f73fbf85.jpg');
insert into interprete values (null,'Carlos','Gardel','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/0c3c224b5c1d68bcaca41a4b66a3ad39.jpg');
insert into interprete values (null,'Aztor','Piazzolla','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/5007daf5b0684c2f970303170059bc58.jpg');
insert into interprete values (null,'Michael','Jackson','USA','https://lastfm.freetls.fastly.net/i/u/770x0/c9c44caa5e1243f23ef5e99d14ca8554.jpg');
insert into interprete values (null,'Luis Miguel','Gallego Basteri','Mexico','https://lastfm.freetls.fastly.net/i/u/770x0/91cfa7835ee20b28aa51e49047a2693f.jpg');
insert into interprete values (null,'José Luis','Perales','España','https://lastfm.freetls.fastly.net/i/u/770x0/e61c59fb9007445786e1cf86edd8a6ee.jpg');
insert into interprete values (null,'Julio','Iglesias','España','https://lastfm.freetls.fastly.net/i/u/770x0/3395183df77747c9bdd533cdc474852c.jpg');
insert into interprete values (null,'Rosana','Arbelo Gopar','España','https://lastfm.freetls.fastly.net/i/u/770x0/b9346a6ee2538656ab5d97c3a34f7da4.jpg');
insert into interprete values (null,'Daria','Zawiałow','Polonia','https://lastfm.freetls.fastly.net/i/u/770x0/e9fc40d6cb9be264198dca70cbd5dee2.jpg');
insert into interprete values (null,'ABBA','ABBA','Suecia','https://lastfm.freetls.fastly.net/i/u/770x0/3cf1a58128e924ad43b4d62153fa6ad2.jpg');
insert into interprete values (null,'Soledad','Pastorutti','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/f9039a6bc34b44c28aaeb5f730c05673.jpg');
insert into interprete values (null,'Abel','Pintos','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/17e919db8770aad5efe00fb811fc0184.jpg');
insert into interprete values (null,'Gustavo','Ceratti','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/1898c40d075c080733a0a8621698c3d0.jpg');
insert into interprete values (null,'Charly','García','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/f5e52e48de795500ab4a560578aa52ef.jpg');
insert into interprete values (null,'Luis Alberto','Spinetta','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/f4a5940a1f874b51a0eb77693f253266.jpg');
insert into interprete values (null,'Soda Stereo','','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/56e163c3ce5e4058c024e15d18436a9f.jpg');
insert into interprete values (null,'Rata Blanca','','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/e02c5b8c28d74ef5a46668f40658bf7a.jpg');
insert into interprete values (null,'Attaque 77','','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/dfcd88da0ae34782a93026028bff1347.jpg');
insert into interprete values (null,'Los Nocheros','','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/f1531ba6208ae89496034a6da9ba1ff3.jpg');
insert into interprete values (null,'Los Tekis','','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/0d226d557e8843629146a7467bf52409.jpg');
insert into interprete values (null,'Peteco','Carabajal','Argentina','https://lastfm.freetls.fastly.net/i/u/770x0/53297a34ba2a4f769993802452d3e3af.jpg');
insert into interprete values (null,'Britney',' Spears','USA','https://lastfm.freetls.fastly.net/i/u/770x0/dee14046912c13a3f74a2dc256f032df.jpg');
insert into interprete values (null,'Christina','Aguilera','USA','https://lastfm.freetls.fastly.net/i/u/770x0/f5c25bd3365e9b45850d926c6272b74d.jpg');
insert into interprete values (null,'Jennifer','Lopez','Puerto Rico','https://lastfm.freetls.fastly.net/i/u/770x0/f0e8f4319ddd4b62cb7a41f7204917e0.jpg');
insert into interprete values (null,'Daft Punk','','Francia','https://lastfm.freetls.fastly.net/i/u/770x0/ae411e2f89d748368a55c0ef36683c58.jpg');
insert into interprete values (null,'Yngwie','Malmsteen','Suecia','https://lastfm.freetls.fastly.net/i/u/770x0/e6c26604d0134e77bdba3f0c68cc3e93.jpg');
insert into interprete values (null,'Iron Maiden','','UK','https://lastfm.freetls.fastly.net/i/u/770x0/b01ec2be3ca1ac95ab00cfa913917f31.jpg');
insert into interprete values (null,'Megadeth','','USA','https://lastfm.freetls.fastly.net/i/u/770x0/9b905399506763de8be77d842ff2820d.jpg');
insert into interprete values (null,'Metallica','','USA','https://lastfm.freetls.fastly.net/i/u/770x0/a02af174f8a65ab8f1987aa0e09f1b97.jpg');
insert into interprete values (null,'Lucho','Gatica','Chile','https://lastfm.freetls.fastly.net/i/u/770x0/e01c13ac3bb1445b8b5e9cacee911c42.jpg');
insert into interprete values (null,'Pedro','Vargas','México','https://lastfm.freetls.fastly.net/i/u/770x0/140e7f666e8b4732a24a90ecbce15acf.jpg');
insert into interprete values (null,'Olga','Guillot','Cuba','https://lastfm.freetls.fastly.net/i/u/770x0/c9e78f8558cb4fe8ac5c5e302fbe8cef.jpg');
insert into interprete values (null,'Taylor','Swift','USA','https://lastfm.freetls.fastly.net/i/u/770x0/a1772dc432a4d3fc0302c76015e1dbfe.jpg');
insert into interprete values (null,'Selena','Gomez','México','https://lastfm.freetls.fastly.net/i/u/770x0/2505b9139761a3f55e2a4a105cadbfe0.jpg');

# Carga de Discográficas:
# Discográfica:                 id_album, nombre

insert into discografica values (null,'BMG'),(null,'Sony Music'),(null,'WEA'),(null,'Universal'),(null,'Independiente'),(null,'Epic'),(null,'Polydor');

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

insert into album values (null,1234567,'Lêttre à ma Mère'   ,3,31,10,5,3,'1979',1000,2,'');
insert into album values (null,1234568,'Las Cosas Que Vives',1,52,12,3,1,'1996',1000,1,'https://lastfm.freetls.fastly.net/i/u/770x0/e469a6abae684ba0cb5004f3db714e88.jpg');
insert into album values (null,1234569,'En Tiempo de Amor'  ,2,31,10,1,1,'1993',1000,1,'https://lastfm.freetls.fastly.net/i/u/770x0/f202cc2c95c74d83a808117ad7943c7c.jpg');
insert into album values (null,1234570,'El Piano de América',2,31,10,1,1,'1994',1000,1,'https://lastfm.freetls.fastly.net/i/u/770x0/6bd1c31fff5626fe476696ffff457207.jpg');
insert into album values (null,'QE 38112','Thriller'        ,14,52,9,6,3,'1982',1200,5 ,'https://lastfm.freetls.fastly.net/i/u/770x0/e5f40ae3767cf5b6184776f97e52b8ca.jpg');
insert into album values (null,'88843053662','Xscape'       ,14,52,8,6,1,'2014',1800,5 ,'https://lastfm.freetls.fastly.net/i/u/770x0/ab67d9a3c3624a16ca334032438752a5.jpg');
insert into album values (null,'EK 40600','Bad'             ,14,52,11,6,1,'1987',1600,5 ,'https://lastfm.freetls.fastly.net/i/u/770x0/8860bfd3ea86680bac8cb2decae33f06.jpg');
insert into album values (null,'EPC 465802 4','Dangerous'    ,14,52,14,6,2,'1991',1100,3 ,'https://lastfm.freetls.fastly.net/i/u/770x0/d667ae4d5428c14d47934dcb8995e84c.jpg');
insert into album values (null,'PD-1-6112','Oxygène'           ,6,12,6,7,3,'1976',880,3 ,'https://lastfm.freetls.fastly.net/i/u/770x0/f581b28d23844ef2a1e6ee06e705eddd.jpg');
insert into album values (null,'POLD 5007','Equinoxe'          ,6,12,8,7,3,'1978',890,3 ,'https://lastfm.freetls.fastly.net/i/u/770x0/fde442bced3443c8a04fceac8590ea8a.jpg');
insert into album values (null,'19075833892','Geometry Of Love',6,12,6,2,1,'1976',880,3 ,'https://lastfm.freetls.fastly.net/i/u/770x0/4b642b94a7b848b2915577b3258e0f14.jpg');

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

# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'WLove Never Felt So Good','00:03:54','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,2,'Chicago','00:04:05','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,3,'Loving You','00:03:15','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,4,'A Place With No Name','00:05:35','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,5,'Slave To The Rhythm','00:04:15','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,6,'Do You Know Where Your Children Are','00:04:36','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,7,'Blue Gangsta','00:04:14','Michael Jackson','Michael Jackson',6,14);
insert into tema values (null,8,'Xscape','00:04:04','Michael Jackson','Michael Jackson',6,14);


# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Bad','00:04:06','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,2,'The Way You Make Me Feel','00:04:59','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,3,'Speed Demon','00:04:01','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,4,'Liberian Girl','00:03:53','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,5,'Just Good Friends','00:04:05','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,6,'Another Part Of Me','00:03:53','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,7,'Man In The Mirror','00:05:18','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,8,'I Just Cant Stop Loving You','00:04:24','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,9,'Dirty Diana','00:04:52','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,10,'Smooth Criminal','00:04:16','Michael Jackson','Michael Jackson',7,14);
insert into tema values (null,11,'Leave Me Alone','00:04:37','Michael Jackson','Michael Jackson',7,14);

# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Jam','00:05:38','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,2,'Why You Wanna Trip On Me','00:05:24','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,3,'In The Closet','00:06:31','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,4,'She Drives Me Wild','00:03:41','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,5,'Remember The Time','00:04:00','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,6,'Cant Let Her Get Away','00:05:01','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,7,'Heal The World','00:06:23','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,8,'Black Or White','00:04:15','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,9,'Who Is It','00:06:35','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,10,'Give In To Me','00:05:28','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,11,'Will You Be There','00:07:39','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,12,'Keep The Faith','00:05:56','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,13,'Gone Too Soon','00:03:22','Michael Jackson','Michael Jackson',8,14);
insert into tema values (null,14,'Dangerous','00:07:00','Michael Jackson','Michael Jackson',8,14);

# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Oxygene (Part I)','00:07:40','Jean Michel Jarre','Jean Michel Jarre',9,6);
insert into tema values (null,2,'Oxygene (Part II)','00:08:10','Jean Michel Jarre','Jean Michel Jarre',9,6);
insert into tema values (null,3,'Oxygene (Part III)','00:02:50','Jean Michel Jarre','Jean Michel Jarre',9,6);
insert into tema values (null,4,'Oxygene (Part IV)','00:04:08','Jean Michel Jarre','Jean Michel Jarre',9,6);
insert into tema values (null,5,'Oxygene (Part V)','00:10:31','Jean Michel Jarre','Jean Michel Jarre',9,6);
insert into tema values (null,6,'Oxygene (Part VI)','00:06:16','Jean Michel Jarre','Jean Michel Jarre',9,6);

# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Equinoxe Part 1','00:02:23','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,2,'Equinoxe Part 2','00:05:13','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,3,'Equinoxe Part 3','00:05:04','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,4,'Equinoxe Part 4','00:06:45','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,5,'Equinoxe Part 5','00:03:59','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,6,'Equinoxe Part 6','00:03:09','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,7,'Equinoxe Part 7','00:07:18','Jean Michel Jarre','Jean Michel Jarre',10,6);
insert into tema values (null,8,'Equinoxe Part 8','00:05:06','Jean Michel Jarre','Jean Michel Jarre',10,6);

# Temas del Disco:     id_tema, track_num,titulo,duracion,autor,compositor,id_album,id_interprete
insert into tema values (null,1,'Pleasure Principle','00:06:15','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,2,'Geometry Of Love Part 1','00:03:51','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,3,'Soul Intrusion','00:04:45','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,4,'Electric Flesh','00:06:01','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,5,'Skin Paradox','00:06:17','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,6,'Velvet Road','00:05:55','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,7,'Near Djaina','00:05:02','Jean Michel Jarre','Jean Michel Jarre',11,6);
insert into tema values (null,8,'Geometry Of Love Part 2','00:04:06','Jean Michel Jarre','Jean Michel Jarre',11,6);
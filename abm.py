# Modulo de funcion de carga de datos.
import conexion

#Clases y metodos de cada tabla de la BD:
#------------------------------------------------------------------------------------------------------

class Album():
    def __init__(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula) -> None:

        self.id_album = id_album
        self.cod_album = cod_album
        self.nombre = nombre
        self.id_interprete = id_interprete
        self.id_genero = id_genero
        self.cant_temas = cant_temas
        self.id_discografica = id_discografica
        self.id_formato = id_formato
        self.fec_lanzamiento = fec_lanzamiento
        self.precio = precio
        self.cantidad = cantidad
        self.caratula = caratula

    def getId_album(self):
        return self.id_album
    def getCod_album(self):
        return self.cod_album
    def getNombre(self):
        return self.nombre
    def getId_interprete(self):
        return self.id_interprete
    def getId_genero(self):
        return self.id_genero
    def getCant_temas(self):
        return self.cant_temas
    def getId_discografica(self):
        return self.id_discografica
    def getId_formato(self):
        return self.id_formato
    def getFec_lanzamiento(self):
        return self.fec_lanzamiento
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cantidad
    def getCaratula(self):
        return self.caratula

    def setId_album(self,id_album):
        self.id_album = id_album
    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setNombre(self,nombre):
        self.nombre = nombre
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete
    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setCant_temas(self,cant_temas):
        self.cant_temas = cant_temas
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setFec_lanzamiento(self,fec_lanzamiento):
        self.fec_lanzamiento = fec_lanzamiento
    def setPrecio(self,precio):
        self.precio = precio
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def setCaratula(self,caratula):
        self.caratula = caratula

    def __str__(self) -> str:
        return str(self.id_album) +' '+ str(self.cod_album) +' '+ str(self.nombre) +' '+ str(self.id_interprete) +' '+ str(self.id_genero) +' '+ str(self.cant_temas) +' '+ str(self.id_discografica) +' '+ str(self.id_formato) +' '+ self.fec_lanzamiento +' '+ str(self.precio) +' '+ str(self.cantidad) +' '+ str(self.caratula)

    
#------------------------------------------------------------------------------------------------------

class Discografica():
    def __init__(self,id_discografica,nombre) -> None:
        self.id_discografica = id_discografica
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_discografica)+' '+self.nombre

    def getId_discografica(self):
        return self.id_discografica
    def getNombre(self):
        return self.nombre
    
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setNombre(self,nombre):
        self.nombre = nombre

#------------------------------------------------------------------------------------------------------


class Formato():
    def __init__(self,id_formato,tipo) -> None:
        self.id_formato = id_formato
        self.tipo = tipo

    def __str__(self) -> str:
        return str(self.id_formato)+' '+self.tipo

    def getId_formato(self):
        return self.id_formato
    def getTipo(self):
        return self.tipo

    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setTipo(self,tipo):
        self.tipo = tipo

#------------------------------------------------------------------------------------------------------

class Genero():
    def __init__(self,id_genero,nombre) -> None:
        self.id_genero = id_genero
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_genero)+' '+self.nombre

    def getId_genero(self):
        return self.getId_genero
    def getNombre(self):
        return self.nombre

    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setNombre(self,nombre):
        self.nombre = nombre

#------------------------------------------------------------------------------------------------------

class Interprete():     

    def __init__(self,id_interprete,nombre,apellido,nacionalidad,foto) -> None:
        self.id_interprete = id_interprete
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.foto = foto

    def getId_Interprete(self):
        return self.id_interprete
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getNacionalidad(self):
        return self.nacionalidad
    def getFoto(self):
        return self.foto

    def setId_Interprete(self,idInterprete):
        self.id_interprete = idInterprete
    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellido(self,apellido):
        self.apellido = apellido
    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad
    def setFoto(self,foto):
        self.foto = foto

    def __str__(self) -> str:
        return str(self.id_interprete)+' '+self.nombre+' '+self.apellido+' '+self.nacionalidad+' '+self.foto


#------------------------------------------------------------------------------------------------------


class Tema():
    def __init__(self,id_tema,track_num,titulo,duracion,autor,compositor,id_album,id_interprete) -> None:
        self.id_tema = id_tema
        self.track_num = track_num
        self.titulo = titulo
        self.duracion = duracion
        self.autor = autor
        self.compositor = compositor
        self.id_album = id_album
        self.id_interprete = id_interprete

    def getId_tema(self):
        return self.id_tema
    def getTrack_num(self):
        return self.track_num
    def getTiulo(self):
        return self.titulo
    def getDuracion(self):
        return self.duracion
    def getAutor(self):
        return self.autor
    def getCompositor(self):
        return self.compositor
    def getId_album(self):
        return self.id_album
    def getId_interprete(self):
        return self.id_interprete

    def setId_tema(self,id_tema):
        self.id_tema = id_tema
    def setTrack_num(self,track_num):
        self.track_num = track_num
    def setTitulo(self,titulo):
        self.titulo = titulo
    def setDuracion(self,duracion):
        self.duracion = duracion
    def setAutor(self,autor):
        self.autor = autor
    def setCompositor(self,compositor):
        self.compositor = compositor
    def setId_album(self,id_album):
        self.id_album = id_album
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete

    def __str__(self) -> str:
        return str(self.id_tema)+ ' ' +self.track_num+' '+self.titulo+' '+str(self.duracion)+' '+self.autor+' '+self.compositor+' '+str(self.id_album)+' '+str(self.id_interprete)
    

#---------------------------------------------------------------------------------------

class Cargar(conexion.BaseDatos):
    def __init__(self):
        #print("[ABM] Instanciada Clase de Carga de datos..")  # Print Debug
        conexion.BaseDatos.__init__(self)
    

    #Nico - Cargar un Album.
    def CargarAlbum(self,album):     
        # Album:   id_album, cod_album,   nombre,   id_interprete, id_genero, cant_temas, id_discografica,  id_formato,  fec_lanzamiento,  precio,cantidad,  caratula

        self.query = "INSERT IGNORE INTO album VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"  #Evitamos cargar duplicado.

        self.data = (album.getCod_album(),
        album.getNombre(),
        album.getId_interprete(),
        album.getId_genero(),
        album.getCant_temas(),
        album.getId_discografica(),
        album.getId_formato(),
        album.getFec_lanzamiento(),
        album.getPrecio(),
        album.getCantidad(),
        album.getCaratula())


        self.Conectar()

        self.datos = self.abmSQL(self.query,self.data)   #Enviamos Query y Tupla, el metodo abm es el que posee el commit. y se desconecta al terminar.

        print("[ABM] Ejecutada CARGA de un Album.") #Si ya esta cargado, o si se cargó el registro.

#----------------------------------------------------------------------------------

    def ModificarAlbum(self,album,id_albumModificado): #Edgar G.

        self.id_albumModificado = id_albumModificado

        #  id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula

        self.query = ("""UPDATE album
                        SET cod_album=%s, nombre=%s, id_interprete=%s, id_genero=%s, cant_temas=%s,id_discografica=%s,id_formato=%s,fec_lanzamiento=%s,precio=%s,cantidad=%s,caratula=%s
                        WHERE id_album = """) + "'" + str(self.id_albumModificado) + "'"


        self.data = (album.getCod_album(),
        album.getNombre(),
        album.getId_interprete(),
        album.getId_genero(),
        album.getCant_temas(),
        album.getId_discografica(),
        album.getId_formato(),
        album.getFec_lanzamiento(),
        album.getPrecio(),
        album.getCantidad(),
        album.getCaratula())

        self.Conectar()

        self.datos = self.abmSQL(self.query,self.data)   #Enviamos Query y Tupla, el metodo abm es el que posee el commit. y se desconecta al terminar.

        print("[ABM] Ejecutada MODIFICACION de un Album.") #Si ya esta cargado, o si se cargó el registro.


#----------------------------------------------------------------------------------


    def EliminarAlbum(self,id_album): # Recibimos solo la id_album para eliminarlo.
        #Preparamos la tupla
        self.id_album = id_album
        self.query = "DELETE FROM album WHERE id_album = %s"
        self.data = (id_album,)

        #Conectamos y enviamos:
        self.Conectar()
        self.run = self.abmSQL(self.query,self.data)
        print("[ABM] Solicitando ELIMINACION del Album..")  #print debug
        
        #Se desconecta automaticamente luego de hacer la operacion, ver modulo conexion.py.


#----------------------------------------------------------------------------------

    def CargarInterprete(self,nombre,apellido,nacionalidad,foto):

        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.foto = foto
        
        self.query = "INSERT IGNORE INTO interprete VALUES(null,%s,%s,%s,%s)"  #Evitamos cargar duplicado.
        self.data = (self.nombre,self.apellido,self.nacionalidad,self.foto) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.
 
        self.Conectar()
        self.run = self.abmSQL(self.query,self.data)
        #print("[ABM] Ejecutada carga de un Interprete..")  #print debug

        #Se desconecta automaticamente luego de hacer la operacion, ver modulo conexion.py.

#----------------------------------------------------------------------------------
    def ModificarInterprete(self,interprete,id_interpreteModificado): 

        self.id_interpreteModificado = id_interpreteModificado

        self.query = ("""UPDATE IGNORE interprete
                        SET nombre=%s, apellido=%s, nacionalidad=%s, foto= %s
                        WHERE id_interprete = """) + "'" + str(self.id_interpreteModificado) + "'"

        self.data = (
            interprete.getNombre(),
            interprete.getApellido(),
            interprete.getNacionalidad(),
            interprete.getFoto(),
        )

        self.Conectar()

        self.datos = self.abmSQL(self.query,self.data)   #Enviamos Query y Tupla, el metodo abm es el que posee el commit. y se desconecta al terminar.

        print("[ABM] Ejecutada MODIFICACION de un Interprete.") #Si ya esta cargado, o si se cargó el registro.

#-----------------------------------------------------------------------------------------------------------------------------------------------------

    def CargarGenero(self,nombre): #Cargar un Género musical.    
        # Tabla Interprete:  id_interprete(autoincremental),nombre,apellido,nacionalidad,foto
        self.nombre = nombre

        self.query = "INSERT IGNORE INTO genero VALUES(null,%s)"  #Evitamos cargar duplicado.
        self.data = (nombre,) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.

        self.Conectar()

        self.run = self.abmSQL(self.query,self.data)
        #print("[ABM] Ejecutada carga de un Género..")  #print debug

        #Se desconecta automaticamente luego de hacer la operacion, ver modulo conexion.py.

#----------------------------------------------------------------------------------


    def CargarFormato(self,tipo): #Cargar un Formato musical.    
        self.tipo = tipo

        self.query = "INSERT IGNORE INTO formato VALUES(null,%s)"  #Evitamos cargar duplicado.
        self.data = (tipo,) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.

        self.Conectar()

        self.run = self.abmSQL(self.query,self.data)
        #print("[ABM] Ejecutada carga de un Formato..")  #print debug

        #Se desconecta automaticamente luego de hacer la operacion, ver modulo conexion.py.

#----------------------------------------------------------------------------------


    def CargarDiscografica(self,nombre): #Cargar un Formato musical.    
        self.nombre = nombre
        
        self.query = "INSERT IGNORE INTO discografica VALUES(null,%s)"  #Evitamos cargar duplicado.

        self.data = (nombre,) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.

        self.Conectar()

        self.run = self.abmSQL(self.query,self.data)
        #print("[ABM] Ejecutada carga de una Discografica..")  #print debug

        #Se desconecta automaticamente luego de hacer la operacion, ver modulo conexion.py.


#---------------------------------------------------------------------------------------------------------------------------

    def CargarCancion(self,Tema):     
        # Tema:   tema.id_tema, tema.track_num, tema.titulo, tema.duracion, tema.autor,tema.compositor,tema.id_album,tema.id_interprete
        #self,id_tema,track_num,titulo,duracion,autor,compositor,id_album,id_interprete

        self.query = "INSERT IGNORE INTO tema VALUES(null,%s,%s,%s,%s,%s,%s,%s);"  #Evitamos cargar duplicado.

        self.data = (Tema.getTrack_num(),
        Tema.getTiulo(),
        Tema.getDuracion(),
        Tema.getAutor(),
        Tema.getCompositor(),
        Tema.getId_album(),
        Tema.getId_interprete())


        self.Conectar()

        self.datos = self.abmSQL(self.query,self.data)   #Enviamos Query y Tupla, el metodo abm es el que posee el commit. y se desconecta al terminar.

        print("[ABM] Ejecutada CARGA de una cancion") #Si ya esta cargado, o si se cargó el registro.

#----------------------------------------------------------------------------------------------------------------------

    def ModificarCancion(self,tema, idTemaModificado):     
        self.idTemaModificado = idTemaModificado

        self.query = ("""UPDATE tema
                        SET track_num=%s, titulo=%s, duracion=%s, autor= %s, compositor=%s, id_album=%s, id_interprete=%s
                        WHERE id_tema = """) + "'" + str(self.idTemaModificado) + "'"


        self.data = (
            tema.getTrack_num(),
            tema.getTiulo(),
            tema.getDuracion(),
            tema.getAutor(),
            tema.getCompositor(),
            tema.getId_album(),
            tema.getId_interprete(),
        )

        self.Conectar()

        self.datos = self.abmSQL(self.query,self.data)   #Enviamos Query y Tupla, el metodo abm es el que posee el commit. y se desconecta al terminar.

        print("[ABM] Ejecutada MODIFICACION de una Cancion.") #Si ya esta cargado, o si se cargó el registro.

#--------------------------------------------------------------------------------------------

#Cargar Album:

# test = Cargar()

# info      = Album(0,765434,'El Sol de Mañana',5,45,4,4,4,2022,1222.0,3,"www.imagen.com/imagen.jpg")
# AComoAmor = Album(0,456783,'A Como Amor',3,5,10,5,3,'1978',899.99,3,"www.imagen.com/imagen.jpg")

# test.CargarAlbum(AComoAmor)

#----------------------------------------------------------------------------------------------------------------------

#Cargar Una cancion a un album.

# objeto = Cargar()

# unacancion = Tema(0,4,"Cancion 1",'',"Autor X","Compositor X",4,2) #Almacenamos el objeto con los parametros de sus propiedades

# objeto.CargarCancion(unacancion)

#----------------------------------------------------------------------------------------------------------------------

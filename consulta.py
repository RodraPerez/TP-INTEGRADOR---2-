#Modulo con Clases Para consultar la Base de Datos, Usamos modulo de conexion que tiene los parametros del connector de MySQL.

import conexion


class Listar(conexion.BaseDatos): # Heredaremos de la clase BaseDeDatos almacenada en modulos para acceder a sus metodos y propiedades.
    def __init__(self):
        #print("[CONSULTA] Instanciada Clase Listar...")  # Print Debug
        conexion.BaseDatos.__init__(self)

#----------------------------------------------------------------------------------------------------------

    def ArtistaEspecifico(self,nombre,apellido):      #Edgar G - Busqueda Albums por Artista
        self.nombre = nombre
        self.apellido = apellido

        self.query =""" SELECT album.nombre, interprete.nombre, interprete.apellido,album.cant_temas, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento,album.precio,album.cantidad,discografica.nombre,album.caratula,album.id_album,album.id_interprete,album.id_genero,album.id_discografica,album.id_formato
        FROM album
        INNER JOIN interprete
        ON album.id_interprete = interprete.id_interprete
        INNER JOIN genero
        ON album.id_genero = genero.id_genero
        INNER JOIN formato
        ON album.id_formato = formato.id_formato
        INNER JOIN discografica
        ON album.id_discografica = discografica.id_discografica
        WHERE interprete.nombre = """  + "'" + self.nombre + "'" + " AND interprete.apellido = " + "'" + self.apellido  + "'" + " ORDER BY album.nombre ASC;"
        
        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Albumes por búsqueda por Interprete.") #print debug
        self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.

#----------------------------------------------------------------------------------------------------------

    def GeneroEspecifico(self, NombreGenero): #Leo Torres
        self.NombreGenero = NombreGenero
        self.query = """SELECT album.id_album,album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento,album.precio,album.cantidad
        FROM album 
        JOIN interprete
        ON album.id_interprete = interprete.id_interprete
        JOIN genero
        ON genero.id_genero = album.id_genero
        JOIN formato
        ON formato.id_formato = album.id_formato
        WHERE genero.nombre LIKE """ + "'%" + self.NombreGenero + "%'" + " ORDER BY genero.nombre ASC;"
         
        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Albums por Género.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#----------------------------------------------------------------------------------------------------------

    def NombreAlbumEspecifico(self, nombre):
        self.nombre = nombre
        self.query = """SELECT album.id_album, album.cod_album, album.nombre, album.cant_temas, album.fec_lanzamiento, album.precio, album.cantidad, album.caratula, interprete.foto, interprete.nombre, interprete.apellido,genero.nombre,formato.tipo,tema.track_num, tema.titulo, tema.duracion
        FROM album
        INNER JOIN interprete
        ON album.id_interprete = interprete.id_interprete
        INNER JOIN genero
        ON album.id_genero = genero.id_genero
        INNER JOIN formato
        ON album.id_formato = formato.id_formato
		LEFT JOIN tema
        ON album.id_album = tema.id_album
        WHERE album.nombre = """ + "'" + self.nombre + "'"

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Albums por Nombre del Album.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#----------------------------------------------------------------------------------------------------------

    def idAlbumEspecifico(self, idAlbum):
        self.idAlbum = idAlbum
        self.query = """SELECT album.id_album, album.cod_album, album.nombre, album.id_interprete, album.id_genero, album.cant_temas, album.id_discografica, album.id_formato, album.fec_lanzamiento, album.precio, album.cantidad, album.caratula
        FROM album
        WHERE album.id_album = """ + "'" + str(self.idAlbum) + "'"
        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Album por id del Album.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        #print(self.datos)
        return self.datos

#----------------------------------------------------------------------------------------------------------

    def ListaAlbumesCompleta(self):
        self.query = """SELECT album.nombre, interprete.nombre, interprete.apellido,album.cant_temas, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento,album.precio,album.cantidad,discografica.nombre,album.caratula,album.id_album,album.id_interprete,album.id_genero,album.id_discografica,album.id_formato
        FROM album
        INNER JOIN interprete
        ON album.id_interprete = interprete.id_interprete
        INNER JOIN genero
        ON album.id_genero = genero.id_genero
        INNER JOIN formato
        ON album.id_formato = formato.id_formato
        INNER JOIN discografica
        ON album.id_discografica = discografica.id_discografica
        WHERE album.id_interprete = interprete.id_interprete
        ORDER By interprete.nombre ASC"""  #Por apellido descendente

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Albums por Artista") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos






#----------------------------------------------------------------------------------------------------------
# consultas de una sola tabla sin parametros:
#----------------------------------------------------------------------------------------------------------


    def ListaGenerosCompleta(self):

        self.query ="SELECT genero.id_genero, genero.nombre FROM genero ORDER BY genero.nombre ASC"

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Lista de géneros.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#---------------------------------------------------------------------------------------------------------
    
     
    def ListaInterpretesCompleta(self): #Nico
        self.query ="""SELECT i.id_interprete, i.nombre, i.apellido, i.nacionalidad, i.foto
                    FROM interprete 
                    AS i
                    ORDER BY i.nombre ASC;"""

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Lista de Intérpretes..") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos




#----------------------------------------------------------------------------------------------------------

    def ListaDiscograficasCompleta(self):

        self.query ="""SELECT d.id_discografica, d.nombre
                    FROM discografica 
                    AS d
                    ORDER BY d.nombre ASC;"""

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Lista de Discograficas.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#----------------------------------------------------------------------------------------------------------
    
    def ListaFormatosCompleta(self):

        self.query ="""SELECT f.id_formato, f.tipo
                    FROM formato 
                    AS f
                    ORDER BY f.tipo ASC;"""

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Lista de Formatos.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos


#----------------------------------------------------------------------------------------------------------
    
    def ListaTemasCompleta(self):

        self.query ="SELECT * FROM tema ORDER BY tema.id_album ASC;"

        #Conexion a Base de Datos:
        self.Conectar()
        #print("[CONSULTA] Ejecutada consulta Lista de Temas.") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        #print(self.datos) test
        return self.datos


#-----------------------------------------------------------------------------------------------------------












#------------------------------------------------------------------------------------------------------
#Tests
#-------------------------------------------------------------------------------------------------------

# instancia = Listar()
# idalbum = 14
# instancia.idAlbumEspecifico(idalbum)
#Modulo con Clases Para consultar la Base de Datos, Usamos modulo de conexion que tiene los parametros del connector de MySQL.

import conexion


class Listar(conexion.BaseDatos): # Heredaremos de la clase BaseDeDatos almacenada en modulos para acceder a sus metodos y propiedades.
    def __init__(self):
        print("Instanciada Clase Listar...")  # Print Debug
        conexion.BaseDatos.__init__(self)

#-----------------------------------------------------------------------------------------------------------------------

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
        print("\033[1mEjecutada consulta Albumes por búsqueda por Interprete.\033[0m") #print debug
        self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.

#-----------------------------------------------------------------------------------------------------------------------

    def GeneroEspecifico(self, NombreGenero): #Leo Torres
        self.NombreGenero = NombreGenero
        self.query = """SELECT album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento,album.id_album
        FROM album 
        JOIN interprete
        ON album.id_interprete = interprete.id_interprete
        JOIN genero
        ON genero.id_genero = album.id_genero
        JOIN formato
        ON formato.id_formato = album.id_formato
        WHERE genero.nombre = """ + "'" + self.NombreGenero + "'" + " ORDER BY genero.nombre ASC;"
                    
        #Conexion a Base de Datos:
        self.Conectar()
        print("\033[1mEjecutada consulta Albums por Género.\033[0m") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#-----------------------------------------------------------------------------------------------------------------------

    def NombreAlbumEspecifico(self, nombre):
        self.nombre = nombre
        self.query = """SELECT tema.track_num, tema.titulo, tema.duracion, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento, album.caratula, interprete.foto, album.precio, album.cantidad, album.cant_temas
        FROM album
        INNER JOIN tema
        ON album.id_album = tema.id_album
        INNER JOIN interprete
        ON album.id_interprete = interprete.id_interprete
        INNER JOIN genero
        ON album.id_genero = genero.id_genero
        INNER JOIN formato
        ON album.id_formato = formato.id_formato
        WHERE album.nombre =""" + "'" + self.nombre + "'"

        #Conexion a Base de Datos:
        self.Conectar()
        print("\033[1mEjecutada consulta Albums por Nombre del Album.\033[0m") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#-----------------------------------------------------------------------------------------------------------------------

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
        print("\033[1mEjecutada consulta Albums por Artista (consigna).\033[0m") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos


#-----------------------------------------------------------------------------------------------------------------------
# consultas de una sola tabla sin parametros:
#-----------------------------------------------------------------------------------------------------------------------


    def ListaGenerosCompleta(self):

        self.query ="SELECT genero.id_genero, genero.nombre FROM genero ORDER BY genero.nombre ASC"

        #Conexion a Base de Datos:
        self.Conectar()
        print("\033[1mEjecutada consulta Lista de géneros.\033[0m") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos

#-----------------------------------------------------------------------------------------------------------------------
    
     
    def ListaInterpretesCompleta(self): #Nico
        self.query ="""SELECT i.id_interprete, i.nombre, i.apellido, i.nacionalidad, i.foto
                    FROM interprete 
                    AS i
                    ORDER BY i.nombre ASC;"""

        #Conexion a Base de Datos:
        self.Conectar()
        print("\033[1mEjecutada consulta Lista de Intérpretes..\033[0m") #print debug
        self.datos = self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
        return self.datos




#-----------------------------------------------------------------------------------------------------------------------
# PENDIENTES:
#-----------------------------------------------------------------------------------------------------------------------    
    # def ListaDiscograficasCompleta(self):

    #     self.query =""  <-------------------------------

    #     #Conexion a Base de Datos:
    #     self.Conectar()
    #     print("\033[1mEjecutada consulta Lista de Discograficas.\033[0m") #print debug
    #     self.datos = self.QuerySQL(self.query)
    #     #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
    #     return self.datos

#-----------------------------------------------------------------------------------------------------------------------
    
    # def ListaFormatosCompleta(self):

    #     self.query =""  <-------------------------------

    #     #Conexion a Base de Datos:
    #     self.Conectar()
    #     print("\033[1mEjecutada consulta Lista de Formatos.\033[0m") #print debug
    #     self.datos = self.QuerySQL(self.query)
    #     #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.
    #     return self.datos

#-----------------------------------------------------------------------------------------------------------------------
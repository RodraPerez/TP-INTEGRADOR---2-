#Modulo con Clases Para consultar la Base de Datos, Usamos modulo de conexion que tiene los parametros del connector de MySQL.

import conexion


class ListarAlbums(conexion.BaseDatos): # Heredaremos de la clase BaseDeDatos almacenada en modulos para acceder a sus metodos y propiedades.
    def __init__(self):
        print("Instanciada Clase ListarAlbums...")  # Print Debug
        conexion.BaseDatos.__init__(self)


    def PorArtista(self,nombre,apellido):      #Edgar G - Busqueda Albums por Artista
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
        print("\033[1mEjecutada consulta Albums por Interprete.\033[0m") #print debug
        self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.

    
    def PorGenero(self, NombreGenero):
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
        self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.


#-----------------------------------------------------------------------------------------------------------------------
# consultas de una sola tabla sin parametros:
#-----------------------------------------------------------------------------------------------------------------------
    
class ListarGeneros(conexion.BaseDatos):
    def __init__(self):
        print("Instanciada Clase ListarGeneros..")  # Print Debug
        conexion.BaseDatos.__init__(self)

         
    def ListaCompleta(self):

        self.query =" "  # <------------------------- PONER SENTENCIA SQL

        #Conexion a Base de Datos:
        self.Conectar()
        print("\033[1mEjecutada consulta Lista de géneros.\033[0m") #print debug
        self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.



#-----------------------------------------------------------------------------------------------------------------------
# PENDIENTES:
#-----------------------------------------------------------------------------------------------------------------------    
# class ListarDiscograficas(conexion.BaseDatos):
#     def __init__(self):
#         print("Instanciada Clase ListarDiscograficas..")  # Print Debug
#         conexion.BaseDatos.__init__(self)        

#     def ListaCompleta(self):
#         pass

#-----------------------------------------------------------------------------------------------------------------------
    
# class ListarFormatos(conexion.BaseDatos):
#     def __init__(self):
#         print("Instanciada Clase ListarFormatos..")  # Print Debug
#         conexion.BaseDatos.__init__(self)        

#     def ListaCompleta(self):
#         pass

#-----------------------------------------------------------------------------------------------------------------------
    
class ListarInterpretes(conexion.BaseDatos): #Nico
    def __init__(self):
        print("Instanciada Clase ListarInterpretes..")  # Print Debug
        conexion.BaseDatos.__init__(self)        

    def ListaCompleta(self):
        self.query ="""SELECT i.id_interprete, i.nombre, i.apellido, i.nacionalidad, i.foto
                    FROM interprete 
                    AS i
                    ORDER BY i.nombre ASC;"""

        #Conexion a Base de Datos:
        self.Conectar()
        print("\033[1mEjecutada consulta Lista de Intérpretes..\033[0m") #print debug
        self.QuerySQL(self.query)
        #Desconexion automatica en el modulo conexion luego de hacer una consulta u otra operacion, ahorramos codigo.


#-----------------------------------------------------------------------------------------------------------------------
    
# class ListarCanciones(conexion.BaseDatos):
#     def __init__(self):
#         print("Instanciada Clase ListarCanciones..")  # Print Debug
#         conexion.BaseDatos.__init__(self)        

#     def ListaCompleta(self):
#         pass
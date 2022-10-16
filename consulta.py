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

        if self.conexion.is_connected():
            try:
                #Cursor y consulta:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)

                #Almacenamos bajada de datos en una Variable Buffer.
                self.listado = self.cursor.fetchall()
                print("\033[1mEjecutada consulta Albums por Interprete.\033[0m") #print debug

                #Desconectamos
                self.Desconectar()

                #return self.listado
                for tupla in self.listado:  #Habilitamos el ciclo solamente para test consola, enviamos listado de tuplas por return a la interfaz.
                     print (tupla)

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
        
    
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

        if self.conexion.is_connected():
            try:
                #Cursor y consulta:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)

                #Almacenamos bajada de datos en una Variable Buffer.
                self.listado = self.cursor.fetchall()
                print("\033[1mEjecutada consulta Albums por Género.\033[0m") #print debug

                #Desconectamos
                self.Desconectar()

                #return self.listado
                for tupla in self.listado:
                        print (tupla)

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)


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

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)
                self.listado = self.cursor.fetchall()
                print("\033[0;34m\033[1mEEjecutada consulta Lista de Generos Musicales..\033[0m") #print debug

                self.Desconectar()

                #return self.listado        #no borrar
                for tupla in self.listado:  #Habilitamos el ciclo solamente para test consola, enviamos listado de tuplas por return a la interfaz.
                        print (tupla)
            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)



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

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)
                self.listado = self.cursor.fetchall()
                print("\033[0;34m\033[1mEjecutada consulta Lista de Interpretes..\033[0m") #print debug

                self.Desconectar()

                #return self.listado        #no borrar
                for tupla in self.listado:  #Habilitamos el ciclo solamente para test consola, enviamos listado de tuplas por return a la interfaz.
                    print (tupla)
            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)


#-----------------------------------------------------------------------------------------------------------------------
    
# class ListarCanciones(conexion.BaseDatos):
#     def __init__(self):
#         print("Instanciada Clase ListarCanciones..")  # Print Debug
#         conexion.BaseDatos.__init__(self)        

#     def ListaCompleta(self):
#         pass
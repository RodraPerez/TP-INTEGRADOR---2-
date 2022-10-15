#Modulo con Clase Para consulta Base de Datos, Usamos modulo de conexion que tiene los parametros del connector de MySQL.

import conexion


class ListarAlbums(conexion.BaseDatos): # Heredaremos de la clase BaseDeDatos almacenada en modulos para acceder a sus metodos y propiedades.
    def __init__(self):
        print("Instanciada Clase ListarAlbums..")  # Print Debug
        conexion.BaseDatos.__init__(self)


    def PorArtista(self,nombre,apellido):      #Edgar G - Busqueda Albums por Artista
        self.nombre = nombre
        self.apellido = apellido

        self.query = """ SELECT album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento
                    FROM album
                    INNER JOIN interprete
                    ON album.id_interprete = interprete.id_interprete
                    INNER JOIN genero
                    ON album.id_genero = genero.id_genero
                    INNER JOIN formato
                    ON album.id_formato = formato.id_formato
                    WHERE interprete.nombre = """ + "'" + self.nombre + "'" + " AND interprete.apellido = " + "'" + self.apellido  + "'" + " ORDER BY album.nombre ASC;"
        
        #Conexion a Base de Datos:
        self.Conectar()

        if self.conexion.is_connected():
            try:
                #Cursor y consulta:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)

                #Almacenamos bajada de datos en una Variable Buffer.
                self.listado = self.cursor.fetchall()
                print("Solicitada consulta por Artista..") #print debug

                #Desconectamos
                self.Desconectar()

                #return self.listado
                for tupla in self.listado:
                     print (tupla)

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
        
    
    def PorGenero(self, NombreGenero):
        self.NombreGenero = NombreGenero
        self.query = """SELECT album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.id_album, formato.tipo, album.fec_lanzamiento
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
                print("Solicitada consulta por Artista..") #print debug

                #Desconectamos
                self.Desconectar()

                #return self.listado
                for tupla in self.listado:
                     print (tupla)

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
         

     
                
    #def OtraMas(self):
        #codigo
    
    #def MasConsultas(self):
        #codigo
        


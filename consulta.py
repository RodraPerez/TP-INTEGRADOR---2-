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

        #Cursor y consulta:
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.query)

        #Almacenamos bajada de datos en una Variable Buffer.
        self.listado = self.cursor.fetchall()
        
        #Desconectamos
        self.Desconectar()

        for tupla in self.listado:
            print (tupla)
        
    


    def PorGenero(self, NombreGenero):
            self.NombreGenero = NombreGenero
            
            self.query = """SELECT g.Nombre, a.Nombre, i.nombre, i.apellido
                            FROM album a 
                            JOIN interprete i ON a.id_interprete = i.id_interprete
                            JOIN genero g ON g.id_genero = a.id_genero
                            WHERE g.nombre = """ + "'" + self.NombreGenero + "'" + " ORDER BY G.NOMBRE ASC;"""
            #Conexion a Base de Datos:
            self.Conectar()

            #Cursor y consulta:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(self.query)

            #Almacenamos bajada de datos en una Variable Buffer.
            self.listado = self.cursor.fetchall()
            
            #Desconectamos
            self.Desconectar()

            for tupla in self.listado:
                print (tupla)
    
    #def OtraMas(self):
        #codigo
    
    #def MasConsultas(self):
        #codigo
        


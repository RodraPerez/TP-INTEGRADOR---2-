#Funciones de formato y salida de texto para estética del CLI consola.


def AlbumsVistaCLI(info): # ordenador de datos, mejora salida de la consulta en crudo para mejor estética.
    resultados = info
    p = 5
    pistaChrLen = 0
    tituloChrLen = 0
    duracionChrLen = 20

    # print(" " * p, str("Pista").ljust(pistaChrLen, ' ')," " * 1,str("Nombre").ljust(tituloChrLen, ' '), " " * p, str("Duracion").ljust(duracionChrLen, ' '))
    print("----")
    print(resultados)
    print("----")
    # print("\n")
    
    #Imprimo resultados se calibran automáticamente de acuerdo al nombre del tema ya que es variable en su longitud.

    # for album in datos:
    #     print(" " * p, album[0]," " * p, str(album[1]).ljust(tituloChrLen, ' '), " " * p  ,album[2])

    for album in resultados:
        print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])







    def MostrarAlbumPorNombre(self,nombre, modo_cli= True):  # Método para consultar la Base de Datos - Edgar G.
        self.modo_cli = modo_cli
        self.nombre = nombre


        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()

                #Hago un INNER JOIN con 5 tablas para obtener la info vinculada, almaceno en una variable como string multilinea para mejor lectura de la sentencia. 
                query = """SELECT tema.track_num, tema.titulo, tema.duracion, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento, album.caratula, interprete.foto
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

                cursor.execute(query)              # Sentencia SQL desde variable
                resultados = cursor.fetchall()     # Buffer del cursor
                self.conexion.close()              
                
                if resultados == []:
                    print("\n No hay registros que coincidan..")                           
                
                else:
                    if self.modo_cli == False:
                        print(resultados)
                    else:    
                    # Antes de mostrar los registros recorro cada indice de la lista de tuplas y se analiza la longitud de cada indice de la tupla como string, para ajustar el texto.
                        for album in resultados:
                            if len(str(album[0])) > self.pistaChrLen:
                                self.pistaChrLen = len(str(album[0]))

                            if len(str(album[1])) > self.tituloChrLen:
                                self.tituloChrLen = len(str(album[1]))

                            if len(str(album[2])) > self.duracionChrLen:
                                self.duracionChrLen = len(str(album[2]))
                        
                        self.p = 5

                        print("\n")

                        print("Album: ", "\033[92m\033[1m",str(album[3]),"\033[0m")
                        print("Cod:    ",  str(album[7]))
                        print("Artista:", str(album[4]),str(album[5]))
                        print("Año:    ", str(album[9]))
                        print("Tipo:   ", str(album[8]))
                        print("Genero: ", str(album[6]))
                        print("\nCanciones del Album:")
                        print("\n")

                        
                        #Apariencia de Tabla, calibrada desde los multiplicadores de caracteres. Se ajusta automático al resultado del album y sus cadenas.                 
                        
                        print(" " * self.p, str("Pista").ljust(self.pistaChrLen, ' ')," " * 1,str("Nombre").ljust(self.tituloChrLen, ' '), " " * self.p, str("Duracion").ljust(self.duracionChrLen, ' '))

                        print("\n")
                        
                        #Imprimo resultados se calibran automáticamente de acuerdo al nombre del tema ya que es variable en su longitud.

                        for album in resultados:
                            print(" " * self.p, album[0]," " * self.p, str(album[1]).ljust(self.tituloChrLen, ' '), " " * self.p  ,album[2])

                        # Muestra liks Web de catalogos populares con detalles del album. Se pasan Parametros de búsqueda a los links mediante variables de los resultados de la consulta.

                        print("\n")
                        print("\nTapa del Disco: ",album[10])
                        print("Foto Interprete:",album[11])
                        print("Spotify Artista:","\033[94m https://open.spotify.com/search/" + str(album[4]) + "%20" + str(album[5]) + "\033[0m")
                        print("Spotify Album:  ","\033[94m https://open.spotify.com/search/album" + "%3A" + str(album[3]) + "\033[0m")
                    
                return
            
            except mysql.connector.Error as conexionError:
                print("No se pudo conectar para hacer la consulta.",conexionError)
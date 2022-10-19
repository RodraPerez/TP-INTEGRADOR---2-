#Funciones de formato y salida de texto para estética del CLI consola y algunas filtros para la interfaz ventana, tambien funciones de control.

import consulta

def AlbumsVistaCLI(): # captura de lista de tuplas del cursor se procesa todo en este modulo.
  
    Listar = consulta.Listar()
    registros = Listar.ListaAlbumesCompleta()

    espaciado = 1
    longalbum = 0
    longnombre = 0
    longapellido = 0
    longgenero = 0
    longalbumcod = 0
    longformato = 0
    longfecha = 0
    longprecio = 0
    longcant = 0
    longdiscograf = 0

    for album in registros:  #Procedimiento para extraer maximos strlen de cada registro
        if len(str(album[0])) > longalbum:
            longalbum = len(str(album[0]))
        if len(str(album[1])) > longnombre:
            longnombre = len(str(album[1]))
        if len(str(album[2])) > longapellido:
            longapellido = len(str(album[2]))
        if len(str(album[4])) > longgenero:
            longgenero = len(str(album[4]))
        if len(str(album[5])) > longalbumcod:
            longalbumcod = len(str(album[5]))
        if len(str(album[6])) > longformato:
            longformato = len(str(album[6]))
        if len(str(album[7])) > longfecha:
            longfecha = len(str(album[7]))
        if len(str(album[8])) > longprecio:
            longprecio = len(str(album[8]))
        if len(str(album[9])) > longcant:
            longcant = len(str(album[9]))
        if len(str(album[10])) > longdiscograf:
            longdiscograf = len(str(album[10]))

    for album in registros:
        #Imprimo resultados se calibran automáticamente de acuerdo a la cadena de long maxima ya que es variable en su longitud en cada columna.
        print(" " * espaciado, str(album[0]).ljust(longalbum, ' ')," " * espaciado, str(album[1]).ljust(longnombre, ' ')," " * espaciado, str(album[2]).ljust(longapellido, ' ')," " * espaciado,str(album[4]).center(longgenero, ' ')," " * espaciado," " * espaciado,str(album[5]).center(longalbumcod, ' ')," " * espaciado," " * espaciado,str(album[6]).ljust(longformato, ' ')," " * espaciado," " * espaciado,str(album[7]).ljust(longfecha, ' ')," " * espaciado," " * espaciado,str(album[8]).ljust(longprecio, ' ')," " * espaciado," " * espaciado,str(album[9]).ljust(longcant, ' ')," " * espaciado," " * espaciado,str(album[10]).ljust(longdiscograf, ' ')," " * espaciado)





def MostrarAlbumPorNombreCLI():
    nombre = input("Ingrese nombre del Album: ")
    pistaChrLen = 0
    tituloChrLen = 0
    duracionChrLen = 0

    Listar = consulta.Listar()
    registros = Listar.NombreAlbumEspecifico(nombre)
            
    if registros == []:
        print("\n No hay registros que coincidan..")                           
    
    else:
        # Antes de mostrar los registros recorro cada indice de la lista de tuplas y se analiza la longitud de cada indice de la tupla como string, para ajustar el texto.
            for album in registros:
                if len(str(album[0])) > pistaChrLen:
                    pistaChrLen = len(str(album[0]))

                if len(str(album[1])) > tituloChrLen:
                    tituloChrLen = len(str(album[1]))

                if len(str(album[2])) > duracionChrLen:
                    duracionChrLen = len(str(album[2]))
            
            espaciado = 5

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
            
            print(" " * espaciado, str("Pista").ljust(pistaChrLen, ' ')," " * 1,str("Nombre").ljust(tituloChrLen, ' '), " " * espaciado, str("Duracion").ljust(duracionChrLen, ' '))

            print("\n")
            
            #Imprimo resultados se calibran automáticamente de acuerdo al nombre del tema ya que es variable en su longitud.

            for album in registros:
                print(" " * espaciado, album[0]," " * espaciado, str(album[1]).ljust(tituloChrLen, ' '), " " * espaciado  ,album[2])

            # Muestra liks Web de catalogos populares con detalles del album. Se pasan Parametros de búsqueda a los links mediante variables de los resultados de la consulta.

            print("\n")
            print("\nTapa del Disco: ",album[10])
            print("Foto Interprete:",album[11])
            print("Spotify Artista:","\033[94m https://open.spotify.com/search/" + str(album[4]) + "%20" + str(album[5]) + "\033[0m")
            print("Spotify Album:  ","\033[94m https://open.spotify.com/search/album" + "%3A" + str(album[3]) + "\033[0m")
        
    return



def MostrarAlbumsPorGenero():
    genero = input("Ingrese el género que quiere listar: ")

    Listar = consulta.Listar()
    registros = Listar.GeneroEspecifico(genero)

    espaciado = 1
    longalbum = 0
    longnombre = 0
    longapellido = 0
    longgenero = 0
    longalbumcod = 0
    longformato = 0
    longfecha = 0

    for album in registros:  #Procedimiento para extraer maximos strlen de cada registro
        if len(str(album[0])) > longalbum:
            longalbum = len(str(album[0]))
        if len(str(album[1])) > longnombre:
            longnombre = len(str(album[1]))
        if len(str(album[2])) > longapellido:
            longapellido = len(str(album[2]))
        if len(str(album[4])) > longgenero:
            longgenero = len(str(album[4]))
        if len(str(album[5])) > longalbumcod:
            longalbumcod = len(str(album[5]))
        if len(str(album[6])) > longformato:
            longformato = len(str(album[6]))
        if len(str(album[7])) > longfecha:
            longfecha = len(str(album[7]))

    for album in registros:
        #Imprimo resultados se calibran automáticamente de acuerdo a la cadena de long maxima ya que es variable en su longitud en cada columna.
        print(" " * espaciado, str(album[0]).ljust(longalbum, ' ')," " * espaciado, str(album[1]).ljust(longnombre, ' ')," " * espaciado, str(album[2]).ljust(longapellido, ' ')," " * espaciado,str(album[4]).center(longgenero, ' ')," " * espaciado," " * espaciado,str(album[5]).center(longalbumcod, ' ')," " * espaciado," " * espaciado,str(album[6]).ljust(longformato, ' ')," " * espaciado," " * espaciado,str(album[7]).ljust(longfecha, ' '))
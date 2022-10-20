#Funciones de formato y salida de texto para estética del CLI consola y algunas filtros para la interfaz ventana, tambien funciones de control.

import consulta
import cargadatos

def AlbumsVistaCLI(): # captura de lista de tuplas del cursor se procesa todo en este modulo.
  
    Listar = consulta.Listar()
    registros = Listar.ListaAlbumesCompleta()

    if registros == []:
        print("\n \033[1m No hay registros que coincidan con su búsqueda..\033[0m")
        return

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

    print("\033[1m")
    print(" " * espaciado, str("Album").ljust(longalbum, ' ')," " * espaciado, str("Nombre").ljust(longnombre, ' ')," " * espaciado, str("Apellido").ljust(longapellido, ' ')," " * espaciado,str("Genero").center(longgenero, ' ')," " * espaciado," " * espaciado,str("Codigo").center(longalbumcod, ' ')," " * espaciado," " * espaciado,str("Formato").ljust(longformato, ' ')," " * espaciado," " * espaciado,str("Año").center(longfecha, ' ')," " * espaciado," " * espaciado,str("Precio").ljust(longprecio, ' ')," " * espaciado," " * espaciado,str("Stock").center(longcant, ' ')," " * espaciado," " * espaciado,str("Sello").ljust(longdiscograf, ' ')," " * espaciado)
    print("\033[0m")
    for album in registros:
        #Imprimo resultados se calibran automáticamente de acuerdo a la cadena de long maxima ya que es variable en su longitud en cada columna.
        print(" " * espaciado, str(album[0]).ljust(longalbum, ' ')," " * espaciado, str(album[1]).ljust(longnombre, ' ')," " * espaciado, str(album[2]).ljust(longapellido, ' ')," " * espaciado,str(album[4]).center(longgenero, ' ')," " * espaciado," " * espaciado,str(album[5]).center(longalbumcod, ' ')," " * espaciado," " * espaciado,str(album[6]).ljust(longformato, ' ')," " * espaciado," " * espaciado,str(album[7]).ljust(longfecha, ' ')," " * espaciado," " * espaciado,str(album[8]).ljust(longprecio, ' ')," " * espaciado," " * espaciado,str(album[9]).ljust(longcant, ' ')," " * espaciado," " * espaciado,str(album[10]).center(longdiscograf, ' ')," " * espaciado)





def MostrarAlbumPorNombreCLI():
    nombre = str(input("Ingrese nombre del Album: "))
    nombre = nombre.strip('\n')  #String, limpieza de espacios ant post.
    nombre = nombre.strip()

    pistaChrLen = 0
    tituloChrLen = 0
    duracionChrLen = 0

    Listar = consulta.Listar()
    registros = Listar.NombreAlbumEspecifico(nombre)
            
    if registros == []:
        print("\n \033[1m No hay registros que coincidan con su búsqueda..\033[0m")
        return                          
    
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



def MostrarAlbumsPorGeneroCLI():
    genero = str(input("Ingrese el género que quiere listar: "))
    genero = genero.strip('\n')  #String, limpieza de espacios ant post, y Capitalizacion.
    genero = genero.strip()
    genero = genero.capitalize()


    Listar = consulta.Listar()
    registros = Listar.GeneroEspecifico(genero)

    if registros == []:
        print("\n \033[1m No hay registros que coincidan con su búsqueda..\033[0m")
        return

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

    print("\n\033[1m")
    print("Usted solicitó listar Albumes del género musical " + genero + ":\n" )
    print(" " * espaciado, str("Album").ljust(longalbum, ' ')," " * espaciado, str("Nombre").ljust(longnombre, ' ')," " * espaciado, str("Apellido").ljust(longapellido, ' ')," " * espaciado,str("Código").ljust(longgenero, ' ')," " * espaciado," " * espaciado,str("Sello").center(longalbumcod, ' ')," " * espaciado," " * espaciado,str("Año").center(longformato, ' ')," " * espaciado," " * espaciado,str("Stock\033[0m").ljust(longfecha, ' '))

    for album in registros:
        print(" " * espaciado, str(album[0]).ljust(longalbum, ' ')," " * espaciado, str(album[1]).ljust(longnombre, ' ')," " * espaciado, str(album[2]).ljust(longapellido, ' ')," " * espaciado,str(album[4]).center(longgenero, ' ')," " * espaciado," " * espaciado,str(album[5]).ljust(longalbumcod, ' ')," " * espaciado," " * espaciado,str(album[6]).ljust(longformato, ' ')," " * espaciado," " * espaciado,str(album[7]).ljust(longfecha, ' '))


def InsertarInterpreteCLI():

    while True:
        print("\n")
        print("Usted está por cargar nuevo Artista o Interprete: \n")

        nombre =        str(input("Escriba Nombre del interprete:                      "))
        apellido =      str(input("Apellido (si no tiene dejar en blanco ej. ABBA):    "))
        nacionalidad =  str(input("Nacionalidad del interprete:                        "))
        foto =          str(input("Foto del interprete (link directo al .jpg .jpeg o .png o puede dejarlo vacio \n Link:  "))
        

        opcion = input("\n Que desea hacer? | 1 (Cargar) | 2 (Reingresar los Datos) | 3 (Cancelar)\nIngrese un número de opción: ")
        
        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = cargadatos.Cargar()
            carga.CargarInterprete(nombre,apellido,nacionalidad,foto)
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            nombre = ""
            apellido = ""
            nacionalidad = ""
            foto = ""

        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  

        else:
            print("¡Opción incorrecta!")



def MostrarInterpreteCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaInterpretesCompleta()

    if registros == []:
        print("\n \033[1m No hay registros que coincidan con su búsqueda..\033[0m")
        return

    #i.id_interprete, i.nombre, i.apellido, i.nacionalidad, i.foto

    espaciado = 1
    longidinterprete = 0
    longnombre = 0
    longapellido = 0
    longnacionalidad = 0

    for artista in registros:
        if len(str(artista[0])) > longidinterprete:
            longidinterprete = len(str(artista[0]))

        if len(str(artista[1])) > longnombre:
            longnombre = len(str(artista[1]))

        if len(str(artista[2])) > longapellido:
            longapellido = len(str(artista[2]))


        if len(str(artista[3])) > longnacionalidad:
            longnacionalidad = len(str(artista[3]))

    print("\n\033[1m")
    print("Usted solicitó listar los Artistas disponibles en la base de datos:\n" )
    print(" " * espaciado, str("Id").ljust(longidinterprete, ' ')," " * espaciado, str("Nombre").ljust(longnombre, ' ')," " * espaciado, str("Apellido").ljust(longapellido, ' ')," " * espaciado,str("Nacionalidad\033[0m").center(longnacionalidad, ' '))

    for artista in registros:
        print(" " * espaciado, str(artista[0]).ljust(longidinterprete, ' ')," " * espaciado, str(artista[1]).ljust(longnombre, ' ')," " * espaciado, str(artista[2]).ljust(longapellido, ' ')," " * espaciado,str(artista[3]).center(longnacionalidad, ' '))


def MostrarGenerosCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaGenerosCompleta()

    if registros == []:
        print("\n \033[1m No hay registros que coincidan con su búsqueda..\033[0m")
        return

    espaciado = 1
    longidgenero = 0
    longnombre = 0

    for genero in registros:
        if len(str(genero[0])) > longidgenero:
            longidgenero = len(str(genero[0]))

        if len(str(genero[1])) > longnombre:
            longnombre = len(str(genero[1]))


    print("\n\033[1m")
    print("Usted solicitó listar los Géneros Musicales cargados en la Base de Datos:\n" )
    print(" " * espaciado, str("Id").ljust(longidgenero, ' ')," " * espaciado, str("Nombre\033[0m").ljust(longnombre, ' '))

    for genero in registros:
        print(" " * espaciado, str(genero[0]).ljust(longidgenero, ' ')," " * espaciado, str(genero[1]).ljust(longnombre, ' '))



def insertarGeneroCLI():
    while True:
        print("\n")
        print("Usted está por cargar nuevo Género Musical, si ya existe en la Base de Datos se omitirá la carga: \n")

        nombre =        str(input("Escriba nombre del Género:  "))
        opcion = input("\n Que desea hacer? | 1 (Cargar) | 2 (Reingresar los Datos) | 3 (Cancelar)\nIngrese un número de opción: ")
        
        nombre = nombre.strip('\n')  #String, limpieza de espacios ant post, y Capitalizacion.
        nombre = nombre.strip()
        nombre = nombre.capitalize()

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = cargadatos.Cargar()
            carga.CargarGenero(nombre)
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            nombre = ""
        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")
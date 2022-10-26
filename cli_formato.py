#Funciones de formato y salida de texto para estética del CLI consola y algunas filtros para la salida de datos en la interfaz.

import consulta
import cargadatos
from cli_colores import ColoresCLI as color

msg_nohayregistros = color.BOLD + "\nNo hay registros que coincidan con su búsqueda.." + color.END


def MostrarAlbumsPorInterpreteCLI():
  
    Listar = consulta.Listar()
    registros = Listar.ListaAlbumesCompleta()

    if registros == []:
        print(msg_nohayregistros)
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

    print(color.BOLD)
    print(" " * espaciado, str("Album").ljust(longalbum, ' ')," " * espaciado, str("Nombre").ljust(longnombre, ' ')," " * espaciado, str("Apellido").ljust(longapellido, ' ')," " * espaciado,str("Genero").center(longgenero, ' ')," " * espaciado," " * espaciado,str("Codigo").center(longalbumcod, ' ')," " * espaciado," " * espaciado,str("Formato").ljust(longformato, ' ')," " * espaciado," " * espaciado,str("Año").center(longfecha, ' ')," " * espaciado," " * espaciado,str("Precio").ljust(longprecio, ' ')," " * espaciado," " * espaciado,str("Stock").center(longcant, ' ')," " * espaciado," " * espaciado,str("Sello").ljust(longdiscograf, ' ')," " * espaciado)
    print(color.END)
    for album in registros:
        #Imprimo resultados se calibran automáticamente de acuerdo a la cadena de long maxima ya que es variable en su longitud en cada columna.
        print(" " * espaciado, str(album[0]).ljust(longalbum, ' ')," " * espaciado, str(album[1]).ljust(longnombre, ' ')," " * espaciado, str(album[2]).ljust(longapellido, ' ')," " * espaciado,str(album[4]).center(longgenero, ' ')," " * espaciado," " * espaciado,str(album[5]).center(longalbumcod, ' ')," " * espaciado," " * espaciado,str(album[6]).ljust(longformato, ' ')," " * espaciado," " * espaciado,str(album[7]).ljust(longfecha, ' ')," " * espaciado," " * espaciado,str(album[8]).ljust(longprecio, ' ')," " * espaciado," " * espaciado,str(album[9]).ljust(longcant, ' ')," " * espaciado," " * espaciado,str(album[10]).center(longdiscograf, ' ')," " * espaciado)



   
def MostrarAlbumPorNombreCLI(): #Edgar G.
    nombre = str(input("Ingrese nombre del Album: "))
    nombre = nombre.strip('\n')  #String, limpieza de espacios ant post.
    nombre = nombre.strip()

    pistaChrLen = 0
    tituloChrLen = 0
    duracionChrLen = 0

    Listar = consulta.Listar()
    registros = Listar.NombreAlbumEspecifico(nombre)
            
    if registros == []:
        print(msg_nohayregistros)
        return                          
    else:
        espaciado = 5
        for album in registros:
            
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")

            print("  Album: ", color.VERDE_CLARO,str(album[2]),color.END)
            print("  Cod:    ",  str(album[1]))
            print("  Artista:", str(album[9]),str(album[10]))
            print("  Año:    ", str(album[4]))
            print("  Tipo:   ", str(album[12]))
            print("  Genero: ", str(album[11]))
            print("  Precio:  $", str(album[5]), sep='')
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

            print("Id en BD:", str(album[0]))

            if album[6] > 0:
                print("En Stock?:",color.VERDE,"SI, hay disponibles", str(album[6]), "unidades.", color.END)
            else:
                print("En Stock?:",color.ROJO, "NO quedan unidades.",color.END)             
            print("Canciones del Album: ", str(album[3]))
            
            print("\n")

        #Se puede dar que existan albumes sin canciones cargadas. 
        if ((album[13] == None) and (album[14] == None) and (album[15] == None)):
            print(color.AMARILLO + "Album sin información de canciones cargadas." + color.END)
        else:
            for cancion in registros:
                if len(str(cancion[13])) > pistaChrLen:
                    pistaChrLen = len(str(cancion[13]))

                if len(str(cancion[14])) > tituloChrLen:
                    tituloChrLen = len(str(cancion[14]))

                if len(str(cancion[15])) > duracionChrLen:
                    duracionChrLen = len(str(cancion[15]))


                print(" " * espaciado, str("Pista").ljust(pistaChrLen, ' ')," " * 1,str("Nombre").ljust(tituloChrLen, ' '), " " * espaciado, str("Duracion").ljust(duracionChrLen, ' '))

                print("\n")
                
                for album in registros:               
                    print(" " * espaciado, album[13]," " * espaciado, str(album[14]).ljust(tituloChrLen, ' '), " " * espaciado  ,album[15])


                print("\n")
                print("\nTapa del Disco: ",album[7])
                print("Foto Interprete:",album[8])
                print("Spotify Artista:","\033[94m https://open.spotify.com/search/" + str(album[9]) + "%20" + str(album[10]) + "\033[0m")
                print("Spotify Album:  ","\033[94m https://open.spotify.com/search/album" + "%3A" + str(album[2]) + "\033[0m")
        
    return



def MostrarAlbumsPorGeneroCLI():
    genero = str(input("Ingrese el género que quiere listar: "))
    genero = genero.strip('\n')  #String, limpieza de espacios ant post
    genero = genero.strip()


    Listar = consulta.Listar()
    registros = Listar.GeneroEspecifico(genero)

    if registros == []:
        print(msg_nohayregistros)
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
        print(msg_nohayregistros)
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
        print(msg_nohayregistros)
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



#--------------------------------------------------------------------------------------------------------------------

def MostrarFormatosCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaFormatosCompleta()

    if registros == []:
        print(msg_nohayregistros)
        return

    espaciado = 1
    longidformato = 0
    longnombre = 0

    for formato in registros:
        if len(str(formato[0])) > longidformato:
            longidformato = len(str(formato[0]))

        if len(str(formato[1])) > longnombre:
            longnombre = len(str(formato[1]))


    print("\n\033[1m")
    print("Usted solicitó listar los formatos de música cargados en la Base de Datos:\n" )
    print(" " * espaciado, str("Id").ljust(longidformato, ' ')," " * espaciado, str("Nombre\033[0m").ljust(longnombre, ' '))

    for formato in registros:
        print(" " * espaciado, str(formato[0]).ljust(longidformato, ' ')," " * espaciado, str(formato[1]).ljust(longnombre, ' '))



def MostrarDiscograficasCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaDiscograficasCompleta()

    if registros == []:
        print(msg_nohayregistros)
        return

    espaciado = 1
    longidnombre = 0
    longnombre = 0

    for discografica in registros:
        if len(str(discografica[0])) > longidnombre:
            longidnombre = len(str(discografica[0]))

        if len(str(discografica[1])) > longnombre:
            longnombre = len(str(discografica[1]))


    print("\n\033[1m")
    print("Usted solicitó listar Discograficas cargadas en la Base de Datos:\n" )
    print(" " * espaciado, str("Id").ljust(longidnombre, ' ')," " * espaciado, str("Nombre\033[0m").ljust(longnombre, ' '))

    for discografica in registros:
        print(" " * espaciado, str(discografica[0]).ljust(longidnombre, ' ')," " * espaciado, str(discografica[1]).ljust(longnombre, ' '))

#--------------------------------------------------------------------------------------------------------------------


def insertarGeneroCLI():
    while True:
        print("\n")
        print("Usted está por cargar nuevo Género Musical, si ya existe en la Base de Datos se omitirá la carga: \n")

        nombre =        str(input("Escriba nombre del Género:  "))
        opcion = input("\n Que desea hacer? | 1 (Cargar) | 2 (Reingresar los Datos) | 3 (Cancelar)\nIngrese un número de opción: ")
        
        nombre = nombre.strip('\n')  #String, limpieza de espacios anteriores y posteriores y Capitalizacion.
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

def insertarFormatoCLI():
    while True:
        print("\n")
        print("Usted está por cargar nuevo Formato de audio, si ya existe en la Base de Datos se omitirá la carga: \n")

        tipo =        str(input("Escriba el tipo de formato:  "))
        opcion = input("\n Que desea hacer? | 1 (Cargar) | 2 (Reingresar los Datos) | 3 (Cancelar)\nIngrese un número de opción: ")
        
        tipo = tipo.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        tipo = tipo.strip()

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = cargadatos.Cargar()
            carga.CargarFormato(tipo)
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            tipo = ""
        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")


def InsertarDiscograficaCLI():
    while True:
        print("\n")
        print("Usted está por cargar una Discográfica, si ya existe en la Base de Datos se omitirá la carga: \n")

        nombre = str(input("Escriba el nombre de la Discográfica:  "))
        opcion = input("\n Que desea hacer? | 1 (Cargar) | 2 (Reingresar los Datos) | 3 (Cancelar)\nIngrese un número de opción: ")
        
        nombre = nombre.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        nombre = nombre.strip()

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = cargadatos.Cargar()
            carga.CargarDiscografica(nombre)
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            nombre = ""
        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")



def InsertarAlbumCLI():

    while True:
        print("\n")
        print("Usted está por cargar un álbum: \n")
        

        cod_album = str(input("\nEscriba el código discográfico del álbum:  "))
        cod_album = cod_album.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        cod_album = cod_album.strip()

        nombre = input("\nIngrese el nombre del álbum: ")
        nombre = nombre.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        nombre = nombre.strip()

       #-------------------------------------------------------------------------------------------------------   

        MostrarInterpreteCLI()
        id_interprete = int(input("\nIngrese el ID del Intérprete: "))

        #------------------------------------------------------------------------------------------------------ 
                 
        MostrarGenerosCLI()
        id_genero = int(input("\nIngrese el ID del Género: "))

        #------------------------------------------------------------------------------------------------------  

        cant_temas = int(input("\nIngrese la cantidad de temas: "))

        #------------------------------------------------------------------------------------------------------   
      
        MostrarDiscograficasCLI()
        id_discografica = int(input("\nIngrese el ID de la discografica: "))

        #------------------------------------------------------------------------------------------------------  
        MostrarFormatosCLI()               
        id_formato = int(input("\nIngrese el ID del formato: "))
        #------------------------------------------------------------------------------------------------------  

        fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (ej: 2018): ")
        precio = float(input("\nIngrese el precio (ej: 1200): "))
        cantidad = int(input("\nIngrese cantidad disponible de este álbum (ej: 4): "))
        caratula = input("\nIngrese la dirección web de la Carátula (link directo al .jpg etc): ")

        nuevoAlbum = cargadatos.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)

        opcion = input("\n Que desea hacer? | 1 (Cargar) | 2 (Reingresar los Datos) | 3 (Cancelar)\nIngrese un número de opción: ")

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = cargadatos.Cargar()
            carga.CargarAlbum(nuevoAlbum)
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            cod_album = ""
            nombre = ""
            id_interprete = ""
            id_genero,cant_temas = ""
            id_discografica = ""
            id_formato = ""
            fec_lanzamiento = ""
            precio = ""
            cantidad = ""
            caratula = ""

        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")


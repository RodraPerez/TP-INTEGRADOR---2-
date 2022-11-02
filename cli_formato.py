#Funciones de formato y salida de texto para estética del CLI consola y algunas filtros para la salida de datos en la interfaz.

import consulta
import abm
import qrcode_terminal
from cli_colores import ColoresCLI as color

#Mensaje por defecto para ausencia de registros:
msg_nohayregistros = color.BOLD + "\nNo hay registros que coincidan con su búsqueda.." + color.END


#Tema de Color Custom para las tablas, puede cambiarse para todas desde aqui::
ColorTemaA = color.CYAN_CLARO
ColorTemaB = color.END
ColorTemaC = color.CYAN
ColorTemaD = color.NARANJA
ColorTemaE = color.GRIS_CLARO

def MostrarAlbumsPorInterpreteCLI():
  
    Listar = consulta.Listar()
    registros = Listar.ListaAlbumesCompleta()

    if registros == []:
        print(msg_nohayregistros)
        return

    gap = 1
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
    longdidalbum = 0

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
        if len(str(album[12])) > longdidalbum:
            longdidalbum = len(str(album[12]))

    print(color.BOLD)
    print(" " * gap, str("Id").ljust(longdidalbum,' '),
    " " * gap,str("Album").ljust(longalbum, ' '),
    " " * gap, str("Nombre").ljust(longnombre, ' '),
    " " * gap, str("Apellido").ljust(longapellido, ' '),
    " " * gap,str("Genero").center(longgenero, ' '),
    " " * gap," " * gap,str("Codigo").center(longalbumcod, ' '),
    " " * gap," " * gap,str("Formato").ljust(longformato, ' '),
    " " * gap," " * gap,str("Año").center(longfecha, ' '),
    " " * gap," " * gap,str("Precio").ljust(longprecio, ' '),
    " " * gap," " * gap,str("Stock").center(longcant, ' '),
    " " * gap,str("Sello").ljust(longdiscograf, ' '),
    " " * gap)
    print(color.END)
    
    i = 0

    for album in registros:
        
        if i % 2 == 0:
            print(ColorTemaA, end='')
        else:
            print(ColorTemaB, end='')
              
        #Imprimo resultados se calibran automáticamente de acuerdo a la cadena de long maxima ya que es variable en su longitud en cada columna.

        print(" " * gap,str(album[12]).ljust(longdidalbum, ' '),
        " " * gap,str(album[0]).ljust(longalbum, ' '),
        " " * gap,str(album[1]).ljust(longnombre, ' '),
        " " * gap, str(album[2]).ljust(longapellido, ' '),
        " " * gap,str(album[4]).center(longgenero, ' '),
        " " * gap," " * gap,str(album[5]).center(longalbumcod, ' '),
        " " * gap," " * gap,str(album[6]).ljust(longformato, ' '),
        " " * gap," " * gap,str(album[7]).ljust(longfecha, ' '),
        " " * gap," " * gap,str(album[8]).ljust(longprecio, ' '),
        " " * gap," " * gap,str(album[9] if album[9] > 0 else color.ROJO + "NO" + color.END).ljust(longcant, ' '),
        " " * gap," " * gap,str(album[10]).ljust(longdiscograf, ' '),
        " " * gap)
        i += 1
    i = 0


   
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
        gap = 5
        for album in registros:
            pass

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

        print(color.BOLD,end='')
        print(" " * gap, str("Pista").ljust(pistaChrLen, ' ')," " * 3,str("Nombre").ljust(tituloChrLen, ' '), " " * 5, str("Duracion").ljust(duracionChrLen, ' '))
        print(color.END)

        
        for album in registros:               
            print(" " * gap, color.CYAN, album[13],color.END," " * gap, str(album[14]).ljust(tituloChrLen, ' '), " " * gap  ,album[15])


    print("\n")
    print("\nTapa del Disco: ",album[7] if album[7] != "" else color.ROJO + "No hay imagen de la caratula en la Base de Datos." + color.END)
    print("Foto Interprete:",album[8] if album[8] != "" else color.ROJO + "No hay imagen del Interprete en la Base de Datos." + color.END)
    print("Spotify Artista:",color.AZUL + "https://open.spotify.com/search/" + str(album[9]).replace(" ", "+") + "%20" + str(album[10]).replace(" ", "+") + color.END)
        
    albumstr = "https://www.last.fm/es/music/" + str(album[9] + ' ' + album[10]).replace(" ", "+") + "/" + str(album[2]).replace(" ", "+")
    #print(albumstr) debug

    while True:
        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Opciones de Album █ 1 (QR Info LastFM) █ 2 (Modificar Album) █ 3 (Salir) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("Generando su QR..\n")
            qrcode_terminal.draw(albumstr)
            print("")
            continue
        elif opcion == "2":
            ModificarAlbumCLI()
            break
        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break
        else:
            print("¡Opción incorrecta!")
    return


def MostrarAlbumsPorGeneroCLI():
    genero = str(input("Ingrese el género que quiere listar: "))
    genero = genero.strip('\n')  #String, limpieza de espacios ant post
    genero = genero.strip()
#album.id_album,album.nombre, interprete.nombre, interprete.apellido, genero.nombre, album.cod_album, formato.tipo, album.fec_lanzamiento,album.precio,album.cantidad

    Listar = consulta.Listar()
    registros = Listar.GeneroEspecifico(genero)

    if registros == []:
        print(msg_nohayregistros)
        return

    gap = 1
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
    longdidalbum = 0

    for album in registros:  #Procedimiento para extraer maximos strlen de cada registro
        if len(str(album[0])) > longdidalbum:
            longdidalbum = len(str(album[0]))
        if len(str(album[1])) > longalbum:
            longalbum = len(str(album[1]))
        if len(str(album[2])) > longnombre:
            longnombre = len(str(album[2]))
        if len(str(album[3])) > longapellido:
            longapellido = len(str(album[3]))
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


    print(color.BOLD)
    print(" " * gap, str("Id").ljust(longdidalbum,' '),
    " " * gap,str("Album").ljust(longalbum, ' '),
    " " * gap, str("Nombre").ljust(longnombre, ' '),
    " " * gap, str("Apellido").ljust(longapellido, ' '),
    "  " * gap,str("Genero").center(longgenero, ' '),
    " " * gap,str("Codigo").center(longalbumcod, ' '),
    " " * gap," " * gap,str("Formato").ljust(longformato, ' '),
    " " * gap," " * gap,str("Año").center(longfecha, ' '),
    " " * gap," " * gap,str("Precio").ljust(longprecio, ' '),
    " " * gap," " * gap,str("Stock").center(longcant, ' '),
    " " * gap)
    print(color.END)
    
    i = 0

    for album in registros:
        
        if i % 2 == 0:
            print(ColorTemaA, end='')
        else:
            print(ColorTemaB, end='')
              
        #Imprimo resultados se calibran automáticamente de acuerdo a la cadena de long maxima ya que es variable en su longitud en cada columna.

        print(" " * gap,str(album[0]).ljust(longdidalbum, ' '),
        " " * gap,str(album[1]).ljust(longalbum, ' '),
        " " * gap,str(album[2]).ljust(longnombre, ' '),
        " " * gap, str(album[3]).ljust(longapellido, ' '),
        "    " * gap,str(album[4]).center(longgenero, ' '),
        " " * gap," " * gap,str(album[5]).center(longalbumcod, ' '),
        " " * gap," " * gap,str(album[6]).ljust(longformato, ' '),
        " " * gap," " * gap,str(album[7]).ljust(longfecha, ' '),
        " " * gap," " * gap,str(album[8]).ljust(longprecio, ' '),
        " " * gap," " * gap,str(album[9] if album[9] > 0 else color.ROJO + "NO" + color.END).ljust(longcant, ' '),
        " " * gap)
        i += 1
    i = 0

def InsertarInterpreteCLI():

    while True:
        print("\n")
        print("Usted está por cargar nuevo Artista o Interprete:"+ color.END)
        nombre =        str(input(color.BOLD +"Escriba Nombre del interprete:                      " + color.END))
        apellido =      str(input(color.BOLD +"Apellido (si no tiene dejar en blanco ej. ABBA):    " + color.END))
        nacionalidad =  str(input(color.BOLD +"Nacionalidad del interprete:                        " + color.END))
        foto =          str(input(color.BOLD +"Foto del interprete (link directo al .jpg .jpeg o .png o puede dejarlo vacio \n Link:  " + color.END))
        print(color.END)

        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Cargar) █ 2 (Reingresar los Datos) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = abm.Cargar()
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

    gap = 1
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

    print(color.BOLD)
    print("Usted solicitó listar los Artistas disponibles en la base de datos:\n" )
    print(" " * gap, str("Id").ljust(longidinterprete, ' ')," " * gap, str("Nombre").ljust(longnombre, ' ')," " * gap, str("Apellido").ljust(longapellido, ' ')," " * gap,str("Nacionalidad" + color.END).center(longnacionalidad, ' '))

    i = 0
    for artista in registros:
        
        if i % 2 == 0:
            print(ColorTemaA, end='')
        else:
            print(ColorTemaC, end='')
        i += 1

        print(" " * gap, str(artista[0]).ljust(longidinterprete, ' ')," " * gap, str(artista[1]).ljust(longnombre, ' ')," " * gap, str(artista[2]).ljust(longapellido, ' ')," " * gap,str(artista[3]).center(longnacionalidad, ' '),(artista[4] if artista[4] != "" else color.ROJO + "No hay imagen de este artista en la Base de Datos." + color.END))
    i = 0

def MostrarGenerosCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaGenerosCompleta()

    if registros == []:
        print(msg_nohayregistros)
        return

    gap = 1
    longidgenero = 0
    longnombre = 0

    for genero in registros:
        if len(str(genero[0])) > longidgenero:
            longidgenero = len(str(genero[0]))

        if len(str(genero[1])) > longnombre:
            longnombre = len(str(genero[1]))


    print(color.BOLD)
    print("Usted solicitó listar los Géneros Musicales cargados en la Base de Datos:\n" )
    print(" " * gap, str("Id").ljust(longidgenero, ' ')," " * gap, str("Nombre" + color.END).ljust(longnombre, ' '))

    i = 0
    for genero in registros:
        
        if i % 2 == 0:
            print(ColorTemaE, end='')
        else:
            print(ColorTemaD, end='')
        i += 1
        print(" " * gap, str(genero[0]).ljust(longidgenero, ' ')," " * gap, str(genero[1]).ljust(longnombre, ' '))
    i = 0


#--------------------------------------------------------------------------------------------------------------------

def MostrarFormatosCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaFormatosCompleta()

    if registros == []:
        print(msg_nohayregistros)
        return

    gap = 1
    longidformato = 0
    longnombre = 0

    for formato in registros:
        if len(str(formato[0])) > longidformato:
            longidformato = len(str(formato[0]))

        if len(str(formato[1])) > longnombre:
            longnombre = len(str(formato[1]))


    print(color.BOLD)
    print("Usted solicitó listar los formatos de música cargados en la Base de Datos:\n" )
    print(" " * gap, str("Id").ljust(longidformato, ' ')," " * gap, str("Nombre" + color.END).ljust(longnombre, ' '))

    i = 0
    for formato in registros:
        
        if i % 2 == 0:
            print(ColorTemaA, end='')
        else:
            print(ColorTemaD, end='')
        i += 1

        print(" " * gap, str(formato[0]).ljust(longidformato, ' ')," " * gap, str(formato[1]).ljust(longnombre, ' '))
    i = 0


def MostrarDiscograficasCLI():

    Listar = consulta.Listar()
    registros = Listar.ListaDiscograficasCompleta()

    if registros == []:
        print(msg_nohayregistros)
        return

    gap = 1
    longidnombre = 0
    longnombre = 0

    for discografica in registros:
        if len(str(discografica[0])) > longidnombre:
            longidnombre = len(str(discografica[0]))

        if len(str(discografica[1])) > longnombre:
            longnombre = len(str(discografica[1]))


    print(color.BOLD)
    print("Usted solicitó listar Discograficas cargadas en la Base de Datos:\n" )
    print(" " * gap, str("Id").ljust(longidnombre, ' ')," " * gap, str("Nombre" + color.END).ljust(longnombre, ' '))

    i = 0
    for discografica in registros:
        
        if i % 2 == 0:
            print(ColorTemaA, end='')
        else:
            print(ColorTemaD, end='')
        i += 1
        print(" " * gap, str(discografica[0]).ljust(longidnombre, ' ')," " * gap, str(discografica[1]).ljust(longnombre, ' '))
    i = 0
#--------------------------------------------------------------------------------------------------------------------


def insertarGeneroCLI():
    while True:
        print("\n" + color.BOLD)
        print("Usted está por cargar nuevo Género Musical, si ya existe en la Base de Datos se omitirá la carga: \n" + color.END)

        nombre = str(input(color.BOLD + "Escriba nombre del Género:  " + color.END))

        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Cargar) █ 2 (Reingresar los Datos) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        nombre = nombre.strip('\n')  #String, limpieza de espacios anteriores y posteriores y Capitalizacion.
        nombre = nombre.strip()
        nombre = nombre.capitalize()

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = abm.Cargar()
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
        print("\n" + color.BOLD)
        print("Usted está por cargar nuevo Tipo de Formato, si ya existe en la Base de Datos se omitirá la carga: \n" + color.END)

        tipo = str(input(color.BOLD + "Escriba el Tipo de Formato:  " + color.END))

        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Cargar) █ 2 (Reingresar los Datos) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)
        
        tipo = tipo.strip()

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = abm.Cargar()
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
        print("\n" + color.BOLD)
        print("Usted está por cargar una nueva Discografica, si ya existe en la Base de Datos se omitirá la carga: \n" + color.END)

        nombre = str(input(color.BOLD + "Escriba el nombre de la Discográfica:  " + color.END))

        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Cargar) █ 2 (Reingresar los Datos) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        nombre = nombre.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        nombre = nombre.strip()

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = abm.Cargar()
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
        

        cod_album = str(input("\nEscriba el " + color.BOLD + "código" + color.END + " discográfico del álbum: "))
        cod_album = cod_album.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        cod_album = cod_album.strip()

        nombre = input("\nIngrese el " + color.BOLD + "nombre" + color.END + " del álbum: ")
        nombre = nombre.strip('\n')  #String, limpieza de espacios anteriores y posteriores.
        nombre = nombre.strip()

       #-------------------------------------------------------------------------------------------------------   

        MostrarInterpreteCLI()

        id_interprete = int(input("\nIngrese el " + color.BOLD + "Id del Interprete" + color.END + " (si no existe, escriba '0' para agregar uno): "))
        if id_interprete == 0:
            InsertarInterpreteCLI()
            MostrarInterpreteCLI()
            id_interprete = int(input("\nIngrese el " + color.BOLD + "Id del Interprete" + color.END + ": "))

        #------------------------------------------------------------------------------------------------------ 
                 
        MostrarGenerosCLI()
        id_genero = int(input("\nIngrese el " + color.BOLD + "Id del género" + color.END + " (si no existe, escriba '0' para agregar uno): "))
        if id_genero == 0:
            insertarGeneroCLI()
            MostrarGenerosCLI()
            id_genero = int(input("\nIngrese el " + color.BOLD + "Id del género " + color.END + ": "))
        #------------------------------------------------------------------------------------------------------  

        cant_temas = int(input("\nIngrese la " + color.BOLD + "cantidad de temas: " + color.END))

        #------------------------------------------------------------------------------------------------------   
      
        MostrarDiscograficasCLI()
        id_discografica = int(input("\nIngrese el " + color.BOLD + "id de la discográfica" + color.END  + " (si no existe, escriba '0' para agregar una): "))
        if id_discografica == 0:
            InsertarDiscograficaCLI()
            MostrarDiscograficasCLI()
            id_discografica = int(input("\nIngrese el " + color.BOLD + "id de la discográfica" + color.END  + ": "))

        #------------------------------------------------------------------------------------------------------  
        MostrarFormatosCLI()               
        id_formato = int(input("\nIngrese el " + color.BOLD + "id del formato" + color.END  + ": "))
        #------------------------------------------------------------------------------------------------------  

        fec_lanzamiento = input("\nIngrese el " + color.BOLD + "año de lanzamiento" + color.END  + " (ej: 2018): ")
        precio = float(input("\nIngrese el " + color.BOLD + "precio" + color.END  + " (ej: 1200): "))
        cantidad = int(input("\nIngrese " + color.BOLD + "cantidad en stock" + color.END  + " de este álbum (ej: 4): "))
        caratula = input("\nIngrese la " + color.BOLD + "direccion web de la imagen" + color.END  + " de la Carátula (link directo al .jpg etc): ")

        nuevoAlbum = abm.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)

        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Cargar) █ 2 (Reingresar los Datos) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("Intentando carga de los datos..")
            carga = abm.Cargar()
            carga.CargarAlbum(nuevoAlbum)
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            cod_album = ""
            nombre = ""
            id_interprete = ""
            id_genero = ""
            cant_temas = ""
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

#-------------------------------------------------------------------------------------------------------------------------------------------

# CLI Modificacion Album (descripción):
# 1 - Pedir id de album. Será el parámetro a pasar junto con la nueva tupla de la clase Album que obtengamos.
# 2 - Durante el cuestionario usamos variables con nombre de todos los campos a modificar con lo que se mantiene o se va segun respuestas. 
# 3 - Luego establecemos todas las propiedades de la clase album con los datos de las columnas, por medio de la consulta por ID que tenemos en "consultas.py" 
# 4 - Usando un filtro con IF's almacenando lo que se modificará. Y manteniendo lo que se queda. Getter y Setters. Se modela la tupla.
# 5 - Al ultimo enviamos a conexion el objeto modelado en sus propiedades. Tenemos Añadido de decidir reintentar la Modificación en un menú adicional.
# 6 - Hacemos el UPDATE Se envia el objeto con la info modificada al modulo ABM. Finalmente éste hace la conexión con la query y la tupla objeto.
# CLI (interfaz) ---> CLI_FORMATO (estetica y formato de los datos) ---> CONSULTA (SOLO CONSULTAS select) ----> ABM(altas bajas modificacion, y clases)-----> conexion.


def ModificarAlbumCLI():

    id_album = None
    cod_album = None
    nombre = None
    id_interprete = None
    id_genero = None
    cant_temas = None
    id_discografica = None
    id_formato = None
    fec_lanzamiento = None
    precio = None
    cantidad = None
    caratula = None


    while True:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
        #Se elige el id del album:

        print("\n")
        print("Usted está por " + color.AMARILLO+ "MODIFICAR" + color.END + " un " + color.BOLD + "álbum." + color.END)

        id_album = int(input("\nEscriba el " + color.BOLD + "id" + color.END + " del album a modificar (ingrese 0 para ver la lista antes, si no lo sabe.):  "))

        if (id_album == 0) or (id_album == None):
            MostrarAlbumsPorInterpreteCLI()
            id_album = int(input("\n Escriba el " + color.BOLD + "id" + color.END + " del album a modificar: "))
              
#-----------------------------------------------------------------------------------------------------------------------------------------------------

        print(color.BOLD + "\nPerfecto, ahora siga las instrucciones: \n" + color.END)

        #Cuestionario donde cambiaremos los datos en las propiedades de la clase Album luego por medio de los setters y los getters las propiedades de el objeto:

        pregunta1 = str(input(color.VERDE_CLARO + "Desea modificar el codigo discográfico del album? " + color.BOLD + "s/n: " + color.END))
        pregunta1.lower()
        if pregunta1 == "s":
            cod_album = str(input("\nEscriba el " + color.BOLD + "nuevo código" + color.END + " discográfico del álbum: "))
            cod_album = cod_album.strip()

        pregunta2 = str(input(color.VERDE_CLARO + "Desea modificar el nombre del album? " + color.BOLD + "s/n: " + color.END))
        pregunta2.lower()       
        if pregunta2 == "s":
            nombre = str(input("\nEscriba el " + color.BOLD + "nuevo nombre" + color.END + " del álbum: "))
            nombre = nombre.strip()
            

        pregunta3 = str(input(color.VERDE_CLARO + "Desea modificar el interprete del album? " + color.BOLD + "s/n: " + color.END))
        pregunta3.lower()       
        if pregunta3 == "s":
            MostrarInterpreteCLI()
            id_interprete = int(input("\nEscriba el " + color.BOLD + "id del nuevo interprete" + color.END + " del álbum: "))
            

        pregunta4 = str(input(color.VERDE_CLARO + "Desea modificar el género del album? " + color.BOLD + "s/n: " + color.END))
        pregunta4.lower()       
        if pregunta4 == "s":
            MostrarGenerosCLI()
            id_genero = int(input("\nEscriba el " + color.BOLD + "id del nuevo género" + color.END + " del álbum: "))


        pregunta5 = str(input(color.VERDE_CLARO + "Desea modificar cantidad de temas del album? " + color.BOLD + "s/n: " + color.END))
        pregunta5.lower()       
        if pregunta5 == "s":
            cant_temas = input("\nEscriba la " + color.BOLD + "nueva cantidad de temas" + color.END + " del álbum: ")
            

        pregunta6 = str(input(color.VERDE_CLARO + "Desea modificar el sello discográfico del album? " + color.BOLD + "s/n: " + color.END))
        pregunta6.lower()       
        if pregunta6 == "s":
            MostrarDiscograficasCLI()
            id_discografica = int(input("\nEscriba la " + color.BOLD + "nueva id discográfica" + color.END + " del álbum: "))
            

        pregunta7 = str(input(color.VERDE_CLARO + "Desea modificar el formato del album? " + color.BOLD + "s/n: " + color.END))
        pregunta7.lower()       
        if pregunta7 == "s":
            MostrarFormatosCLI()
            id_formato = int(input("\nEscriba el " + color.BOLD + "nuevo formato" + color.END + " del álbum: "))
            

        pregunta8 = str(input(color.VERDE_CLARO + "Desea modificar año de lanzamiento del album?" + color.BOLD + "s/n: " + color.END))
        pregunta8.lower()       
        if pregunta8 == "s":
            fec_lanzamiento = input("\nEscriba el " + color.BOLD + "nuevo año" + color.END + " del álbum (ej: 2018): ")
            

        pregunta9 = str(input(color.VERDE_CLARO + "Desea modificar el precio del album?" + color.BOLD + "s/n: " + color.END))
        pregunta9.lower()
        if pregunta9 == "s":
            precio = float(input("\nEscriba el " + color.BOLD + "nuevo precio" + color.END + " del álbum (ej: 1200): "))
            

        pregunta10 = str(input(color.VERDE_CLARO + "Desea modificar el stock de unidades del album?" + color.BOLD + "s/n: " + color.END))
        pregunta10.lower()
        if pregunta10 == "s":
            cantidad = int(input("\nEscriba la " + color.BOLD + "nueva cantidad de unidades" + color.END + " del álbum: "))
            

        pregunta11 = str(input(color.VERDE_CLARO + "Desea modificar la caratula del album?" + color.BOLD + "s/n: " + color.END))
        pregunta11.lower()
        if pregunta11 == "s":
            caratula = (input("\nEscriba el " + color.BOLD + "link directo a la imagen" + color.END + " del álbum: "))
            
#---------------------------------------------------------------------------------------------------------------------------------------

        #Hacemos el Query select para traer los datos del id_album en el orden correcto, solicitado en el cuestionario.
        getdatos = consulta.Listar()
        resultados = getdatos.idAlbumEspecifico(id_album)

        #Llenamos el objeto Album con los datos actualizados de la base de datos del id de album elegido.
        for dato in resultados:
            Album = abm.Album(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9],dato[10],dato[11])
            #print(dato) #print debug

        #Alteramos el objeto Album solamente lo elegido en el cuestionario, si es distino a None es porque lo cambiamos en el cuestionario, si es None obtenemos el dato que sigue sin cambio desde el getter de la clase. 

        if cod_album != None:
            Album.setCod_album(cod_album)
        else:
            cod_album = Album.getCod_album()

        if nombre != None:
            Album.setNombre(nombre)
        else:
            nombre = Album.getNombre()

        if id_interprete != None:
            Album.setId_interprete(id_interprete)
        else:
            id_interprete = Album.getId_interprete()

        if id_genero != None:
            Album.setId_genero(id_genero)
        else:
            id_genero = Album.getId_genero()

        if cant_temas != None:
            Album.setCant_temas(cant_temas)
        else:
            cant_temas = Album.getCant_temas()

        if id_discografica != None:
            Album.setId_discografica(id_discografica)
        else:
            id_discografica = Album.getId_discografica()

        if id_formato != None:
            Album.setId_formato(id_formato)
        else:
            id_formato = Album.getId_formato()

        if fec_lanzamiento != None:
            Album.setFec_lanzamiento(fec_lanzamiento)
        else:
            fec_lanzamiento = Album.getFec_lanzamiento()

        if precio != None:
            Album.setPrecio(precio)
        else:
            precio = Album.getPrecio()

        if cantidad != None:
            Album.setCantidad(cantidad)
        else:
            cantidad = Album.getCantidad()

        if caratula != None:
            Album.setCaratula(caratula)
        else:
            caratula = Album.getCaratula()

        #Antes de confirmar mostramos un resumen de los cambios:

        print(color.BOLD + "\nINFO Precarga de datos: " + color.END)   #Print Debug

        print(  "\nId seleccionado:",id_album, 
                "\nCodigo album:",cod_album,
                "\nNombre Album:",nombre,
                "\nId Interprete:",id_interprete,
                "\nId género:",id_genero,
                "\ncant temas:",cant_temas,
                "\nId Discografica:",id_discografica,
                "\nId Formato:",id_formato,
                "\nAño:",fec_lanzamiento,
                "\nprecio:",precio,
                "\ncantidad",cantidad,
                "\ncaratula",caratula,
                )



        #Generamos la nueva tupla de datos modificados para el envio a la base de datos:

        AlbumModificado = abm.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)


        #Preguntamos y decidimos:
        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Confirmar cambios) █ 2 (Reintentar la Carga) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("\nIntentando modificación de Album...")
            modificar = abm.Cargar()                                 #Instanciamos la carga (modelo) y sus metodos.
            modificar.ModificarAlbum(AlbumModificado,id_album)       #Se envia al metodo de la clase Cargar, el objeto portador de la tupla nueva, y de parametro el ID del album.  

            print(color.AMARILLO + "\nALBUM MODIFICADO" + color.END) 
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            cod_album = None
            nombre = None
            id_interprete = None
            id_genero = None
            cant_temas = None
            id_discografica = None
            id_formato = None
            fec_lanzamiento = None
            precio = None
            cantidad = None
            caratula = None

        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")

#-----------------------------------------------------------------------------------------------------------------------------------------------------


def EliminarAlbumCLI():
    id_album = None

    while True:
        print("\n")
        print("Usted está por " + color.ROJO_CLARO + "ELIMINAR" + color.END + " un " + color.BOLD + "álbum." + color.END)

        id_album = int(input("\nEscriba el " + color.BOLD + "id" + color.END + " del album a eliminar (ingrese 0 para ver la lista antes, si no lo sabe.):  "))

        if (id_album == 0) or (id_album == None):
            MostrarAlbumsPorInterpreteCLI()
            id_album = int(input("\n Escriba el " + color.BOLD + "id" + color.END + " del album a eliminar: "))

        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ " + color.ROJO_CLARO + "1 (ELIMINAR) " + color.END + color.CYAN_CLARO + "█ 2 (Reingresar Id del Album) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("\nIntentando eliminación de Album...")
            eliminar = abm.Cargar()
            eliminar.EliminarAlbum(id_album)                                #Enviamos solamente el id del album 
            print(color.ROJO_CLARO + "\nALBUM ELIMINADO" + color.END) 
            break

        elif opcion == "2":
            print("\nREINTENTANDO..")
            id_album = None
        elif opcion == "3":
            print("\nCANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")



#--------------------------------------------------------------------------------------------------------------------------------------
#Cargar canciones:

def ModificarInterpreteCLI():

    id_interprete = None
    nombre = None
    apellido = None
    nacionalidad = None
    foto = None

    while True:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
        #Se elige el id del album:

        print("\n")
        print("Usted está por " + color.AMARILLO+ "MODIFICAR" + color.END + " un " + color.BOLD + "intérprete." + color.END)

        id_interprete = int(input("\nEscriba el " + color.BOLD + "id" + color.END + " del intérprete a modificar (ingrese 0 para ver la lista antes, si no lo sabe.):  "))

        if (id_interprete == 0) or (id_interprete == None):
            MostrarInterpreteCLI()
            id_interprete = int(input("\n Escriba el " + color.BOLD + "id" + color.END + " del intérprete a modificar: "))
              
#-----------------------------------------------------------------------------------------------------------------------------------------------------

        print(color.BOLD + "\nPerfecto, ahora siga las instrucciones: \n" + color.END)

        #Cuestionario donde cambiaremos los datos en las propiedades de la clase Album luego por medio de los setters y los getters las propiedades de el objeto:

        pregunta1 = str(input(color.VERDE_CLARO + "Desea modificar el nombre del intérprete? " + color.BOLD + "s/n: " + color.END))
        pregunta1.lower()
        if pregunta1 == "s":
            nombre = str(input("\nEscriba el " + color.BOLD + "nuevo nombre" + color.END + " del intérprete: "))
            nombre = nombre.strip()

        pregunta2 = str(input(color.VERDE_CLARO + "Desea modificar el apellido del interprete? " + color.BOLD + "s/n: " + color.END))
        pregunta2.lower()       
        if pregunta2 == "s":
            apellido = str(input("\nEscriba el " + color.BOLD + "nuevo apellido" + color.END + " del intérprete: "))
            apellido = apellido.strip()
            

        pregunta3 = str(input(color.VERDE_CLARO + "Desea modificar la nacionalidad del intérprete? " + color.BOLD + "s/n: " + color.END))
        pregunta3.lower()       
        if pregunta3 == "s":
            nacionalidad = str(input("\nEscriba la " + color.BOLD + "nueva nacionalidad del interprete" + color.END + " del álbum: "))
            nacionalidad = nacionalidad.strip()
            

        pregunta4 = str(input(color.VERDE_CLARO + "Desea modificar la foto del intérprete?" + color.BOLD + "s/n: " + color.END))
        pregunta4.lower()
        if pregunta4 == "s":
            foto = str(input("\nEscriba el " + color.BOLD + "link directo a la imagen" + color.END + " del intérprete: "))
            foto = foto.strip()

            
#---------------------------------------------------------------------------------------------------------------------------------------

        #Hacemos el Query select para traer los datos del id_album en el orden correcto, solicitado en el cuestionario.
        getdatos = consulta.Listar()
        resultados = getdatos.idInterpreteEspecifico(id_interprete)

        #Llenamos el objeto Album con los datos actualizados de la base de datos del id de album elegido.
        for dato in resultados:
            Interprete = abm.Interprete (dato[0],dato[1],dato[2],dato[3],dato[4])
            #print(dato) #print debug 

        #Alteramos el objeto Album solamente lo elegido en el cuestionario, si es distino a None es porque lo cambiamos en el cuestionario, si es None obtenemos el dato que sigue sin cambio desde el getter de la clase. 

        if nombre != None:
            Interprete.setNombre(nombre)
        else:
            nombre = Interprete.getNombre()

        if apellido != None:
            Interprete.setApellido(apellido)
        else:
            nombre = Interprete.getApellido()

        if nacionalidad != None:
            Interprete.setNacionalidad(nacionalidad)
        else:
            nacionalidad = Interprete.getNacionalidad()

        if foto != None:
            Interprete.setFoto(foto)
        else:
            foto = Interprete.getFoto()


        #Antes de confirmar mostramos un resumen de los cambios:

        print(color.BOLD + "\nINFO Precarga de datos: " + color.END)   #Print Debug

        print(  "\nId Interprete:",id_interprete,
                "\nNombre Intérprete:",nombre,
                "\nApellido Intérprete:",apellido,
                "\nNacionalidad Intérprete:",nacionalidad,
                "\nFoto Intérprete:",foto,      
                )

        #Generamos la nueva tupla de datos modificados para el envio a la base de datos:

        InterpreteModificado = abm.Interprete(0,nombre,apellido,nacionalidad,foto)

        #Preguntamos y decidimos:
        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ 1 (Confirmar cambios) █ 2 (Reintentar la Carga) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("\nIntentando modificación de Album...")
            modificar = abm.Cargar()                                 #Instanciamos la carga (modelo) y sus metodos.
            modificar.ModificarInterprete(InterpreteModificado,id_interprete)       #Se envia al metodo de la clase Cargar, el objeto portador de la tupla nueva, y de parametro el ID del album.  

            print(color.AMARILLO + "\nINTERPRETE MODIFICADO" + color.END) 
            break

        elif opcion == "2":
            print("REINTENTANDO..")
            nombre = None
            apellido = None
            nacionalidad = None
            foto = None

        elif opcion == "3":
            print("CANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")

#-----------------------------------------------------------------------------------------------------------------------------------------------------



def InsertarCancionCLI():

    id_album = None

    while True:
        print("\n")
        print("Usted está por " + color.VERDE_CLARO+ "Agregar una cancion" + color.END + " a un " + color.BOLD + "álbum." + color.END)

        id_album = int(input("\nEscriba el " + color.BOLD + "id" + color.END + " del album al que pertenecen los temas (ingrese 0 para ver la lista antes, si no lo sabe.): "))

        if (id_album == 0) or (id_album == None):
            MostrarAlbumsPorInterpreteCLI()
            id_album = int(input("\n Escriba el " + color.BOLD + "id" + color.END + " del album para comenzar: "))

        #Obtenemos Interprete y nombre de album desde la id_album
        getdatos = consulta.Listar()
        resultados = getdatos.idAlbumEspecifico(id_album)

        for dato in resultados:
            albumnom = dato[2]
            interprete = dato[3]

        print (color.AMARILLO + "Usted agregará entonces una canción al album " + color.END + color.CYAN_CLARO + albumnom + ": \n" + color.END)

         #Tema.getTrack_num(),Tema.getTiulo(),Tema.getDuracion(),Tema.getAutor(),Tema.getCompositor(),Tema.getId_album(),Tema.getId_interprete())

        track_num =  int(input(color.BOLD + "Ingrese el Numero" + color.END + " de pista: "))
        titulo =     str(input(color.BOLD + "Ingrese el Título" + color.END + " de la canción: " ))
        duracion =   str(input(color.BOLD + "Ingrese la Duración formato HH:MM:SS" + color.END + " de la canción: "))
        autor =      str(input(color.BOLD + "Ingrese la Autor" + color.END + " de la canción: "))
        compositor = str(input(color.BOLD + "Ingrese la Compositor" + color.END + " de la canción: "))



        print(color.BOLD + color.CYAN_CLARO)
        opcion = input("\n█ Que desea hacer? █ " + color.NARANJA + "1 (CARGAR LA CANCION) " + color.END + color.CYAN_CLARO + "█ 2 (Reingresar los datos) █ 3 (Cancelar) █\n\n" + color.END + color.BOLD + "Ingrese un número de opción: " + color.END)

        if opcion == "1":
            print("\nIntentando CARGA DE CANCION...")

            

            unacancion = abm.Tema(0,track_num,titulo,duracion,autor,compositor,id_album,interprete)  #(0,4,"Cancion 1",'',"Autor X","Compositor X",4,2)

            carga = abm.Cargar()
            carga.CargarCancion(unacancion)                
                             
            print(color.VERDE_CLARO + "\nCARGA DE CANCION CORRECTA" + color.END) 
            break

        elif opcion == "2":
            print("\nREINTENTANDO..")
            id_album = None
        elif opcion == "3":
            print("\nCANCELADO volviendo al menú principal.")
            break  
        else:
            print("¡Opción incorrecta!")


#------------------------------------------------

#TEST DE CLASE ALBUM. 

# consulta = consulta.Listar()
# resultados = consulta.idAlbumEspecifico(14)

# for dato in resultados:
#     Album = abm.Album(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9],dato[10],dato[11])

# variable = Album.getId_album()
# print(variable)

# variable = Album.getCod_album()
# print(variable)

# variable = Album.getNombre()
# print(variable)

# variable = Album.getId_interprete()
# print(variable)

# variable = Album.getId_genero()
# print(variable)

# variable = Album.getCant_temas()
# print(variable)

# variable = Album.getId_discografica()
# print(variable)

# variable = Album.getId_formato()
# print(variable)

# variable = Album.getFec_lanzamiento()
# print(variable)

# variable = Album.getCaratula()
# print(variable)


#-------------------------------------------------


# id_album = 14
# nuevo_cod = "JHGFDDD"
# #Hacemos el Query select para traer los datos del album en el orden correcto.
# getdatos = consulta.Listar()
# resultados = getdatos.idAlbumEspecifico(id_album)
# #Llenamos el objeto Album con los datos de la base de datos del id de album elegido.
# for dato in resultados:
#     Album = amb.Album(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9],dato[10],dato[11])

# variable = Album.getCod_album()
# print(variable)

# Album.setCod_album(nuevo_cod)


# variable = Album.getCod_album()
# print(variable)



#--------------------------------------------------------------------------------

#Carga de cancion descomentar para test:

#InsertarCancionCLI()

#--------------------------------------------------------------------------------
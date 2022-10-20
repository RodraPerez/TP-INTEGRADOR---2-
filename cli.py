#Interfaz de modo consola. En desarrollo.

import cargadatos
import formatodatos


def Menu():
    while True:
        print("\n+-------------------------------------------+")
        print("|         DISQUERÍA FORMOSA MUSICAL         |")
        print("+-------------------------------------------+\n")
        print("")
        print("MENÚ PRINCIPAL\n")
        print("1 - ALTA / BAJA / MODIFICACION DE UN ÁLBUM " + "4 - BÚSQUEDA POR NOMBRE DE ÁLBUM")
        print("2 - LISTADO DE ÁLBUMES POR ARTISTAS        " + "5 - INSERTAR INTERPRETE")
        print("3 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL  " + "6 - LISTADO DE INTERPRETES")
        print("7 - INSERTAR GENERO MUSICAL                " + "8 - LISTADO DE GENEROS MUSICALES")
        print("S - Salir")       
        print("\n")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            print("\033[0;31mFunción no disponible todavía.. \033[0m")
        elif opcion == "2":
            formatodatos.AlbumsVistaCLI()
        elif opcion == "3":
            formatodatos.MostrarAlbumsPorGeneroCLI()
        elif opcion == "4":
            formatodatos.MostrarAlbumPorNombreCLI()
        elif opcion == "5":
            formatodatos.InsertarInterpreteCLI()
        elif opcion == "6":
            formatodatos.MostrarInterpreteCLI()
        elif opcion == "7":
            formatodatos.insertarGeneroCLI()
        elif opcion == "8":
            formatodatos.MostrarGenerosCLI()
        elif (opcion == "s") or (opcion == "S"):
            break
        else:
            print("¡Opción incorrecta!")









    #Test de carga Interprete
    # carga = cargadatos.Cargar()
    # carga.CargarInterprete("Phil","Collins","UK","https://www.discos.com/lafotodelartista.jpg")


def IniciarInterfazConsola():
    print("\033[0;32m\033[1m[MODULO cli] Interfaz de Consola Iniciada..\033[0m")
    Menu()



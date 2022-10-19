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
        print("1 - ALTA / BAJA / MODIFICACION DE UN ÁLBUM")
        print("2 - LISTADO DE ÁLBUMES POR ARTISTAS")
        print("3 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
        print("4 - BÚSQUEDA POR NOMBRE DE ÁLBUM")
        print("5 - INSERTAR INTERPRETE")
        print("6 - SALIR")
        print("\n")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            print("\033[0;31m \033Función no disponible todavía.. \033[0m")
        elif opcion == 2:
            formatodatos.AlbumsVistaCLI()
        elif opcion == 3:
            formatodatos.MostrarAlbumsPorGenero()
        elif opcion == 4:
            formatodatos.MostrarAlbumPorNombreCLI()
        elif opcion == 5:
            print("\033[0;31m \033Función no disponible todavía.. \033[0m")
        elif opcion == 6:
            break
        else:
            print("¡Opción incorrecta!")









    #Test de carga Interprete
    # carga = cargadatos.Cargar()
    # carga.CargarInterprete("Phil","Collins","UK","https://www.discos.com/lafotodelartista.jpg")


def IniciarInterfazConsola():
    print("\033[0;32m\033[1m[MODULO cli] Interfaz de Consola Iniciada..\033[0m")
    Menu()



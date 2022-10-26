#Interfaz de modo consola.

import cli_formato
from cli_colores import ColoresCLI as color

class cli():
    def __init__(self):
        self.Iniciar()


    def Iniciar(self):
        print(color.VERDE_CLARO)
        print("[MODULO cli] Interfaz de Consola Iniciada..")
        print(color.END)
        self.GUIMenuPrincipal()

    def ErrorDeOpcion(self):
        print(color.ROJO_CLARO + color.BOLD)
        print("¡Opción incorrecta!, reintente nuevamente..")
        print(color.END)

    def GUIMenuPrincipal(self):
        while True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.BOLD + "MENÚ PRINCIPAL" + color.END + "\n")
            print("1 - ALTA / BAJA / MODIFICACION DE UN ÁLBUM ")
            print("2 - LISTADOS Y BUSQUEDAS                   ")
            print("3 - OTRAS OPCIONES                         ")
            print("S - Salir")       
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion == "1":
                self.GUIMenuABMAlbum()
            elif self.opcion == "2":
                self.GUIMenuListados()
            elif self.opcion == "3":
                self.GUIMenuOtros()
            elif self.opcion == "S" or self.opcion == "s":
                break
            else:
                self.ErrorDeOpcion()
                continue
            break #[!]

    def GUIMenuABMAlbum(self):
        while True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.CYAN_CLARO)
            print("GESTION DE ALBUMES\n")
            print("1 - ALTA DE UN ÁLBUM")
            print("2 - BAJA DE UN ÁLBUM")
            print("3 - MODIFICACION DE ALBUM")
            print("S - Salir")
            print(color.END)       
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion == "1":
                cli_formato.InsertarAlbumCLI()
            elif self.opcion == "2":
                print("Función BAJA ALBUM no disponible todavía..")
            elif self.opcion == "3":
                print("Función MODIFICACION ALBUM no disponible todavía..")
            elif self.opcion == "S" or self.opcion == "s":
                self.opcion == ""
                break            
            else:
                self.ErrorDeOpcion()
                continue

    def GUIMenuListados(self):
        while True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.VERDE_CLARO)
            print("GESTION DE CONSULTAS\n")
            print("1 > INFORMACION DETALLE DE UN ÁLBUM                      4 > LISTADO DE INTERPRETES")           
            print("2 > LISTA DE ALBUMES POR ARTISTA (NOMBRE ASC)            5 > LISTADO DE GENEROS MUSICALES")
            print("3 > LISTA DE ALBUMES DE UN GENERO MUSICAL ESPECIFICO     6 > LISTADO DE FORMATOS")
            print("S > Salir                                                7 > LISTADO DE DISCOGRAFICAS")              

            print(color.END)            
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion ==   "1":
                cli_formato.MostrarAlbumPorNombreCLI()
                continue
            elif self.opcion == "2":
                cli_formato.MostrarAlbumsPorInterpreteCLI()
                continue
            elif self.opcion == "3":
                cli_formato.MostrarAlbumsPorGeneroCLI()
                continue                
            elif self.opcion == "4":
                cli_formato.MostrarInterpreteCLI()
                continue  
            elif self.opcion == "5":
                cli_formato.MostrarGenerosCLI()   
                continue 
            elif self.opcion == "6":
                cli_formato.MostrarFormatosCLI()
                continue
            elif self.opcion == "7":
                cli_formato.MostrarDiscograficasCLI()
                continue
            elif self.opcion == "S" or self.opcion == "s":
                break            
            else:
                self.ErrorDeOpcion()
                continue

    def GUIMenuOtros(self):
        while True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.MORADO)
            print("OTRAS GESTIONES\n")
            print("1 - INSERTAR INTERPRETE")
            print("2 - INSERTAR GENERO MUSICAL")
            print("3 - INSERTAR FORMATO")
            print("4 - INSERTAR DISCOGRAFICA")            
            print("S - Salir")
            print(color.END)       
            print("\n")

            self.opcion = ""
            self.opcion = input("Ingrese su opción: ")

            if  self.opcion == "1":
                cli_formato.InsertarInterpreteCLI()
                continue
            elif self.opcion == "2":
                cli_formato.insertarGeneroCLI()
                continue
            elif self.opcion == "3":
                cli_formato.insertarFormatoCLI()
                continue
            elif self.opcion == "4":
                cli_formato.InsertarDiscograficaCLI()
                continue
            elif self.opcion == "S" or self.opcion == "s":
                break
            else:
                self.ErrorDeOpcion()
                continue
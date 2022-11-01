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
        self.flag = True
        self.GUIMenuPrincipal()

    def ErrorDeOpcion(self):
        print(color.ROJO_CLARO + color.BOLD)
        print("¡Opción incorrecta!, reintente nuevamente..")
        print(color.END)

    def GUIMenuPrincipal(self):
        while self.flag == True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.BOLD + "MENÚ PRINCIPAL" + color.END + "\n")
            print(color.NARANJA + "1" + color.END + "- ALTA / BAJA / MODIFICACION DE UN ÁLBUM ")
            print(color.NARANJA + "2" + color.END + "- LISTADOS Y BUSQUEDAS                   ")
            print(color.NARANJA + "3" + color.END + "- OTRAS OPCIONES DE CARGA                ")
            print("")
            print(color.NARANJA + "S" + color.END + "- Salir")       
            print("\n")

            self.opcion = input("Ingrese su opción: ")
            self.flag = False
            if self.opcion == "1":
                self.GUIMenuABMAlbum()
            elif self.opcion == "2":
                self.GUIMenuListados()
            elif self.opcion == "3":
                self.GUIMenuOtros()
            elif self.opcion == "S" or self.opcion == "s":
                exit()
            else:
                self.ErrorDeOpcion()
                self.flag = True
                continue 
                
    def GUIMenuABMAlbum(self):
        self.flag = True
        while self.flag == True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.CYAN_CLARO)
            print("GESTION DE ALBUMES\n")
            print(color.NARANJA + "1" + color.END + "- ALTA DE UN ÁLBUM")
            print(color.NARANJA + "2" + color.END + "- BAJA DE UN ÁLBUM")
            print(color.NARANJA + "3" + color.END + "- MODIFICACION DE ALBUM")
            print("")
            print(color.NARANJA + "S" + color.END + "- Salir")
            print(color.END)       
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion == "1":
                cli_formato.InsertarAlbumCLI()
                continue
            elif self.opcion == "2":
                cli_formato.EliminarAlbumCLI()
                continue
            elif self.opcion == "3":
                cli_formato.ModificarAlbumCLI()
                continue
            elif self.opcion == "S" or self.opcion == "s":
                self.GUIMenuPrincipal()
                self.flag = False      
            else:
                self.ErrorDeOpcion()
                self.flag = True
                continue

    def GUIMenuListados(self):
        self.flag = True
        while self.flag == True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.BOLD)
            print("GESTION DE CONSULTAS\n" + color.END + color.VERDE_CLARO)
            print("1 > INFORMACION DETALLE DE UN ÁLBUM                      5 > LISTADO DE INTERPRETES")           
            print("2 > LISTA DE ALBUMES POR ARTISTA (NOMBRE ASC)            6 > LISTADO DE GENEROS MUSICALES")
            print("3 > LISTA DE ALBUMES DE UN GENERO MUSICAL ESPECIFICO     7 > LISTADO DE FORMATOS")
            print("4 > LISTA DE CANCIONES POR AUTOR                         8 > LISTADO DE DISCOGRAFICAS" + color.END)              
            print("")
            print("S > SALIR")
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion == "1":
                cli_formato.MostrarAlbumPorNombreCLI()
                continue
            elif self.opcion == "2":
                cli_formato.MostrarAlbumsPorInterpreteCLI()
                continue
            elif self.opcion == "3":
                cli_formato.MostrarAlbumsPorGeneroCLI()
                continue    
            elif self.opcion == "4":
                cli_formato.MostrarTemaAutorCLI()
                continue                
            elif self.opcion == "5":
                cli_formato.MostrarInterpreteCLI()
                continue  
            elif self.opcion == "6":
                cli_formato.MostrarGenerosCLI()   
                continue 
            elif self.opcion == "7":
                cli_formato.MostrarFormatosCLI()
                continue
            elif self.opcion == "8":
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

            print(color.BOLD)
            print("OTRAS GESTIONES\n",color.END)
            print(color.NARANJA + "1" + color.END + " - INSERTAR INTERPRETE                 ", color.NARANJA + "6" + color.END + " - MODIFICAR INTERPRETE")
            print(color.NARANJA + "2" + color.END + " - INSERTAR GENERO MUSICAL             ",color.NARANJA + "7" + color.END + " - MODIFICAR CANCION")
            print(color.NARANJA + "3" + color.END + " - INSERTAR FORMATO")
            print(color.NARANJA + "4" + color.END + " - INSERTAR DISCOGRAFICA")
            print(color.NARANJA + "5" + color.END + " - INSERTAR CANCION A UN ALBUM")                       
            print("")                     
            print(color.NARANJA + "\nS" + color.END + " - Salir")
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
            elif self.opcion == "5":
                cli_formato.InsertarCancionCLI()
                continue
            elif self.opcion == "6":
                cli_formato.ModificarInterpreteCLI()
                continue
            elif self.opcion == "7":
                cli_formato.ModificarCancionCLI()
                continue
            elif self.opcion == "S" or self.opcion == "s":
                break
            else:
                self.ErrorDeOpcion()
                continue
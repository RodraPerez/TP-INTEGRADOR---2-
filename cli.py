#Interfaz de modo consola.
import os
import cli_formato
from cli_colores import ColoresCLI as color

class cli():
    def __init__(self):
        self.Iniciar()

    def Iniciar(self):
        os.system('cls')
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
        os.system('cls')
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
        os.system('cls')
        self.flag = True
        while self.flag == True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.CYAN_CLARO)
            print("GESTION DE ALBUMES\n")
            print(color.ROJO + "1" + color.END + " > ALTA DE UN ÁLBUM")
            print(color.ROJO + "2" + color.END + " > BAJA DE UN ÁLBUM")
            print(color.ROJO + "3" + color.END + " > MODIFICACION DE ALBUM")
            print("\n")
            print(color.CYAN_CLARO + "S"+ color.AZUL_CLARO + " - VOLVER MENU PRINCIPAL" + color.END)
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
        os.system('cls')
        self.flag = True
        while self.flag == True:
            print(color.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(color.END)

            print(color.VERDE_CLARO + color.BOLD)
            print("GESTION DE CONSULTAS\n" + color.END)
            print(color.CYAN_CLARO + "1" + color.END + " > INFORMACION DETALLE DE UN ÁLBUM                      " + color.CYAN_CLARO + "5" + color.END + " > LISTADO DE INTERPRETES")           
            print(color.CYAN_CLARO + "2" + color.END + " > LISTA DE ALBUMES POR ARTISTA (NOMBRE ASC)            " + color.CYAN_CLARO + "6" + color.END + " > LISTADO DE GENEROS MUSICALES")
            print(color.CYAN_CLARO + "3" + color.END + " > LISTA DE ALBUMES DE UN GENERO MUSICAL ESPECIFICO     " + color.CYAN_CLARO + "7" + color.END + " > LISTADO DE FORMATOS")
            print(color.CYAN_CLARO + "4" + color.END + " > LISTA DE CANCIONES SEGUN LO SOLICITADO               " + color.CYAN_CLARO + "8" + color.END + " > LISTADO DE DISCOGRAFICAS")              
            print("")
            print(color.CYAN_CLARO + "S > "+ color.AZUL_CLARO + "VOLVER MENU PRINCIPAL" + color.END)
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
                cli_formato.MostrarCanciones()
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
                self.GUIMenuPrincipal()
                self.flag = False            
            else:
                self.ErrorDeOpcion()
                self.flag = True
                continue

    def GUIMenuOtros(self):
        os.system('cls')
        self.flag = True
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
            print(color.CYAN_CLARO + "S"+ color.AZUL_CLARO + " - VOLVER MENU PRINCIPAL" + color.END)
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
                self.GUIMenuPrincipal()
                self.flag = False            
            else:
                self.ErrorDeOpcion()
                self.flag = True
                continue

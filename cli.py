#Interfaz de modo consola. En desarrollo.
import formatodatos
import colores

# Atencion con el tema de menus anidados en bucles https://peps.python.org/pep-3136/ ya que si no hacemos la modificacion quedamos atrapados en el primer bucle.


class cli(colores.ColoresCLI):
    def __init__(self):
        self.Iniciar()


    def Iniciar(self):
        print(self.VERDE_CLARO)
        print("[MODULO cli] Interfaz de Consola Iniciada..")
        print(self.END)
        self.GUIMenuPrincipal()

    def ErrorDeOpcion(self):
        print(self.ROJO_CLARO + self.BOLD)
        print("¡Opción incorrecta!, reintente nuevamente..")
        print(self.END)

    def GUIMenuPrincipal(self):
        while True:
            print(self.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(self.END)

            print(self.BOLD + "MENÚ PRINCIPAL" + self.END + "\n")
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
            print(self.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(self.END)

            print(self.CYAN_CLARO)
            print("GESTION DE ALBUMES\n")
            print("1 - ALTA DE UN ÁLBUM")
            print("2 - BAJA DE UN ÁLBUM")
            print("3 - MODIFICACION DE ALBUM")
            print("S - Salir")
            print(self.END)       
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion == "1":
                print("\033[0;31mFunción ALTA ALBUM no disponible todavía.. \033[0m")
            elif self.opcion == "2":
                print("\033[0;31mFunción BAJA ALBUM no disponible todavía.. \033[0m")
            elif self.opcion == "3":
                print("\033[0;31mFunción MODIFICACION ALBUM no disponible todavía.. \033[0m")
            elif self.opcion == "S" or self.opcion == "s":
                self.opcion == ""
                break            
            else:
                self.ErrorDeOpcion()
                continue

    def GUIMenuListados(self):
        while True:
            print(self.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(self.END)

            print(self.VERDE_CLARO)
            print("GESTION DE CONSULTAS")
            print("1 > BÚSQUEDA POR NOMBRE DE ÁLBUM (FULL INFO)          7 > LISTA DE INTERPRETES")           
            print("2 > LISTA DE ALBUMES POR ARTISTA (NOMBRE ASC)         8 > LISTADO DE GENEROS MUSICALES")
            print("3 > LISTA DE ALBUMES DE UN GENERO MUSICAL ESPECIFICO  9 > LISTADO DE FORMATOS")
            print("4 > LISTA DE ALBUMES POR TIPO DE FORMATO             10 > LISTAR TODAS LAS CANCIONES")
            print("5 > LISTA DE ALBUMES EN STOCK                        11 > BUSCAR CANCION POR NOMBRE")
            print("6 > LISTA DE ALBUMES SIN STOCK                       12 > BUSCAR INTERPRETE POR NOMBRE")               
            print("S > Salir                                            13 > LISTADO DE DISCOGRAFICAS")       
            print(self.END)            
            print("\n")

            self.opcion = input("Ingrese su opción: ")

            if self.opcion ==   "1":
                formatodatos.MostrarAlbumPorNombreCLI()
                continue
            elif self.opcion == "2":
                formatodatos.MostrarAlbumsPorInterpreteCLI()
                continue
            elif self.opcion == "3":
                formatodatos.MostrarAlbumsPorGeneroCLI()
                continue                
            elif self.opcion == "4":
                print("falta este listado")
                continue
            elif self.opcion == "5":
                print("falta este listado")
                continue
            elif self.opcion == "6":
                print("falta este listado")
                continue
            elif self.opcion == "7":
                formatodatos.MostrarInterpreteCLI()
                continue  
            elif self.opcion == "8":
                formatodatos.MostrarGenerosCLI()   
                continue 
            elif self.opcion == "9":
                print("falta este listado")
                continue
            elif self.opcion == "10":
                print("falta este listado")
                continue
            elif self.opcion == "11":
                print("falta este listado")
                continue
            elif self.opcion == "12":
                print("falta este listado")
                continue
            elif self.opcion == "13":
                print("falta este listado")
                continue
            elif self.opcion == "S" or self.opcion == "s":
                break            
            else:
                self.ErrorDeOpcion()
                continue

    def GUIMenuOtros(self):
        while True:
            print(self.AZUL_CLARO)
            print("\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print(  "      DISQUERÍA FORMOSA MUSICAL      ")
            print(  "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
            print(self.END)

            print(self.MORADO)
            print("OTRAS GESTIONES\n")
            print("1 - INSERTAR INTERPRETE")
            print("2 - INSERTAR GENERO MUSICAL")
            print("3 - INSERTAR FORMATO")
            print("4 - INSERTAR DISCOGRAFICA")            
            print("S - Salir")
            print(self.END)       
            print("\n")

            self.opcion = ""
            self.opcion = input("Ingrese su opción: ")

            if  self.opcion == "1":
                formatodatos.InsertarInterpreteCLI()
                continue
            elif self.opcion == "2":
                formatodatos.insertarGeneroCLI()
                continue
            elif self.opcion == "3":
                print("falta este insert")
                continue
            elif self.opcion == "4":
                print("falta este insert")
                continue
            elif self.opcion == "S" or self.opcion == "s":
                break
            else:
                self.ErrorDeOpcion()
                continue
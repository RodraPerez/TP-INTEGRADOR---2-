import mysql.connector                                                                  #Se importa el driver MySQL para Python.

class Conectar():                                                                       # Se crea la clase de conecxion.
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(                                    # Se configuran los parámetros del conector. PONER PASS DE SU MYSQL.
                host = "localhost",
                port = "3306",
                user = "root",
                password = "",
                db = "disqueria"
            )

        except mysql.connector.Error as conexionError:                                  # En caso de error almacenamos el texto descriptivo del error del metodo en una 
            print("No se pudo conectar al servidor de Base de Datos",conexionError)     # variable. y la pasamos al print con una descripcion personalizada pero detallada.




    def ListarAlbums(self):                                                              #Método para consultar Base de Datos
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT cod_album, nombre, fec_lanzamiento FROM album")    #Sentencia SQL
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as conexionError:
                print("No se pudo conectar para hacer la consulta.",conexionError)


con = Conectar()                                                                         #Se crea la instancia de la Clase Conectar() se almacena en la variable "con"

for album in con.ListarAlbums():                                  # bucle for que recorre el return "resultados" de ListarAlbums() y va imprimiendo cada item de la lista.
    print(album)

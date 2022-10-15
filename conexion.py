import mysql.connector                                          #Se importa el driver MySQL para Python.

class BaseDatos():                                              #Se crea la clase de conecxion.
    def __init__(self):
        print("Instanciada Clase Base de Datos..")              #Print Debug..

    def Conectar(self):                                         #Metodo para conectarse a la Base de Datos
        try:
            self.conexion = mysql.connector.connect(
            host = 'localhost', #si no conecta con esto probamos con 127.0.0.1
            port = 3306,
            user = 'root',
            password = '',   #NO OLVIDAR Configurar con su pass, y antes de hacer commit borrarlo.
            db = 'disqueria' #nombre de la base de datos
            )
            if self.conexion.is_connected():
                print("La conexion es exitosa.")

        except mysql.connector.Error as error:
            print("¡No se conectó!")
            print(error)

    def Desconectar(self):                                      #Metodo para Desconectarse de la Base de Datos

        if self.conexion.is_connected():
            self.conexion.close()
            print("La conexión se cerró")

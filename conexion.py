#Modulo de conexion, con desconexion automatica por defecto luego de operar.

import mysql.connector                                          #Se importa el driver MySQL para Python.

class BaseDatos():                                              #Se crea la clase de conecxion.
    def __init__(self):
        print("[CONEXION] load.")              

    def Conectar(self):                                         #Metodo para conectarse a la Base de Datos
        try:
            self.conexion = mysql.connector.connect(
            host = 'localhost', #si no conecta con esto probamos con 127.0.0.1
            port = 3306,
            user = 'root',
            password = '36144709Leo',   #NO OLVIDAR Configurar con su pass, y antes de hacer commit borrarlo.
            db = 'disqueria' #nombre de la base de datos
            )
            if self.conexion.is_connected():
                print("[CONEXION] La conexion es exitosa.")

        except mysql.connector.Error as error:
            print("[CONEXION] ¡No se conectó!")
            print(error)

    def Desconectar(self):                                      #Metodo para Desconectarse de la Base de Datos

        if self.conexion.is_connected():
            self.conexion.close()
            print("[CONEXION] La conexión se cerró\n")


    def QuerySQL(self,query):  #Recibimos la query SQL desde cualquier llamando al metodo del objeto con un solo parametro
        self.query = query

        if self.conexion.is_connected():
            try:
                #Cursor y query recibida::
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)
                #print("[CONEXION] Ejecutada selnencia SQL..") #print debug

                #Almacenamos bajada de datos en una Variable Buffer.
                self.listado = self.cursor.fetchall()
                #print("[CONEXION] Datos en cache [OK]..") #print debug

                #Desconectamos por defecto en cualquier operacion, podemos llamar al metodo si deseamos conexión fija (no se recomienda)
                self.Desconectar()  #   <-----------------

                return self.listado

            except self.mysql.connector.Error as Error:
                print("[CONEXION] [QuerySQL] No hay conexion con la base de datos.",Error)

    
    def abmSQL(self,query,data):  # Recibo sentencia SQL y Datos.

        self.query = query
        self.data = data

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()

                self.cursor.execute(self.query,self.data)

                self.conexion.commit() #[!]

                #print("[CONEXION] Commit [OK].") 

            except self.mysql.connector.Error as Error:
                print("[CONEXION] [abmSQL] No hay conexion con la base de datos.",Error)

        #Desconectamos por defecto en cualquier operacion, podemos llamar al metodo si deseamos conexión fija (no se recomienda)
        self.Desconectar()
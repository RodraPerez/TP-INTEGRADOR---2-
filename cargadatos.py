# Modulo de funcion de carga de datos.

import conexion

class Cargar(conexion.BaseDatos):
    def __init__(self):
        print("Instanciada Clase de Carga de datos..")  # Print Debug
        conexion.BaseDatos.__init__(self)
    
    def CargarArtista(self,nombre,apellido,nacionalidad,foto): #Edgar G - Cargar un Interprete.    
        # Tabla Interprete:  id_interprete(autoincremental),nombre,apellido,nacionalidad,foto
        self.Conectar()

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.query = "INSERT IGNORE INTO interprete VALUES(null,%s,%s,%s,%s)"  #Evitamos cargar duplicado.

                self.datos_envio = (nombre,apellido,nacionalidad,foto) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.
                self.cursor.execute(self.query,self.datos_envio)

                self.conexion.commit()
                print("Artista Cargado en Base de Datos.") #Si ya esta cargado, o si se cargó el registro.

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
        self.Desconectar()








            

# Modulo de funcion de carga de datos.

import conexion

class Cargar(conexion.BaseDatos):
    def __init__(self):
        print("Instanciada Clase de Carga de datos..")  # Print Debug
        conexion.BaseDatos.__init__(self)
    
    def CargarInterprete(self,nombre,apellido,nacionalidad,foto): #Edgar G - Cargar un Interprete.    
        # Tabla Interprete:  id_interprete(autoincremental),nombre,apellido,nacionalidad,foto
        self.Conectar()

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.query = "INSERT IGNORE INTO interprete VALUES(null,%s,%s,%s,%s)"  #Evitamos cargar duplicado.

                self.datos_envio = (nombre,apellido,nacionalidad,foto) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.
                self.cursor.execute(self.query,self.datos_envio)

                self.conexion.commit()
                print("\033[1mEjecutada carga de un Interprete. \033[0m") #Si ya esta cargado, o si se cargó el registro.

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
        self.Desconectar()

#----------------------------------------------------------------------------------
    #Nico - Cargar un Album.
    def CargarAlbum(self,codigoAlbum, nombre,idInterprete,idGenero,catidadTemas, idDiscografica, idFormato, fechaLanzamiento, precio, cantidad, caratula):     
        # Album:   id_album, cod_album,   nombre,   id_interprete, id_genero, cant_temas, id_discografica,  id_formato,  fec_lanzamiento,  precio,cantidad,  caratula
        self.Conectar()

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.query = "INSERT IGNORE INTO album VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  #Evitamos cargar duplicado.

                self.datos_envio = (codigoAlbum, nombre,idInterprete,idGenero,catidadTemas, idDiscografica, idFormato, fechaLanzamiento, precio, cantidad, caratula) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.
                self.cursor.execute(self.query,self.datos_envio)

                self.conexion.commit()
                print("\033[1mEjecutada carga de un Album. \033[0m") #Si ya esta cargado, o si se cargó el registro.

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
        self.Desconectar()

#----------------------------------------------------------------------------------

    def CargarGenero(self,nombre): #Cargar un Género musical.    
        # Tabla Interprete:  id_interprete(autoincremental),nombre,apellido,nacionalidad,foto
        self.Conectar()

        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.query = "INSERT IGNORE INTO genero VALUES(null,%s)"  #Evitamos cargar duplicado.

                self.datos_envio = (nombre,) #Creamos la tupla, si la tupla tiene un solo item dejar coma al final.
                self.cursor.execute(self.query,self.datos_envio)

                self.conexion.commit()
                print("\033[1mEjecutada carga de un Género Musical. \033[0m") #Si ya esta cargado, o si se cargó el registro.

            except self.mysql.connector.Error as Error:
                print("No hay conexion con la base de datos.",Error)
        
        self.Desconectar()

#----------------------------------------------------------------------------------
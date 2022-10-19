import sys         #Para acceder a los argumentos por medio del metodo ".argv" (argument value)
import cli         #Para interfaz de consola en cli.py
import interfaz    #Para la interfaz de Ventana en interfaz.py

def main():
    #Del modulo sys de sistema capturamos los comandos o argumentos adicionales con la ejecucion de nuestro Disqueria.py, como string de texto..
    #Se los parametros se almacenan en una lista que devuelve el metodo sys.argv[], la posicion de la lista sys.argv[0] es el nombre del script actual,
    #elegimos el segundo de la lista [1] [1:] pasando a ser el primero [0]. Ya que si no tomaria tambien el Disqueria.py como argumento.

    seleccion_modo = sys.argv[1:] # filtramos al nombre del script actual como parametro. ['Disqueria.py','--ModoVentana'] >>> quedando ['--ModoVentana']

    opcion1 = "--ModoConsola"
    opcion2 = "--ModoVentana"

    ayuda =     """\n Para iniciar el programa Seleccione un modo de interfaz: \n
                Disqueria.py --ModoConsola  (Inicia en modo consola de texto)
                Disqueria.py --ModoVentana  (Inicia en modo Ventana)"""

    #Evitamos cero argumentos o cualquier otro ingreso distinto de las opciones.
    if (len(seleccion_modo) == 0 or ((seleccion_modo[0] != opcion1) and (seleccion_modo[0] != opcion2))): 
        print (ayuda)

    elif seleccion_modo[0] == opcion1:
        print("[MAIN] Entrando al modo consola..")
        cli.IniciarInterfazConsola()  #llamamos al modulo con la interfaz consola

    elif seleccion_modo[0] == opcion2:
        print("[MAIN] Entrando al modo ventana..")
        interfaz.IniciarInterfazVentana()   # llamamos al modulo con la interfaz Ventana
    


if __name__ == '__main__':
    main()
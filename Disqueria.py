import sys         #Para acceder a los argumentos por medio del metodo ".argv" (argument value)
import cli         #Para interfaz de consola en cli.py
from cli_colores import ColoresCLI as color

def main():
    #Del modulo sys de sistema capturamos los comandos o argumentos adicionales con la ejecucion de nuestro Disqueria.py, como string de texto..
    #Se los parametros se almacenan en una lista que devuelve el metodo sys.argv[], la posicion de la lista sys.argv[0] es el nombre del script actual,
    #elegimos el segundo de la lista [1] [1:] pasando a ser el primero [0]. Ya que si no tomaria tambien el Disqueria.py como argumento.

    seleccion_modo = sys.argv[1:] # filtramos al nombre del script actual como parametro. ['Disqueria.py','--ModoVentana'] >>> quedando ['--ModoVentana']

    opcion1 = "--ModoConsola"
    opcion2 = "--AcercaDe"

    info = color.BOLD + "\nSoft de gestión de albumes de Disquería, realizado en Python 3 por Alumnos ISPC TSIT 4.0 - 2022 (TP2)" + color.END + "\n\n" + color.AZUL_CLARO + "Integrantes: Leandro Torres  - Edgar Gil - Rodrigo Perez - Milena Coyante Arias - Nicolás Ignacio Radín" + color.END

    ayuda =     """\n Bienvenido, para iniciar el programa seleccione un modo de interfaz: \n
                Escriba el comando de la manera indicada más abajo.

                Disqueria.py --ModoConsola  (Inicia gestión en modo Consola de texto)
                Disqueria.py --AcercaDe     (Muestra información del programa)"""

    #Evitamos cero argumentos o cualquier otro ingreso distinto de las opciones.
    if (len(seleccion_modo) == 0 or ((seleccion_modo[0] != opcion1) and (seleccion_modo[0] != opcion2))): 
        print (ayuda)

    elif seleccion_modo[0] == opcion1:
        print("[MAIN] Entrando al modo consola..")
        consola = cli.cli()
        consola.Iniciar()

    elif seleccion_modo[0] == opcion2:
        print(info)
        # Acerca De..


if __name__ == '__main__':
    main()
#Interfaz de modo consola. En desarrollo.

import consulta
import cargadatos



def Menu():
    #Primera Lista
    busqueda = consulta.ListarAlbums()
    busqueda.PorGenero("Instrumental")

    #Segunda Lista
    busqueda = consulta.ListarAlbums()
    busqueda.PorArtista("Michael","Jackson")

    #Consulta todos los Interpretes
    Listar1 = consulta.ListarInterpretes()
    Listar1.ListaCompleta()

    # #Consulta todos los Generos
    # Listar2 = consulta.ListarGeneros()
    # Listar2.ListaCompleta()

    # #Consulta todos los Formatos
    # Listar3 = consulta.ListarFormatos()
    # Listar3.ListaCompleta()

    # #Consulta todas las Discograficas
    # Listar4 = consulta.ListarDiscograficas()
    # Listar4.ListaCompleta()

    # #Consulta todos los Temas
    # Listar5 = consulta.ListarCanciones()
    # Listar5.ListaCompleta()

    #Test de carga Interprete
    # carga = cargadatos.Cargar()
    # carga.CargarInterprete("Phil","Collins","UK","https://www.discos.com/lafotodelartista.jpg")

def IniciarInterfazConsola():
    print("\033[0;32m\033[1m[MODULO cli] Interfaz de Consola Iniciada..\033[0m")
    Menu()

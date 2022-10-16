import consulta
import cargadatos


def main():
    
    #Primera Lista
    busqueda = consulta.ListarAlbums()
    busqueda.PorGenero("Instrumental")

    #Segunda Lista
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














if __name__ == '__main__':
    main()
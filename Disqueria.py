import consulta
import cargadatos


def main():
    
    #Primera Lista
    busqueda = consulta.ListarAlbums()
    busqueda.PorGenero("Instrumental")

    busqueda2 = consulta.ListarAlbums()
    busqueda2.PorArtista("Michael","Jackson")

    carga = cargadatos.Cargar()
    carga.CargarInterprete("Phil","Collins","UK","https://www.discos.com/lafotodelartista.jpg")
    














if __name__ == '__main__':
    main()
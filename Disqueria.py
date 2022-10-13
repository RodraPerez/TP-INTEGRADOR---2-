import consulta


def main():
    
    #Primera Lista
    busqueda = consulta.ListarAlbums()
    busqueda.PorGenero("Instrumental")

    busqueda2 = consulta.ListarAlbums()
    busqueda2.PorArtista("Michael","Jackson")














if __name__ == '__main__':
    main()
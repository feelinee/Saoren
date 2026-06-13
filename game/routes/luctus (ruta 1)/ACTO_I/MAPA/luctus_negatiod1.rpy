label mercado_d1:
    "dia1 mercado"
    if ana_tumba:
        "Voy a comprarle la comida al gatito"
        $ gato_comi = True
    else:
        "Traje la comida para el gatito o podria comprarle las flores a Ana...."
        menu:
            "Voy a buscar al gatito":
                call gatod1
            "Anaraith...":
                call floresd1
                
    $ dia_mapa += 1
    jump mapa
    return

label gatod1:
    "ya le di la comida"
    $ gato_comi_usad= True
    return

label floresd1:
    "ya compre las flores"
    $ asfo_ramo= True
    return

label libreria_d1:
    "dia1 libreria"
    $ dia_mapa += 1
    jump mapa   
    return

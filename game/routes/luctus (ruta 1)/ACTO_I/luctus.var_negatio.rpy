#Defaults

default dia_mapa = 1

default gato_comi = False
default gato_comi_usad = False
default asfo_ramo = False

default asfo_flor = False
default mag_libro = False

#Mapa

label mapa:

    if dia_mapa == 1:
        $ lugares = ["mercado", "libreria"]
    elif dia_mapa == 2:
        $ lugares = ["bosque", "puerto"]
    elif dia_mapa == 3:
        $ lugares = ["tumba"]
    elif dia_mapa == 4:
        $ lugares = ["libreria", "bosque"]
    elif dia_mapa == 5:
        $ lugares = ["mercado", "puerto"]
    elif dia_mapa == 6:
        $ lugares = ["mercado", "libreria", "bosque", "puerto"]

    menu:
        "Mercado" if "mercado" in lugares:
            if dia_mapa == 1:
                jump mercado_d1
            elif dia_mapa == 5:
                jump mercado_d5
            elif dia_mapa == 6:
                jump negatio_escena2

        "Libreria" if "libreria" in lugares:
            if dia_mapa == 1:
                jump libreria_d1
            elif dia_mapa == 4:
                jump libreria_4
            elif dia_mapa == 6:
                jump negatio_escena2

        "Bosque" if "bosque" in lugares:
            if dia_mapa == 2:
                jump bosque_d2
            elif dia_mapa == 4:
                jump bosque_d4
            elif dia_mapa == 6:
                jump negatio_escena2
        
        "Puerto" if "puerto" in lugares:
            if dia_mapa == 2:
                jump puerto_d2
            elif dia_mapa == 5:
                jump puerto_d5
            elif dia_mapa == 6:
                jump negatio_escena2

        "Tumba" if "tumba" in lugares:
            jump tumba

    
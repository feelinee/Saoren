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
                jump luctus_negatio2

        "Libreria" if "libreria" in lugares:
            if dia_mapa == 1:
                jump libreria_d1
            elif dia_mapa == 4:
                jump libreria_d4
            elif dia_mapa == 6:
                jump luctus_negatio2

        "Bosque" if "bosque" in lugares:
            if dia_mapa == 2:
                jump bosque_d2
            elif dia_mapa == 4:
                jump bosque_d4
            elif dia_mapa == 6:
                jump luctus_negatio2
        
        "Puerto" if "puerto" in lugares:
            if dia_mapa == 2:
                jump puerto_d2
            elif dia_mapa == 5:
                jump puerto_d5
            elif dia_mapa == 6:
                jump luctus_negatio2

        "Tumba" if "tumba" in lugares:
            jump tumba

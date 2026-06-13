label negatio_d3:
    #pavel dice que puta paja
    "dia3pt1"
    if asfo_ramo:
        "dia3pt2.2 tienes el ramo! a la tumba"
        call mapa
    else:
        #Pavel dice que va a ir a la tumba hoy porque no le llevo flores la ultima vez.
        "dia3pt2.2 no hay ramo..."
        call casa_d3
    $ dia_mapa += 1
    jump mapa

label casa_d3:
    "dia3pt3.1 casa"
    #Pavel dice que va a aprovechar de limpiar
    #Encuentra un libro relacionado con Magnus
    $ mag_libro = True
    return

label tumba:
    #Pasa a comprar las flores y va directo a la tumba
    #habla un poco con ella y toma una de las flores del ramo
    "dia3p3.2 tumba"
    $ asfo_flor= True
    $ ana_tumba= True 
    return
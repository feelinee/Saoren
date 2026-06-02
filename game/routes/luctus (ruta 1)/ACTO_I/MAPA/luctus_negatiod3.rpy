label negatio_d3:
    #pavel dice que puta paja
    if asfo_ramo:
        jump casa_d3
    else:
        #Pavel dice que va a ir a la tumba hoy porque no le llevo flores la ultima vez.
        jump mapa

label casa_d3:
    #Pavel dice que va a aprovechar de limpiar
    #Encuentra un libro relacionado con Magnus
    $ mag_libro = True
    $ dia_mapa += 1
    jump mapa

label tumba:
    #Pasa a comprar las flores y va directo a la tumba
    #habla un poco con ella y toma una de las flores del ramo
    $ asfo_flor = True
    $ dia_mapa += 1
    jump mapa  
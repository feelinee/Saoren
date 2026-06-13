label bosque_d4:
    "d4 bosquee"
    #*Pavel entra al bosque y sigue el camino hacia la tumba, pero la evita, no quiere ir ese día.*
    #*Se hacerca a la "puerta", el lugar donde se separaron él y Anaraith… él y marcille.*
    #*Aunque no vio a marcille pasar, el saber que se podia le da sentimientos encontrados*
    #*se pregunta si hubiera cambiado algo ese dia si hubiera podido pasar.*
    #*Los árboles tienen ojos, y Pavel los siente recorrer su cuerpo. Se siente asqueroso y decide irse*
    #*mientras camina escucha ramillas romperse detrás suyo, imagina que son los animales asiq trata de no prestarles mucha atención*

    if mag_libro:
        "dia4pt1.1 tienes el libro de magnus"
        call bosque_d4p
    elif ana_tumba: 
        "dia4pt1.2 fuiste a la tumba"
        call bosque_d4t
    
    $ dia_mapa += 1
    jump mapa
    return

label bosque_d4p:
    "dia4pt2.1 pavel paranoico duerme"
    #*pero no paran de romperse*
    #*y los pasos detrás suyo no paran*
    #*empieza a sudar frio y acelera el camino hacia la ciudad*
    #*siente como le toman el brazo y practicamente lo arrastran*
    #*Es marcille, y pavel piensa que realmente tiene que dejar de hacer eso*
    #*le lanza una mirada enojada y se suelta de su brazo*
    #*le indica con la mano que espere, y escribe lo más rapido que puede*
    #*practicamente le tira la libreta en la cara y se aleja un poco más, acariciandose el brazo,*
    #“Dejame en paz, ya te dije que no”
    #*marcille lo mira y pavel le quita la libreta de un tirón y empieza a caminar en dirección a su casa*
    #*Siente como marcille lo llama y lo sigue pero ya no le presta atención*
    return

label bosque_d4t:
    "dia4pt2.2 pavel triste no duerme"
    #*mantiene el paso firme y lento, mirando el atardecer en el cielo ¿cuanto tiempo se habia parado ahí mirando a la nada?*
    #*se lamenta del tiempo perdido suspirando, el camino a su casa es tranquilo pero siente que sus pasos son lentos y el tiempo muy rapido*
    #*al llegar a la puerta de su casa se da la vuelta y lo ve ahí*
    #*su altura impone, pero aún rodeado de arboles se ve solitario*
    #*una costumbre vieja lo insita a pedirle que pase, pues es su casa también*
    #*finalmente abre la puerta, pero la cierra detrás suyo inmediatamente*
    #*esa noche fue demasiado  larga puede dormir*
    #variable no durmió(?
    $ pav_dur = False
    return

label libreria_d4:
    "dia4 libreria"
    if mag_libro:
        "Voy a dejar el libro que me encontré, no me gusta verlo en la casa."
        $ mag_libro_entr= True
        #si entrega el libro le vienen recuerdos de magnus, y se ablanda si se encuentra con él después, si no lo entrega, cuando se encuentra con él, no recuerda nada y le lanza el libro en la cara.
        return
    else:

    $ dia_mapa += 1
    jump mapa
    return

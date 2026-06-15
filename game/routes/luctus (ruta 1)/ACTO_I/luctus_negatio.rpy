label luctus_negatio:
    nvl clear
    show fondo negro
    show text "«Tu y yo no somos tan distintos...»"
    pause
    show text "«¿No?»"
    pause
    show text "«...»"
    pause
    hide text
    hide fondo negro

    scene bg gato
    $ color_mode = "green"
    call mode_medio
    "El gato,{w=0.3} que no parece haber entendido mi duda,{w=0.3} se restriega por mi pierna maullando para que lo acaricie."
    "Le susurro un maullido devuelta{cps=2.0}... {cps=12}pero no me responde,{w=0.2} en vez de eso muestra su abdomen,{w=0.2} y yo me agacho para acariciarlo."
    "—Hey chico,{w=0.3} ya está tu pedido."
    "«Ah.»"
    nvl clear
    
    "Me levanto,{w=0.3} y rapidamente me limpio las manos en la chaqueta, sacando una pequeña libreta de mi bolso junto con un par de monedas."
    "El señor apunta todo lo que hay en ella para comprobar que no falte nada."
    "Recibo la bolsa y arranco una de las páginas para entregarsela."
    "\"Gracias.\""
    nvl clear

    "Voy a la ultima hoja de la libreta, donde tengo mi lista de compras para hoy."
    nvl clear

    "LISTA DE COMPRAS ₍^. .^₎\n————————————————————————{fast}{w=0.3}{nw}"
    "— {s}2 Manzanas{/s}{fast}{w=0.3}{nw}"
    "— {s}1kg de harina{/s}{fast}{w=0.3}{nw}" 
    "— Huevo{fast}{w=0.3}{nw}"
    "— Mantequilla{fast}{w=0.3}{nw}"
    "— 2 de pan{fast}{w=0.3}{nw}"
    "— Ramo de flores{fast}"
    nvl clear

    "Lo guardo momentaneamente y tomo mi monedero, dejando caer las monedas en mi mano."
    "«Dos...{w=0.3} Seis...{w=0.3} Doce...»"
    "«Solo me quedan dieciocho fides...»"
    "«...»"
    "Saco mi libreta nuevamente y anoto de todas maneras."
    nvl clear

    "LISTA DE COMPRAS ₍^. .^₎\n————————————————————————{fast}{w=0.3}{nw}" 
    "— {s}2 Manzanas{/s}{fast}{w=0.3}{nw}"
    "— {s}1kg de harina{/s}{fast}{w=0.3}{nw}" 
    "— Huevo{fast}{w=0.3}{nw}"
    "— Mantequilla{fast}{w=0.3}{nw}"
    "— 2 de pan{fast}{w=0.3}{nw}"
    "— Ramo de flores{fast}{w=0.3}{nw}"
    "— Comida para gatos"
    nvl clear

    "Si la chica de las flores —olvide su nombre de nuevo—, tiene un ramo en oferta, podre comprarlo."
    "Me agacho una ultima vez y llamo al gato con un gesto de mis manos."
    "..."
    "Pronto se acerca y se deja acariciar por mi. "
    "«La siguiente vez que te vea, espero poder traerte algo de regalo»."
    nvl clear

    "Empiezo a caminar hacia el siguiente puesto,"
    nvl clear

    "LISTA DE COMPRAS ₍^. .^₎\n————————————————————————{fast}{w=0.3}{nw}"
    "— {s}2 Manzanas{/s}{fast}{w=0.3}{nw}"
    "— {s}1kg de harina{/s}{fast}{w=0.3}{nw}"
    "— Huevo{fast}{w=0.3}{nw}"
    "— Mantequilla{fast}{w=0.3}{nw}"
    "— {s}2 de pan{/s}{w=0.3}{nw}"
    "— Ramo de flores{fast}{w=0.3}{nw}"
    "— Comida para gatos{fast}"
    nvl clear

    "Empiezo a caminar hacia el siguiente puesto,{fast} y el siguiente,"
    nvl clear

    "LISTA DE COMPRAS ₍^. .^₎\n————————————————————————{fast}{w=0.3}{nw}"
    "— {s}2 Manzanas{/s}{fast}{w=0.3}{nw}"
    "— {s}1kg de harina{/s}{fast}{w=0.3}{nw}"
    "— {s}Huevo{/s}{w=0.3}{nw}"
    "— {s}Mantequilla{/s}{w=0.3}{nw}"
    "— {s}2 de pan{/s}{fast}{w=0.3}{nw}"
    "— Ramo de flores{fast}{w=0.3}{nw}"
    "— Comida para gatos{fast}"
    nvl clear
    
    "Empiezo a caminar hacia el siguiente puesto, y el siguiente,{fast} y llego a un dilema..."
    "El puesto de carne es el más cercano, si compro ahí primero luego puedo comprar las flores e irme directo a mi casa."
    "Por otro lado, si voy primero al puesto de flores, puedo comprobar si hay una oferta antes de comprar la comida, pero me tendré que dar la vuelta dos veces..."
    nvl clear
    
    "Al final creo que..."
    menu:
        "El puesto de flores":
            call negatio_flores

        "El puesto de carne":
            call negatio_carne
    
    jump mapa

label negatio_carne:
    $ gato_comi = True
    $ color_mode = "orange"
    scene bg pavcille
    extend " primero voy a ir al puesto de carne."
    return

    #Pavel llega al puesto de carne y compra la comida de gato, cuando le pasa el dinero, el vendedor le susurra que tenga cuidado, pues nota que alguien venia con pavel y lo estaba mirando desde lejos, pavel se asusta y decide ir rapido al otro puesto para irse.

    #Antes de llegar a la tienda de flores, nota por el rabillo del ojo a la persona que lo está siguiendo, es bastante alto y aunque no parece tner mucha masa muscular, es suficiente para intimidarlo, decide meterse entre la muchedumbre.

    #Destacando por su altura como la persona lo empieza a buscar con la mirada, por su cara tapada asume que es alguien de la iglesia y que está en peligro.

    #Mira nuevamentse al rededor y no lo ve más, por lo que un poco más tranquilo decide irse a su casa, no obstante, este chico lo agarra del brazo con fuerza.

    #Pavel sin saber que hacer intenta safarse sin exito, sin poder correr ni gritar se paraliza del miedo y empieza a temblar, apretando el brazo del extraño con las uñas.

    #Marcile le pregunta si es el, y pavel incapaz de mirarlo no dice nada. Marcille pronto aclara su identidad, y pavel finalmente lo mira.

    #Aunque tenia la cara un poco cambiada era él.

    #Marcille le dicen que se alejen de la multitud para hablar bien y se van, pavel camina para calmarse, e inconsientemente empieza a caminar hacia donde se dirigia originalmente.

label negatio_flores:
    $ ana_tumba= True
    extend " primero voy a ir al puesto de flores."
    return
    

    #Pavel va al puesto de flores y pregunta por el precio, viendo que ya se hizo tarde se resigna y compra las flores, prometiendo para si mismo comprarlas otro dia.

label negatio_escena2:
    "escena 2 yay"
    return

##Escena 2 (mover a cap 1):
#"Me despierto con los ojos cerrados, un frio punzante me eriza la piel."
#show pavel neutral at right
#mar "Pavel, vamos, tienes que despertar. "
#show pavel neutral at left
#pav "Mmmm okay."
#show pavel enojado at right
#mar "¿porqué tenemos el mismo sprite..?"
#show pavel dudoso at left
#pav "qué."
#"Sin querer seguir su destino me sujeté fuerte de la pared con una mano."
#mar"Abre los ojos, dios."
#"Y los abrí, pero no habia ningún dios{w}, o al menos yo no lo ví."
#"La oscuridad de la habitación se me hacia ver tanto como veia cuando los tenia cerrados."
#"Así que los cerré." 
#pav "pico pal que lee xdxdxdxd"
#show pavel neutral at right
#"La pregunta cae de los árboles como la nieve."
#El libro que encuentra pavel mientras limpia es el que compro anaraith antes de morir, lo abre para ver de qué se trata y se rie con asco. Es el libro del prólogo.

label luctus_negatio:
    nvl clear
    scene scen nega1
    show text "«Tu y yo...»"
    pause
    scene scen nega2
    show text "«No somos tan distintos»"
    pause
    scene black
    show text "«¿No?»"
    pause
    hide text

    scene scen nega3
    $ color_mode = "green"
    call set_mode("medio")
    "El gato,{w=0.3} que no parece haber entendido mi duda,{w=0.3} se restriega por mi pierna maullando para que lo acaricie."
    "Le susurro un maullido devuelta{cps=2.0}... {nw}" 
    extend "pero no me responde,{w=0.2} en vez de eso muestra su abdomen,{w=0.2} y yo me agacho para acariciarlo."
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
            call negatio_flores from _call_negatio_flores

        "El puesto de carne":
            call negatio_carne from _call_negatio_carne
    
    jump mapa

label negatio_carne:
    $ gato_comi = True
    $ color_mode = "orange"
    scene scen nega4
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

label luctus_negatio2:
    nvl clear
    $ color_mode= "orange"
    scene scen nega5
    show mar nega1 at right
    show pav nega1 at left
    mar "i have feelings for you"
    pav "i have feelings for you too"
    "the feeling was friendship"
    pav "..."
    "Con el aire de nostalgia que llegó junto a un viejo amigo, los recuerdos llenan mi mente y divago mirando las nubes."
    "Aquella que no llegó a ser mi madre, pero no fue menos, es el centro de mi atención."
    "El té siempre se le olvidaba.{w=0.3} Lo dejaba reposar porque estaba muy caliente, cuando se acordaba ya estaba helado y lo empujaba a un lado como si no fuera culpa suya."
    "{cps=6}Es culpa mía."
    "Imitando un casamiento,{w=0.2} las campanas resuenan haciendo eco en las veredas,{w=0.2} me van a volver loco,{w=0.3} suenan,{cps=24} y suenan,{w=0.25}{cps=36} y suenan,{w=0.2}{cps=48} y suenan,{w=0.15}{cps=60} y suenan,{w=0.1}{cps=72} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan."
    "Me pregunto si habrá amado como aquellos en las bodas." 
    "Hace años dejé de creer en el dios cretino del que tanto me hablaron,{w=0.2} me pregunto{w=0.2} ¿Le habrá rezado?{w=0.2} ¿Se habrá puesto de rodillas ante una ventana y deseado con todas sus fuerzas no morir?"

    "Vivió una vida tan miserable como la mía,{w=0.2} significa entonces{w=0.2} ¿Que moriré también?"
    "No,{w=0.3} no, no, no."
    return
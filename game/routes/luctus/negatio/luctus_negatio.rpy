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
    call set_mode("nadie")

    "El gato me devuelve la mirada, mientras tira de mi unica protección contra los vientos atraidos por la marea y los ojos de los indiscretos atraidos hacia mí, entre mis brazos atenta contra mi paz."

    "Desenredo sus garras de entre los hilos de la tela, con cuidado de no dañar sus fragiles pero dolorosas garras, pensando en si su asalto fue una respuesta negativa a mi divagar o no más que un pequeño jugueteo."

    "A pesar del frío de la tarde que acompaña el pleno otoño, puedo sentir como una calidez comparable con el sol invade mi pecho y se apoya en mis mejillas."

    "Una pregunta surge de entre los maullidos."

    vend "¿Esto es todo?"

    "Con un leve empujón, le obligó a bajar de entre mis brazos y terminar nuestro encuentro de corta duración, en el piso empieza a dar vueltas en si mismo persiguiendo su cola, levemente mareado termina su pequeña pirueta y finalmente se apoya en mi pierna."
    nvl clear

    "¿Cuál es el nombre del gato?"

    "Le quiero preguntar al hombre frente a mí. Abro mi bolso, y busco entre mis cosas un pequeño cuarderno. Arranco una hoja con un mensaje previamente escrito, y lo entrego junto a un par de monedas desgastadas."
    nvl clear

    call set_mode("derecha")
    show rside nega1 at right
    "Gracias."

    "Es lo unico que puedo pronunciar sin mi voz."

    hide rside
    call set_mode("nadie")
    "El hombre mira a su alrededor y me indica con la mano que me acerque. Dudoso, hago caso a su petición y pronto me habla entre susurros."

    vend "No sé si lo notaste ya, pero desde hace un rato que alguien te está siguiendo. Si vas a meterte en problemas, hazlo lejos de mi tienda."

    "Asiento inseguro, y tomo la bolsa del mostrador mientras doy pasos atrás."
    nvl clear

    "Busco entre mi cuarderno la hoja suelta donde tengo anotada mi lista. La tranqulidad con la que habia llegado se fue sin mi."
    
    "LISTA DE COMPRAS ₍^. .^₎\n————————————————————————{fast}{w=0.3}{nw}"
    "— {s}2 Manzanas{/s}{fast}{w=0.3}{nw}"
    "— {s}1kg de harina{/s}{fast}{w=0.3}{nw}"
    "— {s}Huevo{/s}{fast}{w=0.3}{nw}"
    "— {s}Mantequilla{/s}{fast}{w=0.3}{nw}"
    "— {s}2 de pan{/s}{fast}{w=0.3}{nw}"
    "— Ramo de flores{fast}{w=0.3}{nw}"
    "— Carne deshidratada{fast}"
    nvl clear

    "Inhalo profundamente el aire frio y este llena mis pulmones, reemplazando el calor que ahí se alojaba. Con un suspiro exhalo, y me imagino una estela de vapor saliendo por mi boca."

    "Solo dos items quedan desmarcados en esta lista... Carne deshidratada y un ramo de flores."

    "Miro dudoso el cielo nublado, en este horario la luz duerme más temprano y con su soñar llega la pesadilla de los vivos. Pretendo irme antes de las seis, pero observando el reloj del mercado encuentro imposible esa posibilidad a menos deje alguna de estas cosas pendientes para la semana."

    "Miro una ultima vez la lista, y mis piernas me llevan a..."

    menu:
        "El puesto de flores":
            call negatio_flores

        "El puesto de carne":
            call negatio_carne
    
    jump luctus_negatio2

label negatio_carne:
    $ gato_comi = True
    $ color_mode = "orange"
    scene scen nega4
    extend " el puesto de carne."
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
    extend " el puesto de flores."
    return
    

    #Pavel va al puesto de flores y pregunta por el precio, viendo que ya se hizo tarde se resigna y compra las flores, prometiendo para si mismo comprarlas otro dia.

label luctus_negatio2:
    nvl clear
    $ color_mode= "orange"
    call set_mode("medio")
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
    jump mapa

label luctus_negatio3:
    nvl clear
    mar "dale pavel no seas putin"
    pav "muerete xdxdxd"    
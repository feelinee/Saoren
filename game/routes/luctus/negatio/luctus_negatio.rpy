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

    play ambience1 "ambiente/seawaves.mp3"  loop fadein 8.0 volume 0.5
    play ambience2 "ambiente/market.mp3"  loop fadein 8.0  volume 0.1
    play ambience3 "ambiente/wind.mp3"  loop fadein 8.0 volume 0.2

    "El gatito entre mis brazos maulla juguetón. Ignorante de las divagaciones silenciosas que persiguen mi mente, tira de mi capucha, unico refugio frente a los vientos de la tarde atraidos por la marea. Las lámparas recién encendidas por los lamperos parpadean a punto de apagarse, y a pesar de que el sol aún besa la mar, durante un instante el mundo se oscurese un poco, dandome un breve momento para descansar de los ojos indiscretos de la escaza multitud."

    "Desenredo sus uñas de entre los hilos de la tela con cuidado de no dañar sus fragiles pero dolorosas garras.{w=0.3} El pequeño responde con un par maullidos y a pesar del frío de la tarde que acompaña el pleno otoño,{w=0.2} puedo sentir como una calidez comparable con la del sol invade mi pecho y se apoya en mis mejillas."

    "Interrumpiendo el romper de las olas, una pregunta surge de entre los maúllos."

    vend "¿Esto es todo?"

    "Como un recordatorio de donde estoy parado, el sonido apagado de la multitud invade mis orejas nuevamente."

    $ renpy.music.set_volume(0.3, channel="ambience2")
    
    extend " Con un leve empujón, obligo a bajar de entre mis brazos al gato para terminar nuestro encuentro de corta duración. En el piso empieza a dar vueltas en si mismo persiguiendo su cola. Entretenido miro como termina su pequeña pirueta levemente mareado y finalmente se apoya en mi pierna, acompañandome un rato más."
    nvl clear

    "¿Cuál es su nombre?"

    "Le quiero preguntar al hombre. Abro mi bolso, y busco entre mis cosas un pequeño cuarderno. Arranco una hoja con un mensaje previamente escrito, y lo entrego junto a un par de monedas desgastadas."
    nvl clear

    call set_mode("derecha")
    show rside nega1 at right
    pav "\"Gracias.\""

    "Es lo unico que puedo pronunciar sin mi voz."

    hide rside
    call set_mode("nadie")
    "El hombre mira a su alrededor y me indica con la mano que me acerque. Dudoso, hago caso a su petición y pronto me habla entre susurros."

    vend "No sé si lo notaste."
    vend "No me importa realmente."
    vend "Pero desde hace un rato que alguien te está siguiendo."
    vend "Si vas a meterte en problemas, hazlo lejos de mi tienda."
    vend "Espantas a los clientes."

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

    "Inhalo profundamente el aire frio y este llena mis pulmones, reemplazando el calor que ahí se alojaba. Con un suspiro exhalo, y me imagino una estela de vapor saliendo por mi boca. {w}Solo dos items quedan desmarcados en esta lista, carne deshidratada y un ramo de flores."

    "Miro dudoso el cielo nublado, en este horario la luz duerme más temprano y con su soñar llega la pesadilla de los vivos. Pretendo irme antes de las seis, pero observando el reloj del mercado encuentro imposible esa posibilidad a menos deje alguna de estas cosas pendientes para la semana."

    "Miro una ultima vez la lista, y mis piernas me llevan a..."

    menu:
        "El puesto de flores":
            call negatio_flores

        "La carniceria":
            call negatio_carne
    
    jump luctus_negatio2

label negatio_carne:
    $ gato_comi = True
    extend " la carniceria."
    nvl clear

    "Con los ultimos rayos de sol de la tarde y una inceridumbre ominosa acompañandome, tomo una descisión rapido y me dirigo al puesto de carne a pocos metros de mi."
    
    $ color_mode = "orange"
    scene scen nega5

    "Me tapo la cara con la bufanda cuando empieza a invadir en el ambiente un olor crudo que me hace revolver el estomago. La sangre esparcida en el mostrador ensucia el precio que indica el valor de los cadaveres de los animales que se encuentran a su lado y me tengo que aguantar las ganas de vomitar."

    "Los ojos de las cabezas colgadas miran hacia el piso, y en una fantasia grotesca imagino como desean recuperar su cuerpo y volver a su libertad. Salir corriendo en esas calles que miran con tanta atención."

    "Pero se quedan colgados, y los comparo conmigo."
    
    "La unica desemejanza que puedo encontrar es que aún estoy respirando. {w}E incluso así, estos hombres puden elegir si quitarme eso también."

    vend "¿Vas a comprar algo o te vas a quedar ahí?"
    
    "No me siento como nada más que ganado cuando me miran a los ojos, con la incapacidad de detener su homicidio y ponerle un precio a mis tripas."
    nvl clear

    "Ojeo lo que hay y apunto a uno de los conejos con cuello cortado, el más blanco, el que hace contrastar más la sangre en su pelo. Lanzo las monedas en el mostrador, ensuciandolas también de pecado. El carnicero las toma silencioso antes de dirigirse a otra persona."

    "Agarro el animal por sus orejas, con la carne entre las manos me siento un poco más como un humano, puedo controlar el cuerpo inerte de esta criatura como ellos pueden controlar el mio. Siento comezón por todo el cuerpo, las miradas de mi cabeza me ponen en un tribunal moral que sé que no puedo ganar. Me doy la vuelta, y la mirada de ese hombre alto entre la multitud se encuentra con la mia."

    "Intento negar el hecho, una coincidiencia probable entre un mar de ojos, pero mientras la luna sube a su trono, la figura del hombre se acerca. Mis piernas me piden correr, pero como siempre son sordas ante sus propias suplicas."

    "Con pasos temblorosos camino en dirección contraria, dandole la espalda. Quizás si me entierra un cuchillo por detrás, me dolerá más la conmoción que el corte."
    nvl clear

    stop ambience1
    stop ambience2
    stop ambience3
    $ color_mode = "green"
    scene scen nega6

    "Subo las escaleras. Ya no sé donde me llevan los pies, quizás a rezar de rodillas clemencia para mi insignificante vida pues, frente a mi, veo ergirse la alta capilla. En la sima de esta pequeña subida, mirando hacia abajo, veo a todas esas personas dando vueltas tontamente sin dirigir su mirada hacia mi."
    
    "Me pregunto si asi se sentira ser un dios olvidado."

    "Entre las siluteas que miro, la de aquel hombre no se asoma y respiro tranquilo. Pretendo volver a mi hogar, cuando las palomas retoman su vuelo,"

    window hide
    scene black
    play audio "audio/efectos/birdsflap.mp3"
    pause  2.0
    $ color_mode = "orange"
    scene scen nega4 with dissolve
    pause 1.0

    extend " una mano aprieta con fuerza mi muñeca."

    return

    ##idea:

    #Pavel llega al puesto de carne y compra, nota por el rabillo del ojo a la persona que lo está siguiendo, es bastante alto y aunque no parece tner mucha masa muscular, es suficiente para intimidarlo, decide meterse entre la muchedumbre.

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
    #mar "cómo que se murio??"
    #pav "..."
    #"no puedo hablar amigo q te pasa"
    #mar "sos re puto"
    #"*marcille se va en re puto*"
    #"miro la tumba"
    #"Con el aire de nostalgia que llegó junto a un viejo amigo, los recuerdos llenan mi mente y divago mirando las nubes."
    #"Aquella que no llegó a ser mi madre, pero no fue menos, es el centro de mi atención."
    #"El té siempre se le olvidaba.{w=0.3} Lo dejaba reposar porque estaba muy caliente, cuando se acordaba ya estaba helado y lo empujaba a un lado como si no fuera culpa suya."
    #"{cps=6}Es culpa mía."
    #"Imitando un casamiento,{w=0.2} las campanas resuenan haciendo eco en las veredas,{w=0.2} me van a volver loco,{w=0.3} suenan,{cps=24} y suenan,{w=0.25}{cps=36} y suenan,{w=0.2}{cps=48} y suenan,{w=0.15}{cps=60} y suenan,{w=0.1}{cps=72} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan."
    #"Me pregunto si habrá amado como aquellos en las bodas." 
    #"Hace años dejé de creer en el dios cretino del que tanto me hablaron,{w=0.2} me pregunto{w=0.2} ¿Le habrá rezado?{w=0.2} ¿Se habrá puesto de rodillas ante una ventana y deseado con todas sus fuerzas no morir?"
    #pav "Perdón..."
    #pav "Pero si no puedo vivir así"
    #pav "No puedo vivir en absoluto"
    #pav "Perdón"
    #pav "De verdad" 
    #pav "Perdón"
    jump mapa

label luctus_negatio3:
    nvl clear
    #mar "dale pavel no seas putin"
    #pav "muerete xdxdxd"    
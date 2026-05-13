define pav = Character("PAVEL", color="#e4dbb2")
define ana = Character("ANARAITH", color="#e4dbb2")
define mar = Character("MARCILLE", color="#e4dbb2")
define asf = Character("ASFÓDEL", color="#e4dbb2")
define qn = Character("???", color="#e4dbb2")

#Pavel Sprites

image Pavel neutral:
    "images/Pjs/Pavel Prologo Sprites/pavelnormal.png"
    zoom 0.30
image Pavel triste:
    "images/Pjs/Pavel Prologo Sprites/paveltriste.png"
    zoom 0.30
image Pavel enojado:
    "images/Pjs/Pavel Prologo Sprites/pavelenojado.png"
    zoom 0.30
image Pavel dudoso:
    "images/Pjs/Pavel Prologo Sprites/paveldudoso.png"
    zoom 0.30
image Pavel anaraith:
    "images/Pjs/Pavel Prologo Sprites/pavelanaraith.png"
    zoom 0.30
image Pavel anaraith2:
    "images/Pjs/Pavel Prologo Sprites/pavelanaraith2.png"
    zoom 0.30

#Fondos

image Bosque: 
    "images/Fondos/bgbosque.png"
    zoom 0.95 yalign 0.05
image Pieza:
    "images/Fondos/bgpieza.jpg"
    zoom 1.80

label start:

    ##Escena 1:
    scene black
    show Bosque zorder 0
    play music "audio/bgbosque.mp3" loop fadein 1.0 volume 1
    "Los árboles hablan."
    "Cuando llega la noche y las almas se duermen, {w=0.3}en el silencio que invade el bosque." 
    "El viento se convierte en su voz y el psiturismo en sus palabras."
    "Los testigos de la oscuridad guardan con reticencia la inefable verdad." 
    "Escapando de la mirada humana, escondiéndose entre las ramas de los secretistas con temor."
    "La razón de tal miedo..."
    "La leí una vez hace mucho tiempo." 
    "Escondido en la esquina menos apreciada, con los ojos entrecerrados tratando de distinguir las letras de un libro descolorido y polvoriento."

    hide Bosque zorder 0
    "\"Cuando dios caminaba por esta tierra escondido entre los hombres humildes, se cuenta una tragedia.\""
    "\"La fauna aquella, cautivada por el creador, pidio con misericordia\"" 
    "\"«Oh Dios mío por favor, por tu divinidad concederme este deseo..."
    extend " Me he enamorado de una mujer, en mi desespero, yo entiendo sus palabras, más ella no las mías y no me da más que un cabeceo.»\""
    "\"En su compasión Dios le respondió\"" 
    "\"«Te otorgare el don del habla para que hábites entre mis hijos." 
    extend " No obstante, no puedo confiar en la integridad de tus palabras.»\""

    "\"A cambio de su anhelo, Dios solo tuvo una petición, se agachó y le susurró.\""
    "\"Levantó el cuerpo e imponente pronunció «Como demostración de tu lealtad, juraras nunca revelar este secreto»\""
    "\"Y en un disfraz el devoto partió, su deseo se cumplió, y por años una vida de felicidad llevó. Con la dama de su sueños se casó y un hijo engendró.\""
    play sound "audio/soundrain.mp3" loop volume 0.5
    "\"«Oh amor mio...» empezó, en una noche lluviosa a la luz de las velas.\""
    "\"«Tenemos un lazo eterno, pero traigo un peso en mi corazón.»\""
    "\"«Comparte tu tristeza» Le respondió, y el animal asintió.\""
    "\"«Esta es mi confesión, yo te amo desde antes de que tu me amaras a mí. Tu sonrisa es mi razón de existir, porque dios me concedió el deseo de a tu lado sonreír.»\""
    "\"«A cambió de está bendición me pidió que su secreto guardara con discreción, pero el pecho me aprieta al pensar en mentirte, corazón»\""
    "\"«Así que lo diré, confío en ti y en que junto a mí a la tumba te lo llevarás. En realidad... »\""
    stop music
    "\"«☐☐☐☐ ☐☐☐☐ ☐☐☐☐☐☐ ☐ ☐☐☐☐☐☐☐☐ ☐☐ ☐☐☐☐☐☐☐»\""
    stop sound fadeout 1.0

    "\"La mayor de las bendiciones puede ser la peor de las maldiciones.\"" 
    "\"Es mejor vivir ansiando humildemente antes de ser consumido en la avaricia.\""
    "\"Como ese maldito animal, condenado al silencio y el exilio. Perderas todo y morirás anhelando lo que tuviste.\""  
    "\"Los hijos de las bestias traicioneras portan la cara de sus padres. Algunos sus orejas, cola o escamas, Dios lo hizo para que no seamos engañados.\""
    "\"Sin embargo hasta las bestias tienen el perdón de Dios, las criaturas que se esconden en el bosque perdieron su derecho a hablar y estar entre la gente.\"" 
    "\"Pero los engendros de dos patas que tienen sangre noble y pura en ellos serán otorgados de una segunda oportunidad para servir al señor y limpiar su sangre sucia.\""

    show Bosque zorder 0
    "Puedo escuchar a los árboles hablar."
    "Pero no escucho sus poesías,{w=0.3} más bien, sus risas rechinan como una cama vieja y desgastada." 
    "Los golpeteos de las ramas suenan como los pasos de la oscuridad que me sigue detrás."
    "En la frondosidad del bosque, no soy más que otro ser de sangre sucia escondiendose como una presa."
    "El rastro bajo mis pies continua hacia delante, las marcas de las suelas de un par zapatos desgastados están enterradas profundas en la nieve."
    "Las sigo, {w=0.3}mientras los copos empiezan a caer como lluvia hirviendo en mi cuerpo,{w=0.3} mientras me congelo de adentro hacia afuera." 

    "Duele."

    "Los animales se acercan y aún escondidos me observan." 
    "Seguro han de pensar..." 
    "¿Un humano? ¿Aquí?"
    "No." 
    "Es una bestia."
    "Tampoco es una bestia, es..."
    "\"Asqueroso.\""
    "Los árboles dejan de reirse, y empiezan a susurrar entre ellos." 
    "\"Un animal de dos patas.\"" 
    "\"Es una deformidad.\""
    "\"Deberia morirse, sufriria menos.\""
    "Saben que no voy a decir nada, {w=0.3}que no puedo decir nada. "
    "Porque al igual que una bestia traicionera {w=0.3}estoy maldito, {w=0.3}y mi boca no vale nada."
    "Así que se burlan de mí." 
    "De una rama cae un montículo de nieve, {w=0.3}y otro, {w=0.3}y otro." 
    "Como niños luego de la primera nevada, lanzan pedazos buscando mi atención."
    "\"Oye.\""
    "Una de las ramas se inclina, {w=0.3}crujiendo."
    "\"¿Por qué sigues pisandolas?\""
    "La pregunta cae de los árboles como la nieve."
    "Abro mi boca, pero no sale nada."
    "Solo un sonido ahogado y patetico."
    "Los árboles explotan en carcajadas."
    "Dejo caer las retoricas infantiles sobre mi cuerpo mientras avanzo."
    "Las huellas en el piso parecen dar giros incomodos, hasta que se paran y dan la vuelta."
    "Aunque pronto vuelven en si mismas, y yo las sigo."
    "Las risas empiezan a apagarse, los arboles empiezan a separarse más uno de los otros hasta que el bosque se convierte en un claro."
    "Pero el camino sigue adelante y yo avanzo junto a él, {w=0.3}contrastando con el resto del escenario, {w=0.3}en medio de todo me encuentro con un macizo de flores."
    "Un campo de Asfodelos teñidos de rojo, con cenizas esparcidas en sus petalos como lo harian gotas de agua."
    "Alrededor suyo no hay nada."
    extend " El camino termina ahí."
    "Puedo ver la salida desde donde estoy, la nieve blanca y nueva me llama a acercame y poner mi marca."
    "{size=+20}{cps=2}. . .{w=0.5}{nw}"
    "Me doy la vuelta."
    "Hacia ese sendero de pisadas superpuestas y borrosas por la nieve que ya cayó."
    ""


    ##Escena 2 (mover a cap 1):
    "Me despierto con los ojos cerrados, un frio punzante me eriza la piel."
    show Pavel neutral at right
    mar "Pavel, vamos, tienes que despertar. "
    show Pavel neutral at left
    pavel "Mmmm okay."
    show Pavel enojado at right
    mar "¿porqué tenemos el mismo sprite..?"
    show Pavel dudoso at left
    pav "qué."
    "Sin querer seguir su destino me sujeté fuerte de la pared con una mano."
    mar"Abre los ojos, dios."
    "Y los abrí, pero no habia ningún dios" 
    extend ", o al menos yo no lo ví."
    "La oscuridad de la habitación se me hacia ver tanto como veia cuando los tenia cerrados."
    "Así que los cerré." 
    pav "pico pal que lee xdxdxdxd"
    show Pavel neutral at right
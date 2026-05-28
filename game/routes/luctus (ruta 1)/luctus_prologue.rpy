label luctus_prologue:
    scene bg bosque
    $ color_mode = "orange"
    call mode_izquierda
    play music bgbosque fadein 1 volume 1
    window show
    "Cuando llega la noche y las almas se duermen, los árboles hablan en el silencio que invade el bosque. {w}El viento se convierte en su voz y el psiturismo en sus palabras."
    "Los testigos de la oscuridad guardan con reticencia la inefable verdad. {w}Escapando de la mirada humana, escondiéndose entre las ramas de los secretistas con temor."
    "La razón de tal miedo... {w}La leí una vez hace mucho tiempo. {w}Escondido en la esquina menos apreciada{w=0.3}, con los ojos entrecerrados tratando de distinguir las letras de un libro descolorido y polvoriento."
    nvl clear

    scene bg cuento
    $ color_mode = "blue"
    call mode_derecha
    "En los dias en que Dios caminaba por esta tierra, cuando el polvo del camino manchaba sus sandalias como las de cualquier mortal, se cuenta una tragedias que pocos se atreven a replicar y contar." 
    "La fauna aquella, criatura fiel entre las criaturas, lo contempló desde la maleza. En su pecho{w=0.3}, escondia algo que ninguna bestia había sentido antes."
    "Amor {w}por una hija de hombre, una mujer de voz suave y manos callosas que olían a tierra mojada."
    "Se postró ante los pies de su divinidad y rogó." 
    "—Oh Señor mío... {w=0.3}por tu divinidad y tu misericordia, concédeme este deseo. {w}Me he enamorado de una mujer. Yo entiendo cada una de sus palabras, más ella no entiende las mías. Soy invisible a sus ojos."
    "Y Dios, que conoce el peso de todos los corazones, en compasión se detuvo a comprender."
    nvl clear
    play sound pageturn volume 2.0

    "—Te otorgaré el don del habla, para que habites entre mis hijos como uno más.{w} No obstante, eres de otra naturaleza, y la naturaleza desconoce la integridad de las palabras."
    "Entonces se agachó lentamente y le susurró a la oreja. Con el crujir de los arboles y el silencio de las rocas acompañandolos como unicos atestiguantes."
    "Cuando se enderezó, su voz resonó con la gravedad de las cosas eternas" 
    "—Este pacto es el precio de tu voz. Como demostración de tu lealtad, jurarás nunca revelar este secreto. Ni a la tierra, ni al agua, ni al ser que más ames."
    "Y la bestia juró, y partió disfrazada de hombre, cargando un nuevo rostro y una promesa consigo."
    nvl clear
    play sound pageturn volume 2.0

    "Las hojas calleron al piso, secas y de un color naranjo caracteristico. Las estaciones habian pasado, asi como lo habian hecho los años. El rio cambio su flujo y la criatura su destino, entre sus brazos tenia una bendición de los cielos un niño con su sangre y la cara de su amada."
    play sound soundrain loop volume 1.0
    $ renpy.music.set_volume(0.1, channel="sound")
    "En una noche de lluvia, con las velas casi consumidas y el sonido del agua golpeando el techo de barro, él tomó la mano de su esposa y comenzó a hablar despacio, con el sosiego de un pecador en un confesionario."
    "—Oh amor mío... Tenemos un lazo eterno, pero traigo un peso en el corazón que ya no puedo sostener solo."
    "—Comparte tu tristeza —le respondió ella, sin soltar su mano."
    "La lluvia arrecia al otro lado de la ventana, él asintió, mirando la llama reflejada en el cristal."
    nvl clear
    play sound pageturn volume 2.0
    
    "—Esta es mi confesión. Yo te amé desde antes de que tú me amaras a mí. Antes de que supieras mi nombre, antes de que yo tuviera uno. Tu sonrisa es mi razón de existir, porque Dios mismo me concedió el deseo de estar a tu lado."
    "—A cambio de esa bendición, me pidió que guardara su secreto con discreción. Y lo he guardado. Años he cargado ese silencio como una piedra en el pecho. Pero mentirte a ti se me hace más pesado aún."
    "La vela parpadeó."
    "—Así que lo diré. Confío en ti, y en que junto a mí, a la tumba te lo llevarás."
    "Sus ojos se encontraron con los de ella en la penumbra, y él abrió la boca para pronunciar lo que {color=#f00}nunca debía ser pronunciado.{/color}"
    stop music
    call seq_prólcensura
    nvl clear
    play sound pageturn volume 2.0

    "Dicen los sabios que la mayor de las bendiciones puede convertirse en la peor de las maldiciones. Que es mejor vivir con el deseo humilde en el pecho que ser devorado por la avaricia de querer más de lo que corresponde." 
    "Tal como ese maldito animal. Condenado al silencio y al exilio, que perdió todo cuanto había amado, y murió anhelando lo que una vez tuvo entre las manos."  
    "Los hijos de las bestias traicioneras portan la cara de sus padres. Algunos heredan sus orejas, otros su cola, otros las escamas que los delatan bajo la ropa. Dios lo dispuso así para que su pueblo no fuera traicionado, como lo habian traicionado a él."
    nvl clear
    play sound pageturn volume 2.0

    "Con todo, hasta las bestias están al alcance de la misericordia de Dios, las criaturas que se refugiaron en los bosques perdieron su derecho a hablar y a caminar entre la gente, y en ese destierro cargan su culpa." 
    "Pero los engendros de dos patas que llevan sangre noble en sus venas recibirán una segunda oportunidad, una última puerta, la de servir al Señor y lavar con sudor y obediencia lo que la sangre de sus padres manchó."
    nvl clear
    play sound pageturn volume 2.0

    window hide None
    scene black
    pause 0.5
    window show None

    call mode_izquierda
    $ color_mode = "orange"
    scene bg bosque      
    show side arboles:
        xalign 0.0 yalign 1.0
    "Puedo escuchar a los árboles hablar."
    "Pero no escucho sus poesías,{w=0.3} sus risas rechinan como una cama vieja y desgastada, y los golpeteos de las ramas caen acompasados, como los pasos de la oscuridad que me persigue detrás. En la frondosidad del bosque, la nieve se queda suspendida entre las ramas sin llegar al suelo."
    show side pisadas at left:
        yalign 0.0
        linear 40.0 yalign 1.0
    nvl clear

    "El rastro bajo mis pies continua hacia delante, las marcas de las suelas de un par de zapatos desgastados están enterradas profundas en la nieve, impresas con \nuna firmeza que me resulta ajena. {w}Las sigo, {w=0.3}mientras \nlos copos empiezan a caer como {cps=50}lluvia {cps=100}hirviendo{nw}"
    $ _history = False
    show anaraith1 at left:
        yalign 0.0
    extend "oooooo{cps=200}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=300}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=400}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=500}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=600}\noooooooooooooooooooooooooooooooooooooooooooooooooooo\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=700}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=800}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=900}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=1000}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=1100}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{nw}"
    hide anaraith1
    scene bg bosque
    show side pisadas at left:
        linear 100.0 yalign 1.0    
    nvl clear #ARREGLE EL FLICKERING SOY LA PUTA CABRA

    "El rastro bajo mis pies continua hacia delante, las marcas de las suelas de un par de zapatos desgastados están enterradas profundas en la nieve, impresas con una firmeza que me resulta ajena. Las sigo, mientras los copos empiezan a caer como lluvia hirviendo{fast} en mi cuerpo,{w=0.3} mientras me congelo de adentro hacia afuera."
    $ _history = True
    "Duele."
    nvl clear

    "Desde las sombras de entre los troncos los animales se acercan, puedo sentir su mirada y de reojo veo como inclinan su cabeza con curiosidad mórbida. Una criatura con sangre de cazador y piel de presa." 
    "¿O es al revés?" 
    show side arboles at left:
        yalign 1.0
        linear 40.0 yalign 0.0  
    "Los árboles dejan de reirse ante las frases silenciosas de los animales, y empiezan a susurrar entre ellos."       
    "Saben que no voy diré nada, {w=0.3}que no puedo decir nada. {w}Porque al igual que una bestia traicionera {w=0.3}estoy maldito con una boca inservible."

    $ _history = False
    "De una rama cae un montículo de nieve,\n{nw}"
    extend "{alpha=0.0}De una rama cae un montículo de nieve,{fast}{/alpha} {w=0.3}y otro\n{nw}"
    extend "{alpha=0.0}De una rama cae un montículo de nieve, y otro,{fast}{/alpha}{w=0.3}y otro."
    $ _history = True
    $ if _history_list: _history_list[-1].what = "De una rama cae un montículo de nieve, y otro, y otro."
    "Como niños luego de la primera nevada, la lanzan buscando mi atención."
    nvl clear

    "—Oye."
    "Una de las ramas se inclina, {w=0.3}crujiendo."
    "—¿Por qué sigues pisandolas?"
    "Abro mi boca, pero no sale más que un sonido ahogado y patetico. Sujeto mi garganta con ambas manos, intentando calmar el ardor. {w}Los árboles explotan en carcajadas."
    "Dejo caer las retoricas infantiles sobre mi cuerpo mientras avanzo. Las huellas en el piso parecen dar giros incomodos, hasta que se paran y dan la vuelta."
    "Aunque pronto vuelven en si mismas, y yo las sigo."
    "Las risas empiezan a apagarse, los arboles empiezan a separarse más uno de los otros hasta que el bosque se convierte en un claro."
    "Pero el camino sigue adelante y yo avanzo junto a él, {w=0.3}contrastando con el resto del escenario, {w=0.3}en medio de todo me encuentro con un macizo de flores."
    show side flores at left:
        xalign 0.0 yalign 0.0   
    "Un campo de Asfodelos teñidos de rojo, con cenizas esparcidas en sus petalos como lo harian gotas de agua."   
    "Alrededor suyo no hay nada, el camino termina ahí."          
    nvl clear

    "Puedo ver la salida desde donde estoy, la nieve blanca y nueva me llama a acercame y poner mi marca."

    call seq_prólpav1

    "{size=+20}{cps=3}. . .{nw}"
    "{cps=25}Me doy la vuelta."
    "Hacia ese sendero de pisadas superpuestas, borrosas por la nieve que ya cayó."

    label luctus_final:
    $ persistent.luctus_compl = True   

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

##Notas que ns donde más poner:
#Para cgs esconder la ventana, mostrar la imagen y luego cambiar el tipo de ventana a cg (más ADV like)
label luctus_prologue:

    scene scen mors7
    $color_mode= "orange"
    call set_mode("nadie")
    play music bgbosque fadein 1
    window show
    "Cuando llega la noche y las almas se duermen, los árboles hablan en el silencio que invade el bosque. {w}\nEl viento se convierte en su voz y el psiturismo en sus palabras."
    "Los testigos de la oscuridad guardan con reticencia la inefable verdad. {w}Escapando de la mirada humana, escondiéndose entre las ramas de los secretistas con temor."
    "La razón de tal miedo... \n\n{w}La leí una vez hace mucho tiempo. {w}Escondido en la esquina menos apreciada{w=0.2}, con los ojos entrecerrados tratando de distinguir las letras de un libro descolorido y polvoriento."
    nvl clear

    scene scen mors8
    show rside mors6 at right
    $ color_mode = "blue"
    call set_mode("derecha")
    "En los dias en que Dios caminaba por esta tierra,{w=0.2} cuando el polvo del camino manchaba sus sandalias como las de cualquier mortal,{w=0.2} se habla una tragedia que pocos se atreven a contar." 
    "La fauna aquella,{w=0.2} criatura fiel entre las criaturas,{w=0.2} lo contemplaba desde la maleza.{w=0.2} En su pecho,{w=0.2} escondia algo que ninguna bestia había sentido antes."
    "Amor{w}, por una hija de hombre,{w=0.2} una mujer de voz suave y manos callosas que olían a tierra mojada."
    "Desesperado se postró ante los pies de su divinidad y rogó." 
    nvl clear

    fau "Oh Señor mío... {w=0.2}por tu divinidad y tu misericordia, concédeme este deseo." 
    fau "Me he enamorado de una mujer."
    fau "Yo entiendo cada una de sus palabras, más ella no entiende las mías.{w=0.2} Soy invisible a sus ojos."
    "Y Dios, que conoce el peso de todos los corazones, en compasión se detuvo a comprender."
    nvl clear
    play audio pageturn volume 1

    dios "Te otorgaré el don del habla, para que habites\nentre mis hijos como uno más."
    
    dios "No obstante, eres de otra naturaleza, y la \nnaturaleza desconoce la integridad de las\npalabras."
    "Con el crujir de los arboles y el silencio de las rocas acompañandolos como unicos atestiguantes, el señor se agachó lentamente y le susurró a la oreja."
    "Cuando se enderezó, su voz resonó con la gravedad de las cosas eternas." 
    dios "Este pacto es el precio de tu voz. Como demostración de tu lealtad, jurarás nunca revelar este secreto. Ni a la tierra, ni al agua, ni al ser que más amas."
    "Y la bestia juró, partiendo disfrazada de hombre, cargando un nuevo rostro y una promesa consigo."
    nvl clear
    play audio pageturn volume 1

    "Las hojas cayeron al piso,{w=0.2} secas y de un color naranjo caracteristico.{w=0.2} Las estaciones habian pasado,{w=0.2} asi como lo habian hecho los años.{w=0.2} El rio cambio su flujo{w=0.1} y la criatura su destino,{w=0.2} entre sus brazos tenia una bendición de los cielos, un niño con su sangre y una cara semejante a la de su amada."
    play sound soundrain loop volume 1.0
    $ renpy.music.set_volume(0.1, channel="sound")
    "En una noche de lluvia, con las velas casi consumidas y el sonido del agua golpeando el techo de barro, él tomó la mano de su esposa y comenzó a hablar despacio, con el sosiego de un pecador en un confesionario."
    fau "Oh amor mío...{w=0.2} Tenemos un lazo eterno, pero traigo un peso en el corazón que ya no puedo sostener solo."
    muj"Comparte tu tristeza" 
    "Le respondió ella, sin soltar su mano."
    "La lluvia arrecia al otro lado de la ventana, él asintió, mirando la llama reflejada en el cristal."
    nvl clear
    play audio pageturn volume 1
     
    fau "Esta es mi confesión,{w=0.2} yo te amé desde antes de que tú me amaras a mí.{w=0.2} Antes de que supieras mi nombre,{w=0.2} antes de que yo tuviera uno.{w=0.2} Tu sonrisa es mi razón de existir,{w=0.2} porque Dios mismo me concedió el deseo de estar a tu lado."
    fau "A cambio de esa bendición,{w=0.2} me pidió que guardara su secreto.{w=0.2} Y lo he guardado.{w=0.2} Años he cargado ese silencio como una piedra en el pecho.{w=0.2} Pero mentirte a ti se me hace más pesado aún."
    "La vela parpadeó."
    fau "Así que lo diré.{w=0.2} Confío en ti, y en que junto a mí, a la tumba te lo llevarás."
    "Sus ojos se encontraron con los de ella en la penumbra,{w=0.2} y él abrió la boca para pronunciar lo que {color=#f00}nunca debía ser pronunciado.{/color}"
    nvl clear
    play audio pageturn volume 1
    stop music
    
    $ _history = False
    $ renpy.music.set_volume(0.2, channel="sound")
    fau "{cps=50}DIOS ES** *UE*** * *O**TR** L* ***AM**{nw} "
    $ renpy.music.set_volume(0.3, channel="sound")
    fau "{cps=100}DI** **T* ****T* Y **S***O* ** M*****S{nw} "
    $ renpy.music.set_volume(0.4, channel="sound")
    fau "{cps=150}*I*S **TA M***** * N******S *O *******{nw} "
    $ renpy.music.set_volume(0.5, channel="sound")
    fau "{cps=200}**OS **** **R*** * ******** ** *******{nw} "
    $ renpy.music.set_volume(0.6, channel="sound")
    fau "{cps=250}***S **** ****O * ***O**** ** **T****{nw} "
    $ renpy.music.set_volume(0.7, channel="sound")
    fau "{cps=300}**** *S** ****** * ******** ** *A***O*{nw} "
    $ renpy.music.set_volume(0.8, channel="sound")
    fau "{cps=350}**** **** ****** * ******** ** *******{nw} "
    $ renpy.music.set_volume(0.9, channel="sound")
    fau "{cps=450}**** **** ****** * ******** ** *******{nw} "
    $ renpy.music.set_volume(1.0, channel="sound")
    fau "{cps=500}**** **** ****** * ******** ** *******{nw} "
    $ _history = True
    $ if _history_list: _history_list[-1].what = "La curiosidad mató al gato, y te matara a ti."
    stop sound
    $ renpy.music.set_volume(1.0, channel="sound")
    nvl clear
    play audio pageturn volume 1

    "Dicen los sabios que la mayor de las bendiciones puede convertirse en la peor de las maldiciones.\n\n{w}Que es mejor vivir con el deseo humilde en el pecho que ser devorado por la avaricia de querer más de lo que corresponde." 
    "Tal como ese maldito animal.{w=0.2} Condenado al silencio y al exilio,{w=0.1} que perdió todo cuanto había amado, y murió anhelando lo que una vez tuvo entre las manos."  
    "Los hijos de las bestias traicioneras portan la cara de sus padres. Algunos heredan sus orejas, otros su cola, otros las escamas que los delatan bajo la ropa. Dios lo dispuso así para que su pueblo no fuera engañado, como lo habian engañado a él."
    nvl clear
    play audio pageturn volume 1

    "Incluso así, hasta las bestias están al alcance de la misericordia de Dios,{w=0.2} las criaturas que se refugiaron en los bosques perdieron su derecho a hablar y a caminar entre la gente,{w=0.2} y en ese destierro cargan su culpa." 
    "Pero los engendros de dos patas que llevan sangre noble en sus venas recibirán una segunda oportunidad, una última puerta, la de servir al señor y lavar con sudor y obediencia lo que la sangre de sus padres manchó."
    nvl clear
    play audio pageturn volume 1
    
    
    nvl hide
    hide rside with None
    scene black with None

    pause 1

    call set_mode("izquierda")
    $ color_mode = "orange"
    scene scen mors7     
    show lside mors4:
        xalign 0.0 yalign 1.0
    "Puedo escuchar a los árboles hablar."
    "Pero no escucho sus poesías,{w=0.2} en su lugar resuenan risas que rechinan como una cama vieja y desgastada,{w=0.2} y los golpeteos de las ramas que caen acompasados,{w=0.2} como los pasos de la oscuridad que me persigue detrás."
    "En la frondosidad del bosque, la nieve se queda suspendida entre las ramas sin llegar al suelo."
    show lside mors2 at left:
        yalign 0.0
        linear 40.0 yalign 1.0
    nvl clear

    "El rastro bajo mis pies continua hacia delante,{w=0.2} las marcas de las suelas de un par de zapatos desgastados están enterradas profundas en la nieve,{w=0.2} impresas con \nuna firmeza que me resulta ajena."
    play ambience1 "audio/efectos/pisadasnieve.mp3"
    extend "   \n\nLas sigo, {w=0.2}mientras los copos empiezan a caer como\nlluvia hirviendo"
    stop ambience1
    $ _history = False
    show lside mors3 at left:
        yalign 0.0
    extend "{cps=100}oooooooooooooooooooooooooooooooooooo{cps=200}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=300}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=400}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=500}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=600}\noooooooooooooooooooooooooooooooooooooooooooooooooooo\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=700}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=800}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=900}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=1000}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{cps=1100}\noooooooooooooooooooooooooooooooooooooooooooooooooooo{nw}"
    scene scen mors7
    show lside mors2 at left:
        linear 100.0 yalign 1.0    
    nvl clear #ARREGLE EL FLICKERING SOY LA PUTA CABRA

    "El rastro bajo mis pies continua hacia delante, las marcas de las suelas de un par de zapatos desgastados están enterradas profundas en la nieve, impresas con una firmeza que me resulta ajena. \n\nLas sigo, mientras los copos empiezan a caer como lluvia hirviendo{fast} en mi cuerpo,{w=0.2} mientras me congelo de adentro hacia afuera."
    $ _history = True
    "Duele."
    nvl clear

    "Desde las sombras de entre los troncos los animales se acercan,{w=0.2} puedo sentir su mirada y de reojo veo como inclinan su cabeza con curiosidad mórbida.{w=0.2} Una criatura con sangre de cazador y piel de presa." 
    "{cps=1.5}... {cps=12}¿O es al revés?" 
    show lside mors4 at left:
        yalign 1.0
        linear 40.0 yalign 0.0  
    "Los árboles dejan de reirse ante las frases silenciosas de los animales, y empiezan a susurrar entre ellos."       
    "Saben que no diré nada, {w=0.2}que no puedo decir nada. {w}Porque al igual que una bestia traicionera, {w=0.2}estoy maldito con una boca inservible."

    $ _history = False
    "De una rama cae un montículo de nieve,\n{nw}"
    extend "{alpha=0.0}De una rama cae un montículo de nieve,{fast}{/alpha} {w=0.2}y otro\n{nw}"
    extend "{alpha=0.0}De una rama cae un montículo de nieve, y otro,{fast}{/alpha}{w=0.2}y otro."
    $ _history = True
    $ if _history_list: _history_list[-1].what = "De una rama cae un montículo de nieve, y otro, y otro."
    "Como niños luego de la primera nevada, la lanzan buscando mi atención."
    nvl clear

    "—Oye."
    "Una de las ramas se inclina, {w=0.2}crujiendo."
    "—¿Por qué sigues pisandolas?"
    "Abro mi boca para responder, pero no sale más que un sonido ahogado y patetico.{w=0.2} Sujeto mi garganta con ambas manos, intentando calmar el ardor. {w}\n\nLos árboles explotan en carcajadas."
    "Dejo caer las retoricas infantiles sobre mi cuerpo mientras avanzo.{w=0.2} Las huellas en el piso parecen dar giros incomodos, hasta que se paran y dan la vuelta."
    "Las risas empiezan a apagarse y los arboles empiezan a separarse más unos de los otros hasta que el bosque se convierte en un claro."
    "Contrastando con el resto del escenario, {w=0.2}en medio de todo me encuentro con un macizo de flores."
    show lside mors5 at left:
        yalign 0.0
        linear 40.0 yalign 1.0  
    "Un campo de Asfodelos teñidos de rojo, con cenizas esparcidas en sus petalos como lo harian gotas de agua. {w=0.2}Alrededor suyo no hay nada, el camino termina ahí."          
    nvl clear

    "Puedo ver la salida desde donde estoy, la nieve blanca y nueva me llama a acercame y poner mi marca."
    "{size=+20}{cps=11}. . ."
    "{cps=15}Pero me doy la vuelta."
    "Hacia ese sendero de pisadas superpuestas, borrosas por la nieve que ya cayó."
        
    scene scen mors1
    nvl clear
    $ color_mode= "default"
    call set_mode("nadie")
    play audio bell volume 0.5
    "..."
    "Mis ojos recorren las calles como mis pies lo han hecho tantas veces antes.{w=0.2} Mis pupilas se detienen en las fachadas de los edificios,{w=0.2} en las caras de las personas{w=0.2}, y no reconozco a nadie,{w=0.2} no reconozco nada."

    "Me siento desorientado entre una multitud ruidosa, que parece gritar entre murmullos burlas que se sobreponen hasta convertirse en chillidos grotescos." 
    "Gente se mueve a mi lado, empujandose unos a otros tratando ojear el centro.{w=0.2} En un intento de caminar y pasar entre ellos levanto el pie levemente,{w=0.2} pero inmediatamente vuelve a tocar el piso." 
    "Siento mi cuerpo temblar, y no puedo hacer más que levantar mi mano,{w=0.2} en un movimiento más parecido a un arrastre sobre mi rostro,{w=0.2} que actua como un camino a recorrer para tapar mis orejas y silenciar el mundo."
    nvl clear

    play audio bell volume 0.6
    "..."
    "El viento mañanero golpea mi espalda y revuelve mi cabello ocultando mi rostro,{w=0.2} volviendose uno desconocido para los demás como lo son los suyos para mí." 
    "En este incognito me atrevo a levantar la mirada.{w=0.2} Con mis manos aprieto mi craneo y lo obligo a levantarse,"

    window hide
    call set_mode("izquierda")

    scene scen mors5:
        ypos -0.05
        linear 6.0 ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat
    
    show cg mors1:
        zoom 0.8
        ypos 0.20 xpos 0.12
        linear 6.0 ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show lside mors1 at left:
        ypos 1.2
        linear 6.0 ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat

    $ renpy.pause(6.0, hard=False)
    
    scene scen mors5:
        ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat

    show cg mors1:
        zoom 0.8
        xpos 0.12
        ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show lside mors1 at left:
        ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat
    
    scene scen mors5:
        ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat

    show cg mors1:
        zoom 0.8
        xpos 0.12
        ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show lside mors1 at left:
        ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat

    $ color_mode= "orange"
    play music armydreamers volume 0.7
    extend "{w=0.2} mi vista está difusa pero su silueta es clara,{w=0.2} mientras la veo a la cara puedo sentir como ella"
    nvl clear

    hide cg 
    hide lside
    window hide
    show scen mors6
    show text "{color=#f00}ME MIRA DE VUELTA.{/color}"
    pause 0.7
    hide text

    scene scen mors5:
        ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat

    show cg mors1:
        zoom 0.8
        xpos 0.12
        ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show lside mors1 at left:
        ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat
    
    scene scen mors5:
        ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat

    show cg mors1:
        zoom 0.8
        xpos 0.12
        ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show lside mors1 at left:
        ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat

    play audio bell volume 0.9
    "..."
    "El humo sube y la multitud no se calla,{w=0.2} algo en mi pecho se aprieta como si alguien metiera la mano y cerrara el puño,{w=0.2} y yo sigo sin moverme,{w=0.1} sigo sin moverme, sigo{nw}"
    "Quiero gritar,{w=0.2} pero las llamas me enfrian los huesos y el humo me quema la garganta convirtiendo las palabras en cenizas."
    "Quiero correr hacia delante, quiero devolverme y huir." 
    "Quiero sacarla de ahí,{w=0.2} tengo que,\n\ntengo que,\n\ntengo que,\n\ntengo que,\n\ntengo que,"
    stop music
    nvl clear

    window hide
    scene black
    pause 1
    play audio bell volume 1
    show undertale at truecenter:
        zoom 3.0
    show text "Prólogo - Mors":
        ypos 0.6
    pause 1
    hide undertale
    hide text
    pause 1

    jump luctus_negatio

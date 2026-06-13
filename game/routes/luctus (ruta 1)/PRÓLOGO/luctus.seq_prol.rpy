## Prólogo

label seq_prolcensura:
    $ _history = False
    $ renpy.music.set_volume(0.2, channel="sound")
    "{cps=50}—DIOS ES** *UE*** * *O**TR** L* ***AM**{nw} "
    $ renpy.music.set_volume(0.3, channel="sound")
    extend "\n\n{cps=100}—DI** **T* ****T* Y **S***O* ** M*****S{nw} "
    $ renpy.music.set_volume(0.4, channel="sound")
    extend "\n\n{cps=150}—*I*S **TA M***** * N******S *O *******{nw} "
    $ renpy.music.set_volume(0.5, channel="sound")
    extend "\n\n{cps=200}—**OS **** **R*** * ******** ** *******{nw} "
    $ renpy.music.set_volume(0.6, channel="sound")
    extend "\n\n{cps=250}—***S **** ****O * ***O**** ** **T****{nw} "
    $ renpy.music.set_volume(0.7, channel="sound")
    extend "\n\n{cps=300}—**** *S** ****** * ******** ** *A***O*{nw} "
    $ renpy.music.set_volume(0.8, channel="sound")
    extend "\n\n{cps=350}—**** **** ****** * ******** ** *******{nw} "
    $ renpy.music.set_volume(0.9, channel="sound")
    extend "\n\n{cps=450}—**** **** ****** * ******** ** *******{nw} "
    $ renpy.music.set_volume(1.0, channel="sound")
    extend "\n\n{cps=500}—**** **** ****** * ******** ** *******{nw} "
    extend "\n{fast}{nw} "
    $ _history = True
    $ if _history_list: _history_list[-1].what = "—La curiosidad mató al gato, y te matara a ti."
    stop sound
    $ renpy.music.set_volume(1.0, channel="sound")
    return

label seq_prolpav1:
    
    nvl clear
    window hide
    scene bg ciudad1:
        ypos -0.05
        linear 6.0 ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat
    
    show pavel1ana:
        zoom 0.8
        ypos 0.20 xpos 0.12
        linear 6.0 ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show anaraith2 at left:
        ypos 1.2
        linear 6.0 ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat

    $ renpy.pause(6.0, hard=False)
    
    scene bg ciudad1:
        ypos 0.0
        block:
            linear 2.2 ypos -0.01         
            linear 2.2 ypos 0.0
            repeat

    show pavel1ana:
        zoom 0.8
        xpos 0.12
        ypos 0.16
        block:           
            linear 2.2 ypos 0.17
            linear 2.2 ypos 0.16
            repeat

    show anaraith2 at left:
        ypos 1.4
        block:
            linear 2.2 ypos 1.38
            linear 2.2 ypos 1.4
            repeat
        
    window show
        
    play audio bell volume 0.5
    "..."
    "Mis ojos recorren las calles como mis pies lo han hecho tantas veces antes.{w=0.3} Mis pupilas se detienen en las fachadas de los edificios,{w=0.2} en las caras de las personas{w=0.2}, y no reconozco a nadie,{w=0.3} no reconozco nada."
    "Me siento desorientado entre una multitud ruidosa, que parece gritar entre murmullos burlas que se sobreponen hasta convertirse en chillidos grotescos." 
    "Gente se mueve a mi lado, empujandose unos a otros tratando ojear el centro.{w=0.3} En un intento de caminar y pasar entre ellos levanto el pie levemente,{w=0.2} pero inmediatamente vuelve a tocar el piso." 
    "Siento mi cuerpo temblar, y no puedo hacer más que levantar mi mano,{w=0.2} en un movimiento más parecido a un arrastre sobre mi rostro,{w=0.2} que actua como un camino a recorrer para tapar mis orejas y silenciar el mundo."
    nvl clear

    play audio bell volume 0.6
    "..."
    "El viento mañanero golpea mi espalda y revuelve mi cabello ocultando mi rostro,{w=0.2} volviendose uno desconocido para los demás como lo son los suyos para mí." 
    "En este incognito me atrevo a levantar la mirada.{w=0.3} Con mis manos aprieto mi craneo y lo obligo a levantarse,{w=0.2} mi vista está difusa pero su silueta es clara,{w=0.2} mientras la veo a la cara puedo sentir como ella {color=#f00}me mira devuelta.{/color}"
    nvl clear

    play audio bell volume 0.7
    "..."
    "Imitando un casamiento,{w=0.2} las campanas resuenan haciendo eco en las veredas,{w=0.2} me van a volver loco,{w=0.3} suenan,{cps=24} y suenan,{w=0.25}{cps=36} y suenan,{w=0.2}{cps=48} y suenan,{w=0.15}{cps=60} y suenan,{w=0.1}{cps=72} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan."
    "Me pregunto si habrá amado." 
    "Hace años dejé de creer en el dios cretino del que tanto me hablaron,{w=0.2} me pregunto{w=0.2} ¿Le habrá rezado?{w=0.2} ¿Se habrá puesto de rodillas ante una ventana y deseado con todas sus fuerzas no morir?"
    "Vivió una vida tan miserable como la mía,{w=0.2} significa entonces{w=0.2} ¿Que moriré también?"
    "No,{w=0.3} no, no, no."
    nvl clear

    play audio bell volume 0.8
    "..."
    "Eso significaria que su vida no tuvo significado."
    "La forma en la que hablaba, en la que me miraba, sus habitos, nada de eso importaria." #no te estaba viendo a tí, estaba viendo a caithra tonto weon
    "No, no puede ser así."
    "¿Cuál es el punto de vivir si se iba a convertir en polvo?"
    "{cps=24}Ella no está muerta."
    "{cps=24}Es imposible."
    "{cps=36}No puede morir así."
    "{cps=36}Es absurdo."
    "{cps=48}No tiene sentido."
    "{cps=48}¿Por qué volví?"
    "¿Por qué volvió?"
    nvl clear
    "Quiero gritar,{w=0.3} pero las llamas me enfrian los huesos y el humo me quema la garganta convirtiendo las palabras en cenizas."
    nvl clear

    play audio bell volume 0.9
    "..."

    "El fuego está caliente,{w=0.3} le quema la punta de los dedos,{w=0.3} le quema el cuerpo.{w=0.3} La quema.{w=0.3} El olor es insoportable y mis pies no se mueven y mis manos no se mueven y yo no me muevo y el olor sigue ahí y el olor no para." 
    "{cps=24}Quiero correr hacia delante,{w=0.3} {color=#f00}quiero devolverme y huir.{/color}{w=0.3}" 
    "El té siempre se le olvidaba.{w=0.3} Lo dejaba reposar porque estaba muy caliente, cuando se acordaba ya estaba helado y lo empujaba a un lado como si no fuera culpa suya."
    "{cps=6}Es culpa mía."

    "{cps=12}El humo sube y la multitud no se calla,{w=0.3} algo en mi pecho se aprieta como si alguien metiera la mano y cerrara el puño,{cps=24}{w=0.2} y yo sigo sin moverme,{cps=36}{w=0.1} sigo sin moverme,{cps=48} sigo{nw}"
    nvl clear

    "{cps=6}Quiero sacarla de ahí,{w=0.3}{cps=12} tengo que,"
    "{cps=6}Tengo que, \n\n{cps=12}Tengo que,{nw}"
    extend "\n\nTengo {fast}{cps=6}que, \n\nTengo {fast}{cps=6}que,{nw}"
    extend "\n\nTengo que,{fast}{nw} \n\nTengo que,{fast}{nw}"
    window hide None
    scene black
    pause 0.2
    play audio bell volume 1.0
    pause 1.0
    nvl clear
    window show None
    scene bg bosque
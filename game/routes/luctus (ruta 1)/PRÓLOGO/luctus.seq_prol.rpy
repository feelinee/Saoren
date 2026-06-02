## Prólogo

label seq_prólcensura:
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

label seq_prólpav1:
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
    "La multitud es ruidosa,{w=0.3} sus murmullos suenan como gritos.{w=0.3}{cps=6} Algo se mueve a mi lado,{w=0.3} y yo no puedo hacer nada más que temblar donde estoy."
    "{cps=12}Las campanas me van a volver loco,{w=0.3} {cps=24} suenan,{w=0.25}{cps=36} y suenan,{w=0.2} {cps=48} y suenan,{w=0.15}{cps=60} y suenan,{w=0.1}{cps=72} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan,{w=0.1} y suenan."
    play audio bell volume 0.6
    "{cps=16}El frío.{w=0.3}{cps=24} Anaraith odiaba el frío.{w=0.3}{cps=12} Le ponía los hombros tensos y arrugaba la nariz sin darse cuenta.{w=0.3} Una vez me dijo que el invierno le robaba el aire antes de que pudiera respirarlo.{cps=18}{w=0.3} \n\nYo me reí.{w=0.3}{cps=19} \n\nMe reí."
    "{cps=6}Quiero gritar,{w=0.3}{cps=12} pero el fuego me enfria los huesos y el humo me quema la garganta convirtiendo las palabras en cenizas."
    play audio bell volume 0.7
    nvl clear

    "El fuego está caliente,{w=0.3}{cps=24} le quema la punta de los {cps=6}dedos,{w=0.3}{cps=24} le quema el cuerpo.{w=0.3} La quema.{w=0.3}{cps=12} El olor es insoportable {cps=24}y mis pies no se mueven {cps=36}y mis manos no se mueven {cps=48}y yo no me muevo {cps=60}y el olor sigue ahí y el olor {cps=6}no para." 
    "{cps=24}Quiero correr hacia delante,{w=0.3}{cps=12} {color=#f00}quiero devolverme y huir.{/color}{w=0.3}" 
    play audio bell volume 0.8
    "El té siempre se le olvidaba.{w=0.3} Lo dejaba reposar porque estaba muy caliente, cuando se acordaba ya estaba helado y lo empujaba a un lado como si no fuera culpa suya."
    "{cps=6}Es culpa mía."
    play audio bell volume 0.9
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
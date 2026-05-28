## Prólogo

label seq_prólcensura:
    $ _history = False
    $ renpy.music.set_volume(0.2, channel="sound")
    "{cps=50}—DIOS ES** *UE*** * *O**TR** L* ***AM**{nw} "
    $ renpy.music.set_volume(0.3, channel="sound")
    "{cps=100}—DI** **T* ****T* Y **S***O* ** M*****S{nw} "
    $ renpy.music.set_volume(0.4, channel="sound")
    "{cps=150}—*I*S **TA M***** * N******S *O *******{nw} "
    $ renpy.music.set_volume(0.5, channel="sound")
    "{cps=200}—**OS **** **R*** * ******** ** *******{nw} "
    $ renpy.music.set_volume(0.6, channel="sound")
    "{cps=250}—***S **** ****O * ***O**** ** **T****{nw} "
    $ renpy.music.set_volume(0.7, channel="sound")
    "{cps=300}—**** *S** ****** * ******** ** *A***O*{nw} "
    $ renpy.music.set_volume(0.8, channel="sound")
    "{cps=350}—**** **** ****** * ******** ** *******{nw} "
    $ renpy.music.set_volume(0.9, channel="sound")
    "{cps=450}—**** **** ****** * ******** ** *******{nw} "
    $ renpy.music.set_volume(1.0, channel="sound")
    "{cps=500}—**** **** ****** * ******** ** *******{nw} "
    $ _history = True
    $ if _history_list: _history_list[-1].what = "—La curiosidad mató al gato, y te matara a ti."
    stop sound
    $ renpy.music.set_volume(1.0, channel="sound")
    return

label seq_prólpav1:
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

    pause
    scene bg bosque
    hide pavel1ana
    hide anaraith2
## Defaults

default persistent.luctus_compl = False
default color_mode = "default"

## Defines

define pav = Character("PAVEL", kind=nvl)
define ana = Character("ANARAITH", kind=nvl)
define mar = Character("MARCILLE", kind=nvl)
define asf = Character("ASFÓDEL", kind=nvl)
define qn = Character("???",  kind=nvl)
define narrator = Character(None, kind=nvl)
define menu = nvl_menu

#callback=make_type_sound(sounds_default)

define color_texto = {
    "default" : "#bebebe",
    "blue"    : "#b2c6e4",
    "red"     : "#e4b2b2",
    "orange" : "#e4dbb2",
    "green" : "#9ec1d1"
}

define color_enfocado = {
    "default" : '#6c6c6c',
    "blue"    : '#0007cc',
    "red"     :  '#cc0000',
    "orange" : '#cc6600',
    "green" :  '#10b777'
}

## Voces

init -1 python:

    sounds_default  = ['audio/voces/default/bip1.mp3', 'audio/voces/default/bip2.mp3', 'audio/voces/default/bip3.mp3']
    sounds_pavel    = ['audio/voces/pavel/pav1.mp3', 'audio/voces/pav2.mp3']
    sounds_marcille    = ['audio/voces/marcille/pav1.mp3', 'audio/voces/marcille/pav2.mp3']
    sounds_anaraith = ['audio/voces/anaraith/ana1.mp3', 'audio/voces/anaraith/ana2.mp3']

    import re
    renpy.music.register_channel("typing", "sfx", loop=False)

    def make_type_sound(sound_list, volume=0.05):
        def type_sound(event, interact=True, vol=volume, **kwargs):
            if not interact:
                return
            if event == "show":
                what = kwargs.get("what", "")
                clean = re.sub(r'\{[^}]*\}', '', what)
                num = max(len(clean.replace(" ", "")), 1)
                for i in range(num):
                    renpy.music.queue(renpy.random.choice(sound_list), channel="typing", relative_volume=vol)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="typing")
        return type_sound

## Pavel Sprites

image pavel neutral: 
    "images/pjs/Pavel Prologo Sprites/pavel normal.png"
    zoom 0.30
image pavel triste: 
    "images/pjs/Pavel Prologo Sprites/pavel triste.png"
    zoom 0.30
image pavel enojado: 
    "images/pjs/Pavel Prologo Sprites/pavel enojado.png"
    zoom 0.30
image pavel dudoso: 
    "images/pjs/Pavel Prologo Sprites/pavel dudoso.png"
    zoom 0.30
image pavel anaraith: 
    "images/pjs/Pavel Prologo Sprites/pavel anaraith.png"
    zoom 0.30
image pavel anaraith2: 
    "images/pjs/Pavel Prologo Sprites/pavel anaraith2.png"
    zoom 0.30

## Side images

# Mors

image side mors1 = "images/side/mors/side_mors_1.png"
image side mors2 = "images/side/mors/side_mors_2.png"
image side mors3 = "images/side/mors/side_mors_3.png"
image side mors4 = "images/side/mors/side_mors_4.png"    
image side mors5 = "images/side/mors/side_mors_5.png"   

## Scenes

# Mors

image scen mors1 = "images/scenes/mors/scene_mors_1.png"
image scen mors3 = Movie(play="images/scenes/mors/scene_mors_3.webm", loop=False)
image scen mors5 = "images/scenes/mors/scene_mors_5.png"
image scen mors6 = "images/scenes/mors/scene_mors_6.png"
image scen mors7 = "images/scenes/mors/scene_mors_7.png"
image scen mors8 = "images/scenes/mors/scene_mors_8.png"

# Negatio

image scen nega1 = "images/scenes/negatio/scene_negatio_1.png"
image scen nega2 = "images/scenes/negatio/scene_negatio_2.png"
image scen nega3 = "images/scenes/negatio/scene_negatio_3.jpg"
image scen nega4 = "images/scenes/negatio/scene_negatio_4.png"

## Cgs

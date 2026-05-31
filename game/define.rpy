# Defaults

default persistent.luctus_compl = False
default color_mode = "default"

# Defines

define pav = Character("PAVEL", kind=nvl, color="#e4dbb2")
define ana = Character("ANARAITH", kind=nvl, color="#e4dbb2")
define mar = Character("MARCILLE", kind=nvl, color="#e4dbb2")
define asf = Character("ASFÓDEL", kind=nvl, color="#e4dbb2")
define qn = Character("???",  kind=nvl, color="#e4dbb2", )
define narrator = Character(None, kind=nvl)
define menu = nvl_menu

#callback=make_type_sound(sounds_default)

define color_texto = {
    "default" : "#e4dbb2",
    "blue"    : "#b2c6e4",
    "red"     : "#e4b2b2",
    "orange" : "#e4dbb2",
    "green" : "#9ec1d1"
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
# Images

## Pavel Sprites

image pavel neutral: 
    "images/Pjs/Pavel Prologo Sprites/pavel normal.png"
    zoom 0.30
image pavel triste: 
    "images/Pjs/Pavel Prologo Sprites/pavel triste.png"
    zoom 0.30
image pavel enojado: 
    "images/Pjs/Pavel Prologo Sprites/pavel enojado.png"
    zoom 0.30
image pavel dudoso: 
    "images/Pjs/Pavel Prologo Sprites/pavel dudoso.png"
    zoom 0.30
image pavel anaraith: 
    "images/Pjs/Pavel Prologo Sprites/pavel anaraith.png"
    zoom 0.30
image pavel anaraith2: 
    "images/Pjs/Pavel Prologo Sprites/pavel anaraith2.png"
    zoom 0.30

## Side images

image side arboles = "images/Side/arboles.png"
image side pisadas = "images/Side/pisadas.png"   
image side flores = "images/Side/asfodelos.png"    

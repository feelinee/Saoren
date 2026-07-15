## Defaults

default persistent.luctus_compl = False
default color_mode = "default"

## Defines

define pav = Character("Pavel", kind=nvl)
define ana = Character("Anaraith", kind=nvl)
define mar = Character("Marcille", kind=nvl)
define asf = Character("Asfodel", kind=nvl)
define qn = Character("???",  kind=nvl)
define narrator = Character(None, kind=nvl)
define menu = nvl_menu

#callback=make_type_sound(sounds_default)

define color_texto = {
    "default" : "#bebebe",
    "blue"    : "#b2c6e4",
    "red"     : "#e4b2b2",
    "orange" : "#e4dbb2",
    "green" : "#b2e4dc"
}

define color_enfocado = {
    "default" : '#6c6c6c',
    "blue"    : '#0007cc',
    "red"     :  '#cc0000',
    "orange" : '#cc6600',
    "green" :  '#10b777'
}

define color_burbuja_izq = {
    "default": "#4e7ea0",
    "blue":    "#3a6a8c",
    "red":     "#7a4e4e",
    "orange":  "#ed8856",
    "green":   "#63959c",
}

define color_burbuja_der = {
    "default": "#a0714e",
    "blue":    "#5a6e8c",
    "red":     "#9c4e4e",
    "orange":  "#5a3c40",
    "green":   "#5c8c79",
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

init python:

    class ColaDeBurbuja(renpy.Displayable):
        """
        Triángulo que apunta hacia el personaje que habla.
        lado  : "izquierda" o "derecha"
        color : hex string e.g. "#4e7ea0"
        """
        def __init__(self, lado, color, ancho=13, alto=24, **properties):
            super(ColaDeBurbuja, self).__init__(**properties)
            self.lado  = lado
            self.color = color
            self.ancho = ancho
            self.alto  = alto

        def render(self, width, height, st, at):
            w, h_dim = self.ancho, self.alto
            surf   = renpy.Render(w, h_dim)
            canvas = surf.canvas()
            h = self.color.lstrip('#')
            c = (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)
            if self.lado == "izquierda":
                pts = [(w, 2), (w, h_dim - 2), (0, h_dim // 2)]
            else:
                pts = [(0, 2), (0, h_dim - 2), (w, h_dim // 2)]
            canvas.polygon(c, pts)
            return surf

        def visit(self):
            return []

    # ── Registro estático ─────────────────────────────────────────────────────
    _burbuja_cfg = {}

    def registrar_burbuja(nombre, lado):
        _burbuja_cfg[nombre] = {"lado": lado}

    def burbuja_de(who):
        if who is None:
            return None
        return _burbuja_cfg.get(who, None)

init 1 python:
    registrar_burbuja("Pavel",    "izquierda")
    registrar_burbuja("Marcille", "derecha")

style nvl_burbuja_quien:
    size 13
    bold True
    outlines []
    kerning 0.5

style nvl_burbuja_texto:
    size 16
    outlines []
    line_spacing 4

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
image scen nega5 = "images/scenes/negatio/scene_negatio_5.png"

## Pjs

# Negatio

image pav nega1= "images/pjs/pavel/pav_nega1.png"
image mar nega1= "images/pjs/marcille/mar_nega1.png"

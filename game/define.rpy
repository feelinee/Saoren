#Defines

define pav = Character("PAVEL", kind=nvl, color="#e4dbb2")
define ana = Character("ANARAITH", kind=nvl, color="#e4dbb2")
define mar = Character("MARCILLE", kind=nvl, color="#e4dbb2")
define asf = Character("ASFÓDEL", kind=nvl, color="#e4dbb2")
define qn = Character("???",  kind=nvl, color="#e4dbb2")
define narrator = nvl_narrator
define menu = nvl_menu

define color_texto = {
    "default" : "#e4dbb2",
    "blue"    : "#b2c6e4",
    "red"     : "#e4b2b2",
    "orange" : "#e4dbb2"
}

#Defaults

default persistent.luctus_compl = False
default color_mode = "default"

#Images

##Pavel Sprites

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

##Side images

image side arboles = "images/Side/arboles.png"
image side pisadas = "images/Side/pisadas.png"   
image side flores = "images/Side/asfodelos.png"        

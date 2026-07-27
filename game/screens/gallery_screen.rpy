init python:
    g = Gallery()
    g.navigation = True

    g.button("gato")
    g.image("scen negatio3")
    g.unlock("scen negatio3")

    g.button("pavcille")
    g.image("scen negatio4")
    g.unlock("scen negatio4")
    

screen gallery():
    tag menus
    add "scen mors1"
    grid 2 2:
        xfill True
        yfill True
        spacing 1

        imagebutton:
            idle "extras/galeria/gallery_cgs.png"
            action ShowMenu("gallery_cgs")
            xalign 0.5
            yalign 0.5

        imagebutton:
            idle "extras/galeria/gallery_bgs.png"
            action ShowMenu("gallery_bgs")
            xalign 0.5
            yalign 0.5

        imagebutton:
            idle "extras/galeria/gallery_sprites.png"
            action ShowMenu("gallery_bgs")
            xalign 0.5
            yalign 0.5

        imagebutton:
            idle "extras/galeria/gallery_extras.png"
            action ShowMenu("gallery_bgs")
            xalign 0.5
            yalign 0.5

    textbutton "Return" action Return() xalign 0.03 yalign 0.03

screen gallery_bgs():
    
    tag menu
    add "scen negatio4"
    grid 3 2:
        xfill True
        yfill True
        spacing 30
    
        add g.make_button("gato", "extras/galeria/gato.png", xalign=0.5, yalign=0.5)

    textbutton "Return" action ShowMenu("gallery") xalign 0.03 yalign 0.03

screen gallery_cgs():
    tag menu
    add "scen mors8"
    grid 3 2:
        xfill True
        yfill True
        spacing 30

        add g.make_button("pavcille","extras/galeria/pavcille.png", xalign=0.5, yalign=0.5)

    textbutton "Return" action ShowMenu("gallery") xalign 0.03 yalign 0.03
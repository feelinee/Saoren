default text_mode = "default"
default nvl_bg = "gui/nvl1.png"

default text_xpos  = 120
default text_ypos  = 100
default text_xsize = 1680

label mode_nadie:

    $ text_mode  = "nadie"
    $ nvl_bg     = "gui/nvl1.png"
    $ text_xpos  = 120
    $ text_ypos  = 100
    $ text_xsize = 1680
    return


label mode_derecha:

    $ text_mode  = "derecha"
    $ nvl_bg     = "gui/nvl2.png"
    $ text_xpos  = 120
    $ text_ypos  = 140
    $ text_xsize = 1000
    return


label mode_izquierda:

    $ text_mode  = "izquierda"
    $ nvl_bg     = "gui/nvl3.png"
    $ text_xpos  = 700
    $ text_ypos  = 140
    $ text_xsize = 1000
    return


label mode_medio:

    $ text_mode  = "medio"
    $ nvl_bg     = "gui/nvl4.png"
    $ text_xpos  = 700
    $ text_ypos  = 180
    $ text_xsize = 520
    return

screen nvl(dialogue, items=None):

    add nvl_bg xpos 0 ypos 0

    window:
        id "window"
        background None
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height

        fixed:

            viewport:
                id "nvl_viewport"
                xpos  text_xpos
                ypos  text_ypos
                xsize text_xsize
                ysize (config.screen_height - text_ypos - 60)

                mousewheel True
                draggable True
                yinitial 1.0

                vbox:
                    spacing 30
                    xfill True

                    for d in dialogue:

                        window:
                            id d.window_id
                            background None
                            xfill True

                            vbox:
                                spacing 5
                                xfill True

                                if d.who is not None:
                                    text d.who:
                                        id d.who_id
                                        xmaximum text_xsize

                                text d.what:
                                    id d.what_id
                                    xmaximum text_xsize

            if items is not None:
                vbox:
                    xalign 0.5
                    yalign 0.85
                    spacing 12

                    for i in items:
                        textbutton i.caption:
                            action i.action

style nvl_entry:
    xfill True
    ysize None

style nvl_dialogue:
    xpos 0
    ypos 0

style nvl_thought:
    xpos 0
    ypos 0        

style nvl_label:
    xpos 0
    ypos 0             
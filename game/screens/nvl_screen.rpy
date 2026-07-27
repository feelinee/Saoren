## Defaults

default text_mode = "default"
default nvl_bg = "gui/nvl/nvl1.png"
default text_xpos = 120
default text_ypos = 140
default text_xsize = 1680
define who_width_default = 150

## Defines
 
define _cfg_modos = {
    "nadie":     {"bg": "gui/nvl/nvl1.png", "xpos": 220, "ypos": 140, "xsize": 1480},
    "derecha":   {"bg": "gui/nvl/nvl2.png", "xpos": 180, "ypos": 140, "xsize": 1000},
    "izquierda": {"bg": "gui/nvl/nvl3.png", "xpos": 750, "ypos": 140, "xsize": 1000},
    "medio":     {"bg": "gui/nvl/nvl4.png", "xpos": 750, "ypos": 140, "xsize": 450},
}


define config.nvl_list_length = gui.nvl_list_length

## Styles

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

## Labels

label set_mode(modo):
    $ _m = _cfg_modos[modo]
    $ text_mode = modo
    $ nvl_bg = _m["bg"]
    $ text_xpos = _m["xpos"]
    $ text_ypos = _m["ypos"]
    $ text_xsize = _m["xsize"]
    return


## Screens

screen nvl(dialogue, items=None):
    $ _bg = nvl_bg if color_mode == "default" else nvl_bg.replace(".png", f"_{color_mode}.png")
    add _bg xpos 0 ypos 0
    window:
        id "window"
        background None
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height
        fixed:
            use nvl_viewport(dialogue)
            if items is not None:
                use nvl_menu(items)


screen nvl_viewport(dialogue):
    viewport:
        id "nvl_viewport"
        xpos  text_xpos
        ypos  text_ypos
        xsize text_xsize
        ysize (config.screen_height - text_ypos - 60)
        mousewheel True
        draggable  True
        yinitial   1.0
        vbox:
            spacing 30
            xfill True
            for d in dialogue:
                use nvl_entrada(d)


screen nvl_entrada(d):
    window:
        id d.window_id
        background None
        xfill True
 
        if d.who is not None:
            $ _who_width = d.who_args.get("xsize", who_width_default)
            hbox:
                spacing 6
                text d.who:
                    id d.who_id
                    style "nvl_dialogue"
                    yalign 0.0
                    properties d.who_args
                text d.what:
                    id d.what_id
                    style "nvl_dialogue"
                    xmaximum (text_xsize - _who_width)
                    yalign 0.0
                    properties d.what_args
        else:
            text d.what:
                id d.what_id
                style "nvl_dialogue"
                xmaximum text_xsize
                properties d.what_args
                color color_texto.get(color_mode, "#e4dbb2")



screen nvl_modo_normal(d):
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
            color color_texto.get(color_mode, "#e4dbb2")


screen nvl_menu(items):
    vbox:
        xalign 0.5
        yalign 0.85
        spacing 12
        for i in items:
            textbutton i.caption:
                action i.action
                text_hover_color color_enfocado.get(color_mode, "#cc6600")




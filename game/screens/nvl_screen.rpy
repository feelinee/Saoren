## Defaults

default text_mode  = "default"
default nvl_bg     = "gui/nvl/nvl1.png"
default text_xpos  = 120
default text_ypos  = 140
default text_xsize = 1680

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
    $ _m         = _cfg_modos[modo]
    $ text_mode  = modo
    $ nvl_bg     = _m["bg"]
    $ text_xpos  = _m["xpos"]
    $ text_ypos  = _m["ypos"]
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
        if text_mode == "medio":
            use nvl_modo_medio(d)
        else:
            use nvl_modo_normal(d)


screen nvl_modo_medio(d):
    $ _cfg_b       = burbuja_de(d.who)
    $ _lado        = _cfg_b["lado"] if _cfg_b else None
    $ _ancho_frame = int(text_xsize * 0.97)
    $ _ancho_texto = _ancho_frame - 24
    $ _color_izq   = color_burbuja_izq.get(color_mode, "#373737")
    $ _color_der   = color_burbuja_der.get(color_mode, "#0a0a0a")

    if _cfg_b and _lado == "izq":
        use nvl_burbuja(d, "izq", _color_izq, _ancho_frame, _ancho_texto)
    elif _cfg_b and _lado == "der":
        use nvl_burbuja(d, "der", _color_der, _ancho_frame, _ancho_texto)
    else:
        use nvl_modo_normal(d)


screen nvl_burbuja(d, lado, bcolor, ancho_frame, ancho_texto):
    $ _bg_b = Transform(Solid(bcolor), alpha=0.8)
    text "" id d.who_id

    if lado == "izq":
        hbox:
            xfill True
            spacing 0
            add Transform(DeltaBurbuja("izq", bcolor), alpha=0.8) xsize 13 ysize 40 yalign 0.5
            frame:
                xsize ancho_frame
                background _bg_b
                padding (12, 10, 12, 10)
                text d.what:
                    id d.what_id
                    style "nvl_burbuja_texto"
                    xmaximum ancho_texto
                    color color_texto.get(color_mode, "#e4dbb2")
            null xfill True
    else:
        hbox:
            xfill True
            spacing 0
            null xfill True
            frame:
                xsize ancho_frame
                background _bg_b
                padding (12, 10, 12, 10)
                text d.what:
                    id d.what_id
                    style "nvl_burbuja_texto"
                    xmaximum ancho_texto
                    color color_texto.get(color_mode, "#e4dbb2")
            add Transform(DeltaBurbuja("der", bcolor), alpha=0.8) xsize 13 ysize 40 yalign 0.5


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




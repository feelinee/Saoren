label start:
    if persistent.luctus_compl:
        jump menu_rutas
    else:
        jump luctus_prologue

label menu_rutas:
    call mode_medio
    "elige tu ruta bruh"

    menu:
        "pavel":
            nvl clear
            jump luctus_prologue
        "magnus":
            nvl clear
            "no existe lol"
            $ persistent.luctus_compl = False
            pass

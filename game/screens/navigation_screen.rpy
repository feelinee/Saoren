## Defaults

default quick_menu = True

## Styles

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.00


style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Comenzar") action Start()

        else:

            textbutton _("Historial") action ShowMenu("history")

            textbutton _("Guardar") action ShowMenu("save")

        textbutton _("Cargar") action ShowMenu("load")

        textbutton _("Opciones") action ShowMenu("preferences")

        textbutton _("Galería") action ShowMenu("gallery")

        if _in_replay:

            textbutton _("Finaliza repetición") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menú principal") action MainMenu()

        textbutton _("Acerca de") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## La ayuda no es necesaria ni relevante en dispositivos móviles.
            textbutton _("Ayuda") action ShowMenu("help")

        if renpy.variant("pc"):

            ## El botón de salida está prohibido en iOS y no es necesario en
            ## Android y Web.
            textbutton _("Salir") action Quit(confirm=not main_menu)

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Historial") action ShowMenu('history')
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Guardar") action ShowMenu('save')
            textbutton _("Guardado R.") action QuickSave()
            textbutton _("Cargado R.") action QuickLoad()
            textbutton _("Config.") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")



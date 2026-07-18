## Defaults

default persistent.menu_music_muted = False

## Styles

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Screens

screen main_menu():

    tag menu

    on "show" action [
        Play("menumusic", "audio/Simbiosis.mp3"),
        Function(renpy.music.set_volume, 0.0 if persistent.menu_music_muted else 1.0, channel="menumusic")
    ]

    add gui.main_menu_background

    ## Este marco vacío oscurece el menu principal.
    frame:
        style "main_menu_frame"

    ## La sentencia 'use' incluye otra pantalla dentro de esta. El contenido
    ## real del menú principal está en la pantalla de navegación.
    use navigation

    if gui.show_name:

        textbutton _("Silenciar"):
            action Function(toggle_menu_mute)
            style "mute_all_button"
            xpos 1730
            ypos 20

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


## Init

init python:
    renpy.music.register_channel("menumusic", mixer="music", loop=True)


init python:
    def toggle_menu_mute():
        persistent.menu_music_muted = not persistent.menu_music_muted
        renpy.music.set_volume(0.0 if persistent.menu_music_muted else 1.0, channel="menumusic")


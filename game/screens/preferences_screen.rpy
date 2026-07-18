## Styles

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

## Screens

screen preferences():

    tag menu

    use game_menu(_("Opciones"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Pantalla")
                        textbutton _("Ventana") action Preference("display", "window")
                        textbutton _("Pantalla completa") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Saltar")
                    textbutton _("Texto no visto") action Preference("skip", "toggle")
                    textbutton _("Tras elecciones") action Preference("after choices", "toggle")
                    textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

                ## Aquí se pueden añadir 'vboxes' adicionales del tipo
                ## "radio_pref" o "check_pref" para nuevas preferencias.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    #label _("Veloc. texto")

                    #bar value Preference("text speed")

                    label _("Veloc. autoavance")

                    bar value Preference("auto-forward time")

                vbox:

                    label _("Volumen General")
                    hbox:
                        bar value Preference("mixer main volume")

                    if config.has_music:

                        label _("Volumen música")
                        hbox:
                            bar value Preference("music volume")



                    if config.has_sound:

                        label _("Volumen sonido")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Prueba") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volumen voz")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Prueba") action Play("voice", config.sample_voice)

                    null height gui.pref_spacing

                    textbutton _("Silenciar"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

## Defaults

default pos_burbuja = {
    "Pavel":    "izq",
    "Marcille": "der",
    "Fauna": "izq",
    "Dios": "der",
    "Vendedor": "der",
}

## Defines

define color_burbuja_izq = {
    "default": "#373737",
    "blue":    "#3a6a8c",
    "red":     "#7a4e4e",
    "orange":  "#ed8856",
    "green":   "#63959c",
}

define color_burbuja_der = {
    "default": "#0a0a0a",
    "blue":    "#5a6e8c",
    "red":     "#9c4e4e",
    "orange":  "#5a3c40",
    "green":   "#5c8c79",
}

## Styles

style nvl_burbuja_quien:
    size 13
    bold True
    outlines []
    kerning 0.5

style nvl_burbuja_texto:
    size 16
    outlines []
    line_spacing 4


init python:


    class DeltaBurbuja(renpy.Displayable):
        def __init__(self, lado, color, ancho=13, alto=24, **properties):
            super(DeltaBurbuja, self).__init__(**properties)
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
            if self.lado == "izq":
                pts = [(w, 2), (w, h_dim - 2), (0, h_dim // 2)]
            else:
                pts = [(0, 2), (0, h_dim - 2), (w, h_dim // 2)]
            canvas.polygon(c, pts)
            return surf

        def visit(self):
            return []

    def burbuja_de(who):
        if who is None:
            return None
        lado = renpy.store.pos_burbuja.get(who, None)
        if lado is None:
            return None
        return {"lado": lado}

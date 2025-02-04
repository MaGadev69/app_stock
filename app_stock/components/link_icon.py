import reflex as rx


def link_icon(icon: str, url: str, size: str) -> rx.Component:
    return rx.el.a(  #Elemento HTML	<i> (ícono)	<a> (botón)
        "",
        class_name=f"nes-icon {icon} {size}",
        # Las librerías como NES.css tienen varias opciones para tamaños predefinidos, como is-small, is-medium, y is-large. 
        # Cambia is-medium por otra clase para ajustar el tamaño.
        on_click=rx.redirect(url,external=True),
    )
def button(text: str, url: str, size: str, width: str = None, height: str = None) -> rx.Component:
    return rx.el.a(
        text,
        class_name=f"nes-btn is-warning {size}",
        on_click=rx.redirect(url,external=False),

        style={
            "width": width,  # Ancho personalizado
            "height": height,  # Alto personalizado
            "display": "inline-flex",  # Para alinear el contenido correctamente
            "align_items": "center",  # Centrar el contenido verticalmente
            "justify_content": "center",  # Centrar el contenido horizontalmente
        },
    )


# Si ambos botones hacen lo mismo, puedes unificarlos en una sola función y agregar una opción para que tenga ícono o texto:
#def custom_button(
#    url: str,
#    text: str = None,
#    icon: str = None,
#    size: str = "is-medium",
#    width: str = None,
#    height: str = None
#) -> rx.Component:
#    content = rx.el.i(class_name=f"nes-icon {icon} {size}") if icon else text  # Muestra ícono o texto
#    return rx.el.a(
#        content,
#       class_name=f"nes-btn is-warning {size}",
#        on_click=rx.redirect(url, external=False),  # Navegación en la misma pestaña
#        style={
#            "width": width,
#            "height": height,
#            "display": "inline-flex",
#            "align_items": "center",
#            "justify_content": "center",
#        }
#   )

# llamada
#custom_button(url="/otra_pagina", text="Ir a otra página")
#custom_button(url="/home", icon="star")

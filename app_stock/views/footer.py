import reflex as rx
from app_stock.styles.styles import Size
from app_stock.styles import styles
from app_stock.styles.colors import Color,TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                "© 2025 MVP Stock Reflex",
                font_size=Size.SMALL.value,
                color=TextColor.QUATERNARY.value,
            ),
            rx.text(
                "Creado con Cafe por MaGaDev",
                font_size=Size.SMALL.value,
                color=TextColor.QUATERNARY.value,
            ),  
            spacing="1",
        ),
        align_items="center", #esto sirve para alinear los elementos dentro del vstack al centro, start, end, center, baseline, stretch
        #justify_content="",  # Centra el contenido en el eje vertical (Y) 
        #border_top=f"0.25em solid {Color.SECONDARY.value}", # linea navbar
        padding_x=Size.BIG.value, # esto sirve para que el navbar no quede pegado a los bordes izquierdo
        padding_y=Size.DEFAULT.value, # esto sirve para que el navbar no quede pegado a los bordes inferior
        width="100%", #esto sirve para que el navbar ocupe todo el ancho de la pantalla
        text_align="center", # alinea el texto al centro
    )
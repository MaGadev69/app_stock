import reflex as rx
import app_stock.constants as constants

import app_stock.styles.styles as styles
from app_stock.styles.styles import Size
from app_stock.styles.colors import TextColor


#from app_stock.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.center(  # Usamos rx.box para asegurar que se ocupa todo el espacio
        rx.vstack(  # Usamos vstack para apilar los elementos verticalmente
            rx.heading(
                "Real time specs.",
                font_size=Size.MEDIUM.value,
                padding_bottom=Size.MEDIUM.value,
                color=TextColor.PRIMARY.value,
            ),
            rx.flex(
                rx.vstack(
                    rx.box(
                        rx.text("Productos registrados: 250"),
                        rx.text("Productos con bajo stock: 12"),
                        rx.text("Pedidos en proceso: 5"),
                        rx.text("Última sincronización: 18/01/2025 10:45 AM"),
                        class_name="nes-container is-dark with-title",  
                    ),  
                    align_items="center",  # Centra los elementos dentro del vstack
                    justify="center",      # Centra los elementos dentro del vstack
                ),
                flex_direction="column",  # Asegura que los elementos estén en columna
                align_items="center",     # Centra verticalmente dentro del flex
                justify="center",         # Centra horizontalmente dentro del flex
            ),
            padding_top=Size.BIG.value,
        ),
        width="100%",   # Asegura que ocupe todo el ancho disponible
        height="100%",  # Asegura que ocupe todo el alto disponible
        display="flex", # Aplica Flexbox al contenedor
        align_items="center",  # Centra los elementos verticalmente
        justify="center",      # Centra los elementos horizontalmente
    )

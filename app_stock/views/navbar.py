import reflex as rx
import app_stock.constants as constants
from app_stock.styles.styles import Size, Color
from app_stock.components.link_icon import link_icon
from app_stock.styles.colors import TextColor


#alto del navbar está siendo determinado dinámicamente por el tamaño de su contenido interno
def navbar() -> rx.Component:
    return rx.vstack( #pinta de manera horizontal
        rx.hstack( #apila de manera vertical
            rx.image(
                src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                alt="logo",
                width=Size.BIG.value,
                height=Size.BIG.value,
                #gap="1em",
            ),
            #rx.text(
            #    "MVP stock", size="3",
            #    color=TextColor.TERTIARY.value,
            #    ),
            rx.spacer(),
                link_icon(
                    "github", #nombre del link, debe ser el mismo que el nombre de la libreria de iconos
                    constants.GITHUB_URL,
                    size=Size.BIG.value,
                    #is-small, is-medium, y is-large
                ),
                link_icon(
                    "twitter",
                    constants.TWITTER_URL,
                    size=Size.BIG.value,
                ),
            align="center",
            width="100%",
            gap="1em", 
            
        ),
        #height="4em",  # Especifica un alto fijo
        bg=Color.SECONDARY.value, #background del navbar
        backdrop_filter="blur(3px)",  # Efecto de difuminado
        position="sticky", #navbar se queda fijo en la parte superior
        border_bottom=f"0.2em solid {Color.SECONDARY.value}", # linea navbar
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
        width="100%" 
    )
import reflex as rx
from .fonts import Font
from .colors import Color, TextColor   
from enum import Enum


MAX_WIDTH = "1000px"

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "5em"



STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {      
    "font-family": "'Press Start 2P', sans-serif",
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading:{
        "font-family": "'Press Start 2P', sans-serif",
        "color": TextColor.QUATERNARY.value,
    },
    rx.link:{
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.SECONDARY.value,
            "text_decoration": "none",
        },
    },
    
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)



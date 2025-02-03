import reflex as rx
import app_stock.constants as constants
import app_stock.styles.styles as styles
from app_stock.styles.styles import Size
from app_stock.styles.colors import TextColor
from app_stock.components.link_icon import button
from app_stock.routes import Route

STYLES = {
    
    "hero_title": {
        "font_size": "1.2em",
        "line_height": "0.9",
        "margin_bottom": "0.2em",
    },
    "hero_subtitle": {
        "font_size": "1.2em",
        "max_width": "600px",
        "margin_bottom": "2em",
    },
    "learn_button": {
        "background_color": "#003708",
        "color": "white",
        "padding": "12px 24px",
        "border_radius": "4px",
        "font_weight": "500",
        "_hover": {
            "opacity": 0.8,
        },
    },
    
    
}

def specs() -> rx.Component:
    #Lista con contenido único para cada tarjeta
    #card_contents = [
    #    {"title": "Gestión de proveedores", "content": "Registro de todos tus proveedores, su contacto, información, precios y condiciones de pago. Podrás tener una visión global de tus relaciones comerciales."},
    #    {"title": "Control de Stock", "content": "Control detallado de tus productos y materiales, verificando su disponibilidad y actualizando su stock en tiempo real."},
    #    {"title": "Gestión de almacenes", "content": "Podrás tener un registro de todos tus almacenes, ubicaciones de tus productos y cantidad de stock disponible."},
    #]
    
    #return rx.box(width="100%", height="2px", bg="white", margin="20px 0"),
    
    return rx.hstack(
        
        rx.vstack(
            rx.text(
                "Optimiza tu stock, impulsa tu negocio.", 
                style=STYLES["hero_title"], 
                color=TextColor.TERTIARY.value,
                margin_bottom="2em",
            ),
            rx.heading(
                "MVP'S\nStock",
                font_size=Size.BIG.value,
                margin_bottom="0.5em",
            ),
            rx.text(
                "CONTROL DETALLADO DE TUS PRODUCTOS Y MATERIALES, VERIFICANDO SU DISPONIBILIDAD Y ACTUALIZANDO SU STOCK EN TIEMPO REAL.",
                style=STYLES["hero_subtitle"],
                color=TextColor.TERTIARY.value,
                margin_bottom="2em",
            ),
            rx.text(
                "Conoce más sobre nuestro servicio.",
                color=TextColor.TERTIARY.value,
                padding_y=Size.SMALL.value,
                margin_bottom="0.2em",
            ),
            rx.box(
                button(
                    "#whitelist", #nombre del link, debe ser el mismo que el nombre de la libreria de iconos
                    constants.WHITELIST_URL,
                    size="is-small",
                    width=["100%", "200px"],  # 100% en móvil, 200px en desktop
                    height="40px",  # Alto fijo
                    #is-small, is-medium, y is-large
                ),
                button(
                    "/DEMO",
                    Route.DEMO_FRONT,
                    size="is-small",
                    width=["100%", "200px"],  # 100% en móvil, 200px en desktop
                    height="40px",  # Alto fijo
                ),
                #aplica un felxbox para que los botones se acomoden en columna en movil y en fila en desktop 
                display="flex",
                flex_direction=["column", "row"],  # Columna en móvil, fila en desktop
                justify_content="start",
                align_items="start",
                gap="2em",
                width="100%",
            ),
            align_items="start",
            justify="start", 
            width="100%",
        ),
        align_items="start",
        justify="start",
        padding_x=Size.VERY_BIG.value,
        padding_y=Size.BIG.value,
        width="100%",
    )
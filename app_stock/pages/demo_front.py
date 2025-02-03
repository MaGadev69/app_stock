import reflex as rx
from app_stock.styles.styles import STYLESHEETS, BASE_STYLE # Verifica que estas importaciones sean válidas
from app_stock.views.navbar import navbar  # Importa correctamente el componente navbar
from app_stock.views.header import header  # Importa correctamente el componente navbar
from app_stock.views.footer import footer  # Importa correctamente el componente navbar
from app_stock.views.specs import specs  # Importa correctamente el componente navbar
from app_stock.components.background import background_v2  # Importa correctamente el componente navbar
import app_stock.utils as utils
from app_stock.styles.colors import TextColor

@rx.page(
        route="demo_front",
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
)

def demo_front() -> rx.Component:
        return rx.box(
        background_v2(),
        rx.vstack(
                navbar(),
                rx.text("¡Esta es la demo!",color=TextColor.TERTIARY.value),
                footer(),
                width="100%",
                # Propiedades después de todos los bloques hijos
        ),
        position="relative",  # Contenedor principal con posicionamiento relativo
        # Propiedades después de todos los bloques hijos
        )
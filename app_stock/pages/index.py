import reflex as rx
from app_stock.styles.styles import STYLESHEETS, BASE_STYLE # Verifica que estas importaciones sean válidas
from app_stock.views.navbar import navbar  # Importa correctamente el componente navbar
from app_stock.views.header import header  # Importa correctamente el componente navbar
from app_stock.views.footer import footer  # Importa correctamente el componente navbar
from app_stock.views.specs import specs  # Importa correctamente el componente navbar
from app_stock.components.background import background_v2  # Importa correctamente el componente navbar
import app_stock.utils as utils


@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
)

def index() -> rx.Component:
        return rx.box(
        # utlis.lang es una función que retorna un script con el lenguaje de la página
        utils.lang(),
        background_v2(),
        rx.vstack(
                navbar(),
                specs(),
                header(),
                header(),
                header(),
                header(),
                header(),
                footer(),
                
                width="100%",
                # Propiedades después de todos los bloques hijos
        ),
        
        position="relative",  # Contenedor principal con posicionamiento relativo
        # Propiedades después de todos los bloques hijos
        )

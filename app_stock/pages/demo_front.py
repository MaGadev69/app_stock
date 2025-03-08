import reflex as rx
from app_stock.styles.styles import STYLESHEETS, BASE_STYLE # Verifica que estas importaciones sean válidas
from app_stock.styles.fonts import Font
from app_stock.views.navbar import navbar  # Importa correctamente el componente navbar
from app_stock.views.footer import footer  # Importa correctamente el componente navbar
from app_stock.components.background import background_v2  # Importa correctamente el componente navbar
import app_stock.utils as utils
from app_stock.styles.colors import TextColor
from app_stock.states.states import ProductoState
from app_stock.views.sidebar import sidebar_items

from app_stock.views.sidebar import sidebar_bottom_profile



#from app_stock.api.api import hello
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
                rx.flex(
                sidebar_bottom_profile(),  # O sidebar_items() para versión simple
                flex_direction=['row'],        
                ),

        
        
        rx.hstack(
                rx.input(
                placeholder="Nombre del producto",
                on_blur=ProductoState.set_name,
                ),
                rx.input(
                placeholder="Descripción",
                on_blur=ProductoState.set_description,
                ),
                rx.input(
                #placeholder="Precio",
                #type="number",
                #default_value=ProductoState.precio,
                #on_blur=ProductoState.set_price,
                ),
                rx.button(
                "Agregar Producto",
                #    on_click=ProductoState.add_product,
                ),
        ),
        rx.foreach(
                ProductoState.productos,
                lambda product: rx.box(
                #rx.text(product.nombre),
                #rx.text(product.description),
                #rx.text(product.price),
                rx.button(
                        "Eliminar",
                        #on_click=lambda: ProductoState.delete_product(product.id),
                )
                )
        ),
        footer(),
        width="100%",
        ),
        position="relative",
        )
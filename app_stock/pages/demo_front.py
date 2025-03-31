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


                rx.form(
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
                        placeholder="Precio",
                        on_blur=ProductoState.set_price,
                        ),
                        
                        rx.input(
                        value=ProductoState.nombre_proveedor,
                        on_change=ProductoState.buscar_proveedores,
                        placeholder="Buscar proveedor...",
                        ),
                        
                        rx.cond(
                        ProductoState.proveedores_sugeridos,
                        rx.vstack(
                                rx.foreach(
                                ProductoState.proveedores_sugeridos,
                                lambda proveedor: rx.button(
                                        proveedor.nombre,
                                        on_click=lambda p=proveedor: ProductoState.seleccionar_proveedor(
                                        p.id_proveedor, p.nombre
                                        ),
                                )
                                )
                        ),
                        rx.text("")
                        ),
                        
                        rx.input(
                        placeholder="Stock",
                        on_blur=ProductoState.set_stock,
                        ),
                        rx.input(
                        placeholder="Imagen",
                        on_blur=ProductoState.set_image,
                        ),
                        rx.input(
                        placeholder="Categoría",
                        on_blur=ProductoState.set_category,
                        ),
                        rx.select(
                        ["activo", "discontinuado", "en oferta"],
                        value=ProductoState.estado,
                        on_change=ProductoState.set_estado,
                        ),
                        rx.button(
                        "Agregar Producto",
                        on_click=ProductoState.agregar_producto,
                        
                        
                        ),
                ),
                reset_on_submit=True,
                
                ),



        footer(),
        width="100%",
        ),
        position="relative",
        )
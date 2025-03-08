# cuestiones basicas de reflex# https://www.youtube.com/watch?v=yFOCSl-OGTE
# https://www.radix-ui.com/

import reflex as rx
from app_stock.styles.styles import STYLESHEETS, BASE_STYLE # Verifica que estas importaciones sean válidas
#from app_stock.api.api import hello
from app_stock.pages.demo_front import demo_front
from app_stock.pages.index import index

class State(rx.State):
    """Define el estado de la aplicación"""
    

# Configuración de la aplicación
app = rx.App(
    stylesheets=STYLESHEETS,  # Define correctamente tus estilos CSS globales
    style=BASE_STYLE,  # Define un estilo base si es necesario
)
if __name__ == "__main__":
    app.compile()



app.add_page(index, route="/") 
app.add_page(demo_front, route="/demo_front")

#app.api.add_api_route("/hello",hello)
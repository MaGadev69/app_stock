
# cuestiones basicas de reflex
# https://www.youtube.com/watch?v=yFOCSl-OGTE
# https://www.radix-ui.com/



import reflex as rx
from app_stock.styles.styles import STYLESHEETS, BASE_STYLE # Verifica que estas importaciones sean válidas
#from app_stock.views.navbar import navbar  # Importa correctamente el componente navbar
#from app_stock.views.header import header  # Importa correctamente el componente navbar
#from app_stock.views.footer import footer  # Importa correctamente el componente navbar
#from app_stock.views.specs import specs  # Importa correctamente el componente navbar
#from app_stock.views.test import test  # Importa correctamente el componente navbar
#from app_stock.components.background import background_v2  # Importa correctamente el componente navbar

#from app_stock.pages.index import index 
#from app_stock.pages.demo_front import demo_front
# Con reflex run --loglevel debug se puede ver el log de la aplicación
class State(rx.State):
    """Define el estado de la aplicación"""


    
# Configuración de la aplicación
app = rx.App(
    stylesheets=STYLESHEETS,  # Define correctamente tus estilos CSS globales
    style=BASE_STYLE,  # Define un estilo base si es necesario
)
# Ejecuta el servidor Reflex
if __name__ == "__main__":
    app.compile()
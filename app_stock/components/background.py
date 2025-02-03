import reflex as rx

def background_v2():
    return rx.center(
        #rx.heading("Buridan UI", size="8", weight="bold", z_index="10"),
    
        background_size="20px 20px",
        background_image="radial-gradient(circle, hsl(0, 0%, 39%) 1px, transparent 1px), radial-gradient(circle, hsl(0, 0%, 45%) 1px, transparent 1px)",
        mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.5), hsl(0, 0%, 0%, 0))",
    
        width="100%",
        height="100vh",  # Ahora ocupa toda la altura de la pantalla
        position="fixed",  # Fondo fijo
        #top="0",           # Coloca el componente en la parte superior
        top="3.25rem",     # Desplaza el fondo hacia abajo
        left="0",          # Alinea a la izquierda
        z_index="-1",      # Colócalo detrás del contenido principal
    )
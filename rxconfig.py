import reflex as rx

config = rx.Config(
    app_name="app_stock",
    port=3000,  # Cambia el puerto según tu preferencia
    backend_port=8000,  # Puerto del backend
    cors_allow_all=True,
    #esta api es la que se va a usar el front, la misma viene de railway
    #api_url="https://appstock-production-132c.up.railway.app",
    # lo envie a build.sh
)
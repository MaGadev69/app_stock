import reflex as rx
#comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")
    


preview="app_stock/assets/magadev.jpg"


#index
index_title="Index mvp 2025"
index_description="Tu stock, tu información, tu control"

index_meta=[
    {"name": "title", "content": index_title},
    {"name": "description", "content": index_description}
]
#index_meta.extend(_meta)

#demo_front
demo_front_title="Demo mvp stock"
demo_front_description="Demo Front"

demo_front_meta=[
    {"name": "title", "content": demo_front_title},
    {"name": "description", "content": demo_front_description}
]
#demo_front_meta.extend(_meta)


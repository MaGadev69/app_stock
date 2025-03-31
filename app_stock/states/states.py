import reflex as rx
from sqlmodel import select
from datetime import datetime
from app_stock.models.models import Productos, Proveedores  # Importar modelos de la base de datos

# convenciones de Python (PEP 8) donde las clases usan CamelCase y las variables/atributos usan snake_case.

# Estado para manejar productos
class ProductoState(rx.State):
    productos: list[Productos] = []  # Lista de productos 
    nombre: str = ""  # Nombre del producto
    descripcion: str = ""  # Descripción del producto
    precio: float = 0.0  # Precio del producto
    #search field with autocomplete 1/2
    id_proveedor: int = 0  # ID del proveedor
    nombre_proveedor: str = ""  # Nombre del proveedor
    proveedores_sugeridos: list[Proveedores] = []  # Proveedores sugeridos
    #
    stock: int = 0  # Stock del producto
    imagen: str = ""  # Imagen del producto
    categoria: str = ""  # Categoría del producto
    estado: str = "activo"  # Estado del producto
    # Método para establecer el nombre del producto
    #on_blur requiere siempre un valor srt
    @rx.event
    def set_name(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.nombre = value
    # Método para establecer la descripción del producto
    @rx.event
    def set_description(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.descripcion = value
    # Método para establecer el precio del producto
    @rx.event
    def set_price(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.precio = float(value)
    
    #search field with autocomplete 2/2
    # Método para buscar proveedores a medida que se escribe

    @rx.event
    def buscar_proveedores(self, value: str):
        self.nombre_proveedor = value
        with rx.session() as session:
            query = select(Proveedores).where(
                Proveedores.nombre.ilike(f"%{value}%")
            ).limit(5)
            self.proveedores_sugeridos = session.exec(query).all()





    # Método para seleccionar un proveedor de la lista
    @rx.event
    def seleccionar_proveedor(self, id_proveedor: int, nombre: str):
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre  # Se muestra el nombre en el input
        self.proveedores_sugeridos = []  # Se limpia la lista de sugerencias




    @rx.event
    def set_stock(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.stock = int(value)
    @rx.event
    def set_image(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.imagen = value
    @rx.event
    def set_category(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.categoria = value
    @rx.event
    def set_state(self, value: str):
        if value == "":
            return  # Handle empty string case
        self.estado = value


    # Método para agregar un producto
    @rx.event
    def agregar_producto(self):
        with rx.session() as session:
            session.add(
                Productos(
                    nombre=self.nombre,
                    descripcion=self.descripcion,
                    precio=self.precio,
                    id_proveedor=self.id_proveedor,
                    stock=self.stock,
                    imagen=self.imagen,
                    categoria=self.categoria,
                    estado=self.estado,
                    fecha_creacion=datetime.now(),  # Fecha actual
                    fecha_ultima_modificacion=datetime.now()  # Fecha actual
                )
            )
            session.commit()
            self.obtener_productos()  # Actualizar la lista de productos

    # Método para obtener productos
    @rx.event
    def obtener_productos(self):
        with rx.session() as session:
            self.productos = session.exec(Productos.select()).all()

    # Método para eliminar un producto
    @rx.event
    def eliminar_producto(self, id_producto: int):
        with rx.session() as session:
            producto = session.exec(
                Productos.select().where(Productos.id_producto == id_producto)
            ).first()
            if producto:
                session.delete(producto)
                session.commit()
                self.obtener_productos()  # Actualizar la lista de productos

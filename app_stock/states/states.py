import reflex as rx
from datetime import datetime
from app_stock.models.models import Productos
# convenciones de Python (PEP 8) donde las clases usan CamelCase y las variables/atributos usan snake_case.
# Estado para manejar productos
class ProductoState(rx.State):
    productos: list[Productos] = []  # Lista de productos 
    nombre: str = ""  # Nombre del producto
    descripcion: str = ""  # Descripción del producto
    precio: float = 0.0  # Precio del producto
    id_proveedor: int = 0  # ID del proveedor
    stock: int = 0  # Stock del producto
    categoria: str = ""  # Categoría del producto
    estado: str = "activo"  # Estado del producto

    # Método para establecer el nombre del producto
    @rx.event
    def set_name(self, value: str):
        self.nombre = value

    # Método para establecer la descripción del producto
    @rx.event
    def set_description(self, value: str):
        self.descripcion = value

    # Método para establecer el precio del producto
    @rx.event
    def set_price(self, value: float):
        self.precio = value

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

import datetime
import sqlmodel
import sqlalchemy
import reflex as rx


class Productos(rx.Model, table=True):
    id_producto: int = sqlmodel.Field(primary_key=True)
    nombre: str
    descripcion: str
    precio: float
    id_proveedor: int = sqlmodel.Field(foreign_key="proveedores.id_proveedor")
    stock: int
    imagen: str = sqlmodel.Field(default="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",)
    fecha_creacion: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "fecha_creacion",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    fecha_ultima_modificacion: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "fecha_ultima_modificacion",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    categoria: str
    estado: str  # activo, discontinuado, en oferta


class Proveedores(rx.Model, table=True):
    id_proveedor: int = sqlmodel.Field(primary_key=True)
    nombre: str
    direccion: str
    telefono: str
    email: str
    estado: str  # activo, inactivo
    fecha_registro: datetime.datetime = sqlmodel.Field(
        default=datetime.datetime.utcnow
    )


class Remitos(rx.Model, table=True):
    id_remito: int = sqlmodel.Field(primary_key=True)
    fecha: datetime.date
    id_sucursal: int = sqlmodel.Field(foreign_key="sucursales.id_sucursal")
    id_empleado: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    estado: str  # pendiente, completado, anulado
    id_sucursal_origen: int = sqlmodel.Field(foreign_key="sucursales.id_sucursal")
    id_sucursal_destino: int = sqlmodel.Field(foreign_key="sucursales.id_sucursal")


class Sucursales(rx.Model, table=True):
    id_sucursal: int = sqlmodel.Field(primary_key=True)
    nombre: str
    direccion: str
    telefono: str
    ciudad: str
    codigo_postal: str
    fecha_apertura: datetime.date
    horario_apertura: datetime.datetime
    estado: str  # activo, inactivo


class Usuarios(rx.Model, table=True):
    id_usuario: int = sqlmodel.Field(primary_key=True)
    nombre_usuario: str
    apellido_usuario: str
    contraseña: str
    id_sucursal: int = sqlmodel.Field(foreign_key="sucursales.id_sucursal")
    fecha_creacion: datetime.datetime = sqlmodel.Field(
        default=datetime.datetime.utcnow
    )
    fecha_ultima_sesion: datetime.datetime = sqlmodel.Field(
        default=datetime.datetime.utcnow
    )
    estado: str  # activo, inactivo
    rol: str  # admin, empleado


class RemitosProductos(rx.Model, table=True):
    id_remito: int = sqlmodel.Field(foreign_key="remitos.id_remito", primary_key=True)
    id_producto: int = sqlmodel.Field(foreign_key="productos.id_producto", primary_key=True)
    cantidad: int
    precio: float

import reflex as rx
#from datetime import datetime
# Definir el Modelo: Crea un modelo para los productos en un archivo adecuado
import datetime
import sqlmodel
import sqlalchemy




class Productos(rx.Model, table=True):
    id_producto: int = sqlmodel.Field(primary_key=True)
    nombre: str
    descripcion: str
    precio: float
    id_proveedor: int
    stock: int
    imagen: str
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

class proveedores(rx.Model, table=True):
    id_proveedor: int = sqlmodel.Field(primary_key=True)
    nombre: str
    direccion: str
    telefono: str
    email: str
    #fecha_registro: datetime  # Cambiado a datetime
    estado: str  # activo, inactivo

class remitos(rx.Model, table=True):
    id_remito: int = sqlmodel.Field(primary_key=True)
    #fecha: datetime.date
    id_sucursal: int  # Cambiado a int
    id_empleado: int
    estado: str  # pendiente, completado, anulado
    id_sucursal_origen: int  # Cambiado a int
    id_sucursal_destino: int  # Cambiado a int

class sucursales(rx.Model, table=True):
    id_sucursal: int = sqlmodel.Field(primary_key=True)
    nombre: str
    direccion: str
    telefono: str
    ciudad: str
    codigo_postal: str
    #fecha_apertura: datetime.date
    horario_apertura: str  # Cambiado a str
    estado: str  # activo, inactivo

class usuarios(rx.Model, table=True):
    id_usuario: int = sqlmodel.Field(primary_key=True)
    nombre_usuario: str
    contraseña: str
    id_sucursal: int  # Cambiado a int
    apellido_usuario: str
    #fecha_creacion: datetime  # Cambiado a datetime
    #fecha_ultima_sesion: datetime  # Cambiado a datetime
    estado: str  # activo, inactivo
    rol: str  # admin, empleado


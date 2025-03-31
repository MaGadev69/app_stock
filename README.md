Documentación de la Base de Datos 📌
📂 Descripción General
Esta base de datos gestiona información de productos, proveedores, sucursales, usuarios y remitos (traslados de mercadería entre sucursales). Se estructura de manera que permite realizar un seguimiento del stock y movimientos de productos.

📑 Tablas y Relaciones
🏢 Sucursales
id_sucursal (PK): Identificador único de la sucursal.

nombre: Nombre de la sucursal.

dirección, teléfono, ciudad, código_postal: Datos de contacto.

fecha_apertura, horario_apertura: Fechas y horarios de operación.

estado: Estado de la sucursal (activo/inactivo).

🔗 Relación: Una sucursal puede estar asociada a muchos usuarios y puede ser origen o destino en remitos.

👥 Usuarios
id_usuario (PK): Identificador único del usuario.

nombre_usuario, apellido_usuario: Datos personales.

contraseña: Clave encriptada para acceso.

id_sucursal (FK): Relación con la sucursal donde trabaja.

fecha_creación, fecha_última_sesión: Fechas de actividad.

estado: Puede ser 'activo' o 'inactivo'.

rol: Puede ser 'admin' o 'empleado'.

🔗 Relación: Un usuario puede registrar remitos.

🚛 Proveedores
id_proveedor (PK): Identificador del proveedor.

nombre, dirección, teléfono, email: Información de contacto.

fecha_registro: Fecha en que se registró en el sistema.

estado: Activo o inactivo.

🔗 Relación: Un proveedor puede suministrar muchos productos.

📦 Productos
id_producto (PK): Identificador del producto.

nombre, descripción, precio: Datos del producto.

id_proveedor (FK): Relación con el proveedor.

stock: Cantidad disponible.

imagen: Ruta de imagen del producto.

estado: 'activo', 'discontinuado' o 'en oferta'.

categoria: Categoría del producto.

🔗 Relación: Un producto puede estar en muchos remitos_productos.

📄 Remitos
id_remito (PK): Identificador del remito.

fecha: Fecha del traslado.

id_sucursal (FK): Sucursal responsable del remito.

id_empleado (FK): Usuario que creó el remito.

estado: 'pendiente', 'completado' o 'anulado'.

id_sucursal_origen (FK): Sucursal de donde salió la mercadería.

id_sucursal_destino (FK): Sucursal a donde llega la mercadería.

🔗 Relación: Un remito puede incluir muchos productos.

📜 Remitos_Productos (Intermedia)
id_remito (FK): Relación con la tabla remitos.

id_producto (FK): Relación con la tabla productos.

cantidad: Cantidad trasladada.

precio: Precio unitario del producto en el momento del traslado.

🔗 Relación: Relaciona productos con remitos en un esquema de muchos a muchos.

📂Esta base de datos está diseñada para gestionar un flujo completo de stock y logística. Con este esquema se pueden:
-Registrar y gestionar sucursales, empleados y proveedores.
-Mantener un catálogo de productos y su stock.
-Administrar traslados de mercadería entre sucursales mediante remitos.
-Optimizar consultas con índices estratégicos.
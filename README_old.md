Documentación de la Base de Datos

📂 Tablas y sus Descripciones

🛒 productos

Contiene los productos disponibles en el sistema.

id_producto (INT, PRIMARY KEY) - Identificador único del producto.

nombre (VARCHAR(100)) - Nombre del producto.

descripcion (TEXT) - Descripción del producto.

precio (DECIMAL(10,2)) - Precio del producto.

id_proveedor (INT, FOREIGN KEY) - Relación con proveedores.

stock (INT) - Cantidad disponible en inventario.

imagen (VARCHAR(100)) - URL o nombre de la imagen del producto.

fecha_creacion (DATETIME) - Fecha de creación del registro.

fecha_ultima_modificacion (DATETIME) - Última fecha de modificación.

categoria (VARCHAR(100)) - Categoría del producto.

estado (ENUM) - Estado del producto (activo/inactivo).

🚚 proveedores

Registra la información de los proveedores de productos.

id_proveedor (INT, PRIMARY KEY) - Identificador único del proveedor.

nombre (VARCHAR(100)) - Nombre del proveedor.

direccion (VARCHAR(255)) - Dirección del proveedor.

telefono (VARCHAR(50)) - Número de contacto.

email (VARCHAR(100)) - Correo electrónico.

fecha_registro (DATETIME) - Fecha en la que se registró el proveedor.

estado (ENUM) - Estado del proveedor.

👤 usuarios

Registra a los usuarios del sistema.

id_usuario (INT, PRIMARY KEY) - Identificador único del usuario.

nombre_usuario (VARCHAR(100)) - Nombre de usuario.

contraseña (VARCHAR(100)) - Contraseña encriptada.

id_sucursal (VARCHAR(30), FOREIGN KEY) - Relación con sucursales.

apellido_usuario (VARCHAR(100)) - Apellido del usuario.

fecha_creacion (DATETIME) - Fecha de creación del usuario.

fecha_ultima_sesion (DATETIME) - Fecha de última sesión del usuario.

estado (ENUM) - Estado del usuario.

rol (ENUM) - Rol del usuario (admin, empleado, etc.).

🏢 sucursales

Registra las sucursales del sistema.

id_sucursal (VARCHAR(30), PRIMARY KEY) - Identificador único de la sucursal.

nombre (VARCHAR(100)) - Nombre de la sucursal.

direccion (VARCHAR(255)) - Dirección de la sucursal.

telefono (VARCHAR(50)) - Teléfono de contacto.

ciudad (VARCHAR(100)) - Ciudad donde está ubicada.

codigo_postal (VARCHAR(10)) - Código postal.

fecha_apertura (DATE) - Fecha en que se abrió la sucursal.

horario_apertura (VARCHAR(50)) - Horario de apertura.

estado (ENUM) - Estado de la sucursal.

📦 remitos

Registra los movimientos de mercadería entre sucursales.

id_remito (INT, PRIMARY KEY) - Identificador único del remito.

fecha (DATE) - Fecha de emisión del remito.

id_sucursal (VARCHAR(30), FOREIGN KEY) - Relación con sucursales.

id_empleado (INT, FOREIGN KEY) - Relación con usuarios.

estado (ENUM) - Estado del remito (pendiente, enviado, recibido).

id_sucursal_origen (VARCHAR(30), FOREIGN KEY) - Sucursal de origen.

id_sucursal_destino (VARCHAR(30), FOREIGN KEY) - Sucursal de destino.

🔄 remitos_productos

Registra los productos incluidos en los remitos.

id_remito (INT, FOREIGN KEY) - Relación con remitos.

id_producto (INT, FOREIGN KEY) - Relación con productos.

cantidad (INT) - Cantidad de productos enviados.

precio (DECIMAL(10,2)) - Precio unitario del producto en el remito.

🔗 Relaciones entre Tablas

productos tiene un id_proveedor que referencia a proveedores.

usuarios tiene un id_sucursal que referencia a sucursales.

remitos tiene un id_sucursal, id_sucursal_origen y id_sucursal_destino que referencian a sucursales.

remitos tiene un id_empleado que referencia a usuarios.

remitos_productos relaciona remitos y productos.

⚙️ Operaciones Disponibles

Esta base de datos permite realizar diversas operaciones para la gestión de stock y movimientos de mercadería:

🛍️ Productos

Agregar nuevos productos.

Modificar información de productos existentes.

Eliminar productos.

Consultar stock disponible.

🏭 Proveedores

Registrar nuevos proveedores.

Actualizar datos de proveedores.

Eliminar proveedores inactivos.

Consultar lista de proveedores.

👥 Usuarios

Crear nuevos usuarios.

Modificar datos de usuarios.

Cambiar estado de usuarios (activo/inactivo).

Gestionar roles y permisos.

🏬 Sucursales

Registrar nuevas sucursales.

Modificar información de sucursales.

Eliminar sucursales (si no tienen operaciones asociadas).

Consultar información de sucursales.

📑 Remitos

Generar nuevos remitos.

Asignar productos a los remitos.

Registrar envíos entre sucursales.

Cambiar estado de remitos (pendiente, enviado, recibido).

Consultar historial de remitos.
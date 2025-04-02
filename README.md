# Coleon
Descripción:
Coleon es una aplicación diseñada para coleccionistas que buscan organizar y planificar sus colecciones de manera eficiente. Permite a los usuarios crear, personalizar y seguir el progreso de sus colecciones, ya sean de sellos, discos, cartas u otros artículos de interés.
La aplicación ofrece una interfaz basada en tablas personalizables, donde cada artículo ocupa una fila y el usuario puede agregar columnas personalizadas para registrar la información que necesite, como precio, fecha de adquisición, origen, tienda, imágenes y más.  
Además, Coleon genera gráficos automáticamente para visualizar el progreso de la colección, el dinero gastado, la evolución de precios y otros análisis relevantes. También permite compartir esquemas de colección con otros usuarios y exportar datos en distintos formatos. 

## Funcionalidades principales:

Generación de gráficos automáticos: Si la colección tiene columnas predeterminadas como “precio” o “estado”, se generarán gráficos como:

- "Productos más caros"
- "Histórico de compras"
- "Progreso de la colección"

Creación de columnas personalizadas: Los usuarios pueden añadir columnas con distintos tipos de datos:
- Texto (string)
- Número (number)
- Fecha (date)
- Estado (boolean o enum)

Vista en tarjetas y tabla: El usuario puede alternar entre una vista en tabla o en tarjetas, ideal para colecciones visuales.

Exportación de colecciones: Se podrá exportar en formato CSV para facilitar el intercambio y respaldo de datos.

Filtros avanzados: Permite filtrar la colección por cualquier columna.

Gestión de usuarios y seguridad: Registro, inicio de sesión con contraseña y acceso seguro a colecciones personales.

Añadir y eliminar artículos: Administración sencilla con paginación para colecciones grandes.

Verificación de enlaces de imágenes: Evita imágenes rotas al validar URLs.

Notificaciones antes de eliminar datos sensibles: Alertas antes de eliminar artículos o columnas con muchos datos.


## Tecnologías utilizadas:

- Backend: Python con Django
- Base de datos: SQL con almacenamiento JSON (para columnas personalizadas)
- Frontend: HTML y CSS

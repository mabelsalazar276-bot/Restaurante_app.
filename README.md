# Datos Informativos
**Estudiante:** Mabela del Cisne Salazar Ren 
**Materia:** Programación Orientada a Objetos  
**Tarea semana 9:** Proyecto Restaurant

# Aplicación para Administración y Control Gourmet (Semana 9)

Este proyecto consiste en la evolución estructurada del sistema `restaurante_app`. El diseño implementa una arquitectura limpia separada por capas autónomas de abstracción (módulos y paquetes) y aplica de forma coherente las cuatro colecciones esenciales de Python.

## 🛠️ Organización del Software (Módulos)

El código fuente respeta la estructura modular estricta exigida para el proyecto:

*   **`modelos/`**: Capa estructural que alberga las clases conceptuales del dominio del problema.
    *   `producto.py`: Contiene la clase `Producto` que maneja propiedades lógicas y financieras (código, nombre, categoría y precio).
    *   `usuario.py`: Contiene la clase `Usuario` que representa la información general de las personas del ecosistema (identificación, nombre, correo y rol).
*   **`servicios/`**: Capa operativa encargada de la lógica de negocio.
    *   `restaurante.py`: Contiene la clase `Restaurante`, encargada de administrar las colecciones, registros, búsquedas, actualizaciones y eliminaciones.
*   **`main.py`**: Punto de arranque que interactúa con el usuario, coordina el menú de consola mediante funciones y delega las operaciones al servicio.

## 📊 Justificación Teórica de las Estructuras de Datos

Cada una de las cuatro estructuras de Python cumple una función concreta y justificable dentro del programa:

1.  **Listas (`list`)**: Implementadas en `servicios/restaurante.py` como `self._productos` y `self._usuarios`. Son las colecciones dinámicas ideales para almacenar secuencialmente objetos de tipo `Producto` y `Usuario`, permitiendo realizar registros, listados globales y eliminaciones de forma ordenada.
2.  **Tuplas (`tuple`)**: Implementadas en `main.py` como `OPCIONES_MENU` y en `Usuario` como `ROLES_PERMITIDOS`. Al ser colecciones inmutables (de solo lectura), garantizan que los datos estables de la interfaz y las reglas del negocio no se alteren accidentalmente durante la ejecución.
3.  **Diccionarios (`dict`)**: Implementado en `main.py` como `ACCIONES_MENU`. Establece una relación estructurada clave -> valor para asociar los caracteres de selección del menú ("1", "2", etc.) directamente con sus respectivas funciones de control, eliminando estructuras repetitivas `if-elif`.
4.  **Conjuntos (`set`)**: Utilizado en el método `obtener_categorias_unicas()`. Aprovecha la propiedad nativa de los conjuntos de prohibir elementos duplicados para extraer y presentar de forma limpia un consolidado de las categorías existentes en el inventario.

## ⚙️ Características Técnicas y Buenas Prácticas

*   **Encapsulamiento de Colecciones**: Las listas internas del servicio están protegidas (`self._productos` y `self._usuarios`). El servicio retorna copias explícitas mediante el uso de `.copy()`, evitando que `main.py` modifique las colecciones internas directamente.
*   **Manejo de Excepciones**: Implementación de bloques `try-except` para capturar errores de tipo (`ValueError`) en ingresos numéricos desde consola, evitando que el programa se detenga bruscamente ante datos incorrectos.
*   **Tipado Estricto**: Se aplicaron anotaciones de tipos de datos en la firma de todos los constructores, métodos y funciones para mejorar la legibilidad y mantenimiento del código.
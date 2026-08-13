# Bitácora de Desarrollo - Proyecto Gourmet (Semana 9)

**Desarrollador del Software:** Mabela del Cisne Salazar Ren  
**Asignatura Académica:** Programación Orientada a Objetos  
**Período de Evaluación:** Tarea Práctica 9  

---

## 🏛️ Diseño Arquitectural y Paquetes

La aplicación `restaurante_app` se ha construido bajo un esquema de segmentación modular estricta. Las responsabilidades del sistema se dividen de la siguiente manera:

*   **Paquete `modelos`**: Contiene los moldes de datos puros. El archivo `producto.py` estructura las variables de catálogo (código numérico, descripción, grupo y costo), mientras que `usuario.py` gestiona la información de identificación, nombres, correos y credenciales de acceso.
*   **Paquete `servicios`**: Implementa la lógica de control en `restaurante.py`. Este módulo actúa como el motor del sistema, centralizando la manipulación segura de las bases de datos en memoria (altas, bajas, búsquedas y modificaciones).
*   **Raíz `main.py`**: Es el despachador de la interfaz de usuario en consola. Se encarga exclusivamente de la captura de datos por teclado (`input`), el despliegue del menú y la derivación de comandos hacia el motor del servicio.

---

## 💾 Implementación Funcional de Estructuras de Datos

Para resolver las necesidades operacionales del negocio gastronómico, se integraron cuatro colecciones nativas, explotando sus ventajas técnicas particulares:

1.  **Colecciones Lineales (`list`)**: Declaradas bajo los identificadores privados `self._productos` y `self._usuarios`. Al ser estructuras dinámicas y mutables, son perfectas para mantener el inventario base y el padrón de usuarios, permitiendo la inserción inversa de objetos en tiempo de ejecución.
2.  **Registros Inmutables (`tuple`)**: Utilizadas para salvaguardar arreglos de solo lectura que deben permanecer constantes durante toda la sesión, como el catálogo estático de perfiles de usuario (`ROLES_PERMITIDOS`) y las líneas de texto indexadas que componen el menú de la terminal.
3.  **Mapeos Indexados (`dict`)**: Aplicados en `ACCIONES_MENU` como un diccionario de enrutamiento. Asocia de forma directa la opción elegida por el usuario con la referencia en memoria de la función encargada de procesarla, reemplazando con éxito las estructuras anidadas de bifurcación condicional.
4.  **Estructuras de Filtrado (`set`)**: El método de extracción de categorías consolida los nombres de los grupos alimentarios dentro de un conjunto. Al omitir por definición los elementos repetidos, actúa como un depurador nativo para listar términos únicos del inventario de forma inmediata.

---

## 🛡️ Protocolos de Seguridad y Calidad del Código

*   **Aislamiento del Estado (Encapsulamiento)**: Las variables de colección del servicio están protegidas del exterior. Cada consulta externa obliga al sistema a emitir una réplica exacta (`.copy()`), impidiendo alteraciones externas accidentales desde la interfaz de usuario.
*   **Contención de Fallos (Excepciones)**: Los flujos de captura numérica están blindados con capturadores `try-except` orientados a anomalías de tipo `ValueError`. Si se detectan cadenas de texto en campos financieros o de códigos, la aplicación lo reporta de forma limpia sin interrumpir la experiencia.
*   **Especificación de Contratos (Tipado)**: Cada constructor, rutina y argumento contiene anotaciones de tipo estricto, facilitando el mantenimiento a largo plazo y la legibilidad del código fuente.

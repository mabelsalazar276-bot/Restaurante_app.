import sys
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

sistema: Restaurante = Restaurante()

OPCIONES_MENU: tuple[str, ...] = (
    " [1] Registrar producto",
    " [2] Buscar producto",
    " [3] Actualizar producto",
    " [4] Eliminar producto",
    " [5] Listar productos",
    " _____________________________________",
    " [6] Registrar usuario",
    " [7] Listar usuarios",
    " _____________________________________",
    " [8] Mostrar categorías",
    " [9] Salir"
)

def mostrar_menu() -> None:
    print("\n _____________________________________")
    print("        SISTEMA DE RESTAURANTE        ")
    print(" _____________________________________")
    for opcion in OPCIONES_MENU:
        print(opcion)

def opc_registrar_producto() -> None:
    try:
        cod: int = int(input("Ingrese matrícula/código numérico: "))
        nom: str = input("Descripción comercial del producto: ")
        cat: str = input("Grupo/Categoría (Plato o Bebida): ").strip().capitalize()
        pre: float = float(input("Arancel/Precio establecido: $"))
        
        if sistema.agregar_producto(Producto(cod, nom, cat, pre)):
            print(">> Confirmación: Registro completado con éxito.")
        else:
            print(">> Advertencia: La matrícula numérica ya consta en el sistema.")
    except ValueError:
        print(">> Error crítico: Formato numérico incorrecto en el ingreso.")

def opc_buscar_producto() -> None:
    try:
        cod: int = int(input("Ingrese código de búsqueda: "))
        producto = sistema.buscar_producto(cod)
        if producto:
            print(f"\nResultado de la consulta:\n{producto}")
        else:
            print(">> Alerta: No se localizó ningún elemento con ese código.")
    except ValueError:
        print(">> Error crítico: Tipo de dato no válido.")

def opc_actualizar_producto() -> None:
    try:
        cod: int = int(input("Ingrese código del producto a modificar: "))
        if sistema.buscar_producto(cod):
            nom: str = input("Nuevo nombre comercial: ")
            cat: str = input("Nueva categoría asignada: ").strip().capitalize()
            pre: float = float(input("Nuevo valor asignado: $"))
            if sistema.actualizar_producto(cod, nom, cat, pre):
                print(">> Confirmación: Registro modificado correctamente.")
        else:
            print(">> Alerta: El elemento indicado no se encuentra en el catálogo.")
    except ValueError:
        print(">> Error: Entrada de datos no compatible.")

def opc_eliminar_producto() -> None:
    try:
        cod: int = int(input("Código del producto a remover: "))
        if sistema.eliminar_producto(cod):
            print(">> Confirmación: Producto removido del inventario.")
        else:
            print(">> Alerta: Matrícula de producto no encontrada.")
    except ValueError:
        print(">> Error numérico detectado.")

def opc_listar_productos() -> None:
    print("\n--- INVENTARIO GENERAL DE EXISTENCIAS ---")
    productos: list[Producto] = sistema.obtener_todos_productos()
    if not productos:
        print("El catálogo actual está vacío.")
    for p in productos:
        print(p)

def opc_registrar_usuario() -> None:
    try:
        ide: int = int(input("Número de credencial/ID: "))
        nom: str = input("Nombre y apellido del usuario: ")
        cor: str = input("Dirección de correo electrónico: ")
        print(f"Perfiles admitidos en la base: {Usuario.ROLES_PERMITIDOS}")
        rol: str = input("Escriba el perfil asignado: ").strip().capitalize()
        
        if sistema.registrar_usuario(Usuario(ide, nom, cor, rol)):
            print(">> Confirmación: Cuenta registrada de forma exitosa.")
        else:
            print(">> Advertencia: Identificación o correo ya registrados en la base.")
    except ValueError as e:
        print(f">> Error en reglas: {e}")

def opc_listar_usuarios() -> None:
    print("\n--- BASE DE USUARIOS DEL SISTEMA ---")
    usuarios: list[Usuario] = sistema.obtener_todos_usuarios()
    if not usuarios:
        print("No constan perfiles cargados en el sistema.")
    for u in usuarios:
        print(u)

def opc_mostrar_categorias() -> None:
    print("\n--- GRUPOS Y CATEGORÍAS REGISTRADAS ---")
    categorias: set[str] = sistema.obtener_categorias_unicas()
    if not categorias:
        print("No se registran datos para procesar conjuntos.")
    for cat in categorias:
        print(f" -> {cat}")

def opc_salir() -> None:
    print("\n[!] Finalizando ejecución del software de control. Buen día Mariuxi.")
    sys.exit()

ACCIONES_MENU: dict[str, callable] = {
    "1": opc_registrar_producto,
    "2": opc_buscar_producto,
    "3": opc_actualizar_producto,
    "4": opc_eliminar_producto,
    "5": opc_listar_productos,
    "6": opc_registrar_usuario,
    "7": opc_listar_usuarios,
    "8": opc_mostrar_categorias,
    "9": opc_salir
}

def main() -> None:
    sistema.agregar_producto(Producto(101, "Corte de Lomo Fino", "Plato", 14.99))
    sistema.agregar_producto(Producto(202, "Té Helado Supremo", "Bebida", 1.99))
    sistema.registrar_usuario(Usuario(2202, "Mabela Salazar", "mabela@gmail.com", "Administrador"))

    while True:
        mostrar_menu()
        opcion: str = input("Escriba el comando a ejecutar (1-9): ").strip()
        
        if opcion in ACCIONES_MENU:
            ACCIONES_MENU[opcion]()  
        elif opcion not in (" _____________________________________"):
            print(">> Error: Selección fuera del rango válido (1-9).")

if __name__ == "__main__":
    main()

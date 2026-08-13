from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:
        self._productos: list[Producto] = []  
        self._usuarios: list[Usuario] = []   

    def agregar_producto(self, producto: Producto) -> bool:
        if any(item.codigo == producto.codigo for item in self._productos):
            return False
        self._productos.insert(0, producto)
        return True

    def buscar_producto(self, codigo: int) -> Producto | None:
        for item in self._productos:
            if item.codigo == codigo:
                return item
        return None

    def actualizar_producto(self, codigo: int, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        elemento = self.buscar_producto(codigo)
        if elemento:
            elemento.nombre = nuevo_nombre
            elemento.categoria = nueva_categoria
            elemento.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: int) -> bool:
        elemento = self.buscar_producto(codigo)
        if elemento:
            self._productos.remove(elemento)
            return True
        return False

    def obtener_todos_productos(self) -> list[Producto]:
        return self._productos.copy()

    def obtener_categorias_unicas(self) -> set[str]:
        registros_unicos: set[str] = set()
        for item in self._productos:
            registros_unicos.add(item.categoria)
        return registros_unicos

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if any(u.identificacion == usuario.identificacion or u.correo == usuario.correo for u in self._usuarios):
            return False
        self._usuarios.insert(0, usuario)
        return True

    def buscar_usuario(self, identificacion: int) -> Usuario | None:
        for user in self._usuarios:
            if user.identificacion == identificacion:
                return user
        return None

    def eliminar_usuario(self, identificacion: int) -> bool:
        user = self.buscar_usuario(identificacion)
        if user:
            self._usuarios.remove(user)
            return True
        return False

    def obtener_todos_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()
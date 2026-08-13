class Usuario:
    ROLES_PERMITIDOS: tuple[str, ...] = ("Administrador", "Cliente", "Mesero")

    def __init__(self, identificacion: int, nombre: str, correo: str, rol: str) -> None:
        self.identificacion: int = identificacion
        self.nombre: str = nombre
        self.correo: str = correo
        
        if rol not in self.ROLES_PERMITIDOS:
            raise ValueError(f"Rol inválido. Roles permitidos: {self.ROLES_PERMITIDOS}")
        self.rol: str = rol

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | {self.nombre} - {self.rol} ({self.correo})"
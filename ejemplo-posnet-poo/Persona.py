class Persona:
    
    def __init__(self, DNI, nombre, apellido, telefono, email) -> None:
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        
    def nombre_completo(self):
        return f"{self.nombre} , {self.apellido}"
    
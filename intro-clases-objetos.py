# Definir clases (cuidar la indentación, que es lo que determina la pertenencia a una clase)
class Persona: #esto no es un objeto, es una clase
    #Los atributos que aparezcan acá son de clase y no de instancia (es decir, de objeto); todos los objetos de esta clase tendrán los atributos detallados acá
    cant_ojos = 2
    
    #Constructor de objetos de la clase Persona - Primer método
    
    """def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    """
    
    #Constructor de objetos de la clase Persona - Segundo método (__init__)
    def __init__(self, nombre, apellido, edad, numero, nacionalidad, gano_mundial):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.numero = numero
        self.nacionalidad = nacionalidad
        self.gano_mundial = gano_mundial
    
    #Creación de métodos en una clase, para todos los objetos de esta clase
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años") #"self" se usa para referenciar un objeto de la misma clase en donde estoy creando el método (es como el "this" en Java)
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self) -> str: #convierte el objeto a cadena (toString en Java)
        return f"nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}, numero: {self.numero}, nacionalidad: {self.nacionalidad}, ganó mundial: {self.gano_mundial}"
#Termina la clase Persona

#Instanciar un objeto
leo = Persona("Lionel", "Messi", 35, 10, "Argentina", True) #Así creo un objeto a partir de un constructor
fideo = Persona("Angel", "Di Maria", 37, 7, "Argentina", True)

#Asignación de atributos a un objeto
"""
leo.nombre = "Lionel"
leo.apellido = "Messi"
leo.edad = 35
leo.numero = 10
leo.nacionalidad = "Argentina"
leo.gano_mundial = True
"""

leo.saludar() #Llamo al método "saludar()" para el objeto leo desde el main
print(leo.nombre_completo()) #Imprimo el método "nombre_completo()" para el objeto leo desde el main

print(leo) #Sin el método __str__, esto da un valor que es el id de objeto guardado por Python; pero se puede ver los datos del objeto en la consola en lugar de ver el id


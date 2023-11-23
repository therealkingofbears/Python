from typing import Any


class Persona:
    
    def __init__(self, nombre, edad): #Constructor --aunque por convención para ser un atributo privado debería ser "self._nombre = _nombre" y "self._edad = _edad"
        self.__nombre = nombre
        self.__edad = edad
    
    @nombre.setter
    def nombre(self, nuevo_nombre): #Setter (nombre) 
        self.nombre = nuevo_nombre
    
    @edad.setter
    def edad(self, nueva_edad):
        self.edad = nueva_edad
            
    @property
    def nombre(self): #Getter (nombre)
        return self.nombre
        
    @property
    def edad(self):
        return self.edad
    
    def __str__(self): #Método toString para imprimir el objeto como cadena
        return f"nombre: {self.nombre}, edad: {self.edad}"
    
    def es_mayor_de_edad(self, mayor):
        if self.edad >= 18:
            mayor = True
        else:
            mayor = False
        return mayor

    def es_mayor_que(self, mayor):
        p1 = Persona()
        
        if p1.edad > self.edad:
            mayor = p1.edad
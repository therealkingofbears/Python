class TarjetaDeCredito:
    
    def __init__(self, entidad_bancaria, numero, titular):
        self.__entidad_bancaria = entidad_bancaria #Para que los atributos sean privados, se antepone al nombre el doble guión bajo ("__")
        self.__numero = numero
        self.__saldo = 0
        self.__titular = titular #Cuando cree un objeto en el main, el titular va a pasar como un objeto de clase Persona
    
    #Hay que agregar un decorador al Getter, que en Python se llama "property" (usando @property)
    
    @property
    def saldo(self): #Método Getter
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def entidad_bancaria(self):
        return self.__entidad_bancaria
    
    def nombre_completo_titular(self): #COn este método llamamos a un atributo que es un objeto de otra clase, en lugar de usar un Getter
        return self.__titular.nombre_completo()
    
    '''
    @saldo.setter
    def saldo(self, nuevo_saldo): #Método Setter
        if nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
    
    @entidad_bancaria.setter
    def entidad_bancaria(self, nueva_entidad):
        self.__entidad_bancaria = nueva_entidad
    '''
    
    def saldo_suficiente(self, monto):
        return self.__saldo >= monto
    
    def recargar_saldo(self, cuanto):
        self.__saldo += cuanto
    
    def descontar_saldo(self, cuanto):
        if cuanto > 0 and self.saldo_suficiente(cuanto):
            self.__saldo -= cuanto
    
    
#Programa Principal

#Importar una clase: from nombre_del_modulo import lo_que_queres_del_modulo
from Persona import Persona
from TarjetaDeCredito import TarjetaDeCredito

juan = Persona('1234','Juan', 'Gomez', '21213', 'juan@fake.com')
tarjeta = TarjetaDeCredito('Banco Fake', '1234123412341234', juan) #El titular va a ser un objeto de clase Persona

print(tarjeta.saldo)
tarjeta.saldo = 25000
print(tarjeta.saldo)
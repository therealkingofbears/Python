from Ticket import Ticket

class Posnet:
    
    def __init__(self, tarjeta, monto, cantidad_cuotas) -> None:
        self.tarjeta = tarjeta
        self.monto = monto
        self.cantidad_cuotas= cantidad_cuotas
    
    def datos_validos(self, tarjeta, monto, cantidad_cuotas):
        return monto > 0 and cantidad_cuotas >= 1 and cantidad_cuotas <= 6
    
    def recargo_segun_cuotas(self, cantidad_cuotas):
        return (cantidad_cuotas - 1) * 0.03
    
    def efectuar_pago(self, tarjeta, monto, cantidad_cuotas):
        ticket: None
        if self.datos_validos(tarjeta, monto, cantidad_cuotas):
            monto_final = monto + monto * self.recargo_segun_cuotas(cantidad_cuotas)
            if tarjeta.saldo_suficiente(monto_final):
                tarjeta.descontar_saldo(monto_final)
                ticket = Ticket(tarjeta.nombre_completo_titular(), monto_final, monto_final/cantidad_cuotas)
        return ticket
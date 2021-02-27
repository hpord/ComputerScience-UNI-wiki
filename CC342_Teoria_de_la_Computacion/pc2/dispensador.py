class CajaRegistradora:
    def __init__(self, cajaChica):
        self.cajaChica = cajaChica 
    
    def getSaldoActual(self):
        return self.cajaChica
    
    def aceptarMonto(self, monto):
        self.cajaChica += monto

class TipoDispensador:
    def __init__(self, nroProductos, costo):
        self.nroProductos = nroProductos if nroProductos >= 0 else 0
        self.costo = costo if nroProductos >=0 else 0
    
    def getNroProductos(self):
        return self.nroProductos
    
    def getCosto(self):
        return self.costo
    
    def hacerVenta(self):
        if self.getNroProductos() > 0:
            self.nroProductos -= 1
        else:
            print("Producto agotado\n")
    
     
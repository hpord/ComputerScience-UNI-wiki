from dispensador import CajaRegistradora, TipoDispensador

def mostrarSeleccion():
    print("\nBienvenido a la dispensadora FC-UNI\n")
    print("Para elegir un producto, ingrese: ")
    print("G para galletas")
    print("C para chocolates")
    print("X para salir")

def VenderProducto(caja, dispensadorG, dispensadorC):
    salir = False
    vuelto = None
    nameProduct = None
    opciones = ['G', 'C', 'X']

    entrada = input("Ingrese por favor: ")

    if entrada == 'X':
        salir = True
        return salir
    else:

        caja.aceptarMonto(float(entrada))
        while caja.getSaldoActual() < 20:
            entrada = input("Ingrese por favor: ")
            if entrada not in opciones:
                caja.aceptarMonto(float(entrada))
            
            else:
                if entrada == 'X':
                    vuelto = caja.getSaldoActual()
                    print("Devolviendo {} centavos ".format(vuelto))
                    salir = True
                    return salir 
                else:
                    print("Saldo insuficiente, siga depositando ")

                
        vuelto = caja.getSaldoActual() - 20.0
        if vuelto > 0:
            print("vuelto: " + str(vuelto))
        entrada = input("Ingrese por favor: ")

        
        if entrada in list(opciones[0:2]):
            if entrada == 'C':
                nameProduct = "Chocolate"
                dispensadorC.hacerVenta()
            else:
                nameProduct = "Galleta"
                dispensadorG.hacerVenta()
        else: 
            print("Devolviendo {} centavos ".format(caja.getSaldoActual()))
            salir = True
            return salir 

    if nameProduct != None:    
        print("Recoja su {} al fondo y buen provecho\n".format(nameProduct))
    
    print("-------------------------------------")
    return salir

if __name__ == '__main__':
    cajaPrincipal = CajaRegistradora(cajaChica = 0)

    dispGalletas = TipoDispensador(nroProductos = 10, costo = 20.0)

    dispChocolates = TipoDispensador(nroProductos = 10, costo = 20.0)

    while True:
        mostrarSeleccion()
        if VenderProducto(cajaPrincipal, dispGalletas, dispChocolates):
            break
        else:
            continue







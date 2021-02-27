# diseño de la clase
class Acumulador():
    def __init__(self, valorInicial):
        self.estadoInicial = valorInicial

    def iniciar(self):
        self.estado = self.estadoInicial

    def siguientesValores(self, estado, simb):
        return (estado + simb, estado + simb)

    def transicion(self, simb):
        (si, yi) = self.siguientesValores(self.estado, simb)
        self.estado = si
        return yi

    def transducir(self, lista):
        self.iniciar()
        aux = []
        for item in lista:
            yi = self.transicion(item)
            aux.append(yi)

        return aux

# programa de prueba
if __name__ == '__main__':
    print('Iniciando acumulador..')
    a = Acumulador(0)
    # valores de entrada
    lista = [12, 8, 25, -37, 9, 16]
    print('Lista de entrada\n', lista)

    lst_salida = a.transducir(lista)
    print("trans\tacumulador")
    for i in range(len(lst_salida)):
        print(i+1, end="\t")
        print(lst_salida[i])



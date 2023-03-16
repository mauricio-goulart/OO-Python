class Fila():


    c_fila = ['fodase']

    classmethod
    def entrar(cls, obj):
        cls.c_fila.append(obj)


    def __init__(self):
        self.fila = []

    def entrarc(self, obj):
        self.fila.append(obj)


Fila().entrar('Ola')
supermercado = Fila()
supermercado.entrarc('Maria')

print(supermercado.c_fila, supermercado.fila)
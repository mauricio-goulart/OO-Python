class Fila:
    fila = []

    def entrar(self, nome):
        self.fila.append(nome)
    def sair(self):
        self.fila.pop(0)

supermercado = Fila()

supermercado.entrar('Mauricio')

print(supermercado.fila)
print(len(supermercado.fila))
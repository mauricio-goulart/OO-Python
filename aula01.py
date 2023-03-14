class Fila:
    fila = []

    def entrar(self, nome):
        self.fila.append(nome)

supermercado = Fila()

supermercado.entrar('Mauricio')

print(supermercado.fila)

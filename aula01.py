#Basic

class Passaro:
    def voar():
        print('Voando')
    def pousar():
        print('Pousado')


Passaro.voar()


#Aplicando o 'self'
class Passaro1:
    estado = 'parado'
    def voar(self):
        self.estado = 'voando'
        print(self.estado)
    def pousar(self):
        self.estado = 'Pousado'
        print(self.estado)

p1 = Passaro1

p1.voar()

print(p1.estado)

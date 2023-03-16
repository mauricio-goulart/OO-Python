class Pizza:
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def comer(self):
        self.pedacos = self.pedacos - 1

    @classmethod
    def mudarpedacos(cls, pedacos):
        cls.pedacos = pedacos
class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, Ruedas {}, Puertas {}, Velocidad {} km/h, Cilindrada {} cc".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)


car = Coche("negro", 4, 5, 200, 1000)
print(car)

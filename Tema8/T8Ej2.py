import pickle
class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return "Color: {}. Ruedas: {}. Puertas {}.".format(self.color, self.ruedas, self.puertas)


f = open('T8Ej2_Guiomar', 'wb')
car = Vehiculo("negro", 4, 5)
pickle.dump(car, f)
f.close()

f_car = open('T8Ej2_Guiomar', 'rb')
car_load = pickle.load(f_car)
f_car.close()
print(car_load)
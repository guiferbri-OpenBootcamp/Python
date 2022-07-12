class Alumno:
    def init(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def print(self):
        print("Alumno: {}. Nota: {}".format(self.nombre, self.nota))

    def result(self):
        if self.nota > 5:
            print("El alumno {} ha aprobado".format(self.nombre))
        else:
            print("El alumno {} NO ha aprobado".format(self.nombre))


alum1 = Alumno()
alum1.init("Juanito", 8)
alum1.print()
alum1.result()

alum2 = Alumno()
alum2.init("Pepito", 0)
alum2.print()
alum2.result()
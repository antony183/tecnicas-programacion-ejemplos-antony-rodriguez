class Animal:
    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        return "Guau"


class Gato(Animal):
    def sonido(self):
        return "Miau"


def hacer_sonido(animal):
        print(animal.sonido())


perro = Perro()
gato = Gato()

hacer_sonido(perro)
hacer_sonido(gato)

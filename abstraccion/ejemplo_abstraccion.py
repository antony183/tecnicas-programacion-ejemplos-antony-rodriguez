from abc import ABC, abstractmethod

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

# Clase concreta
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

# Uso
fig = Circulo(5)
print("Área del círculo:", fig.area())


import math


class Figura:

    def __init__(self, color):
        self.color = color

    def area(self):
        """Retorna el área de la figura. Las subclases deben sobreescribir este método."""
        return 0

    def describir(self):
        """Imprime el color y el área de la figura."""
        print(f"Figura de color {self.color} | Área: {self.area():.2f}")


class Rectangulo(Figura):


    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):

        return self.base * self.altura

    def describir(self):
       
        print(f"Rectángulo {self.color} | Base: {self.base} | Altura: {self.altura} | Área: {self.area():.2f}")


class Circulo(Figura):


    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):

        return math.pi * self.radio ** 2

    def describir(self):
        """Descripción específica del círculo."""
        print(f"Círculo {self.color} | Radio: {self.radio} | Área: {self.area():.2f}")


figuras = [
    Rectangulo("rojo", 5, 3),
    Rectangulo("azul", 10, 4),
    Circulo("verde", 7),
    Circulo("amarillo", 3),
]

print("=== Sistema de Figuras Geométricas ===\n")

for figura in figuras:
    figura.describir()
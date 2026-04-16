
class Vehiculo:


    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):

        print(f"Vehículo de marca {self.marca} con velocidad máxima de {self.velocidad_max} km/h.")


class Auto(Vehiculo):


    def __init__(self, marca, velocidad_max, cantidad_puertas):
        super().__init__(marca, velocidad_max)
        self.cantidad_puertas = cantidad_puertas

    def describir(self):

        print(f"Auto {self.marca} | Velocidad máxima: {self.velocidad_max} km/h | Puertas: {self.cantidad_puertas}")


class Moto(Vehiculo):


    def __init__(self, marca, velocidad_max, tipo):
        super().__init__(marca, velocidad_max)
        self.tipo = tipo

    def describir(self):

        print(f"Moto {self.marca} | Velocidad máxima: {self.velocidad_max} km/h | Tipo: {self.tipo}")



vehiculos = [
    Auto("Toyota", 180, 4),
    Auto("Ford", 200, 2),
    Moto("Honda", 220, "deportiva"),
    Moto("Harley-Davidson", 160, "cruiser"),
]

print("=== Sistema de Transporte ===\n")

for vehiculo in vehiculos:
    vehiculo.describir()
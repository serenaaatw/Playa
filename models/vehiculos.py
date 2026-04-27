class Vehiculo:
    def __init__(self, matricula, color, marca, modelo):
        self.matricula=matricula
        self.color=color
        self.marca=marca
        self.modelo=modelo
    def encender (self):
        return f"El vehiculo {self.marca} de color {self.color} con patente {self.matricula} enciende con normalidad"
    def avanzar (self):
        return f"El vehiculo {self.marca} de color {self.color} con patente {self.matricula} avanza cuando ingresa y se retira del taller"
Vehiculo_uno = Vehiculo ("Blanco","Peugeot","AG642GQ")
print(Vehiculo_uno.encender())
print(Vehiculo_uno.avanzar())
Vehiculo_dos = Vehiculo ("Rojo","Onix","AH842LK")
print(Vehiculo_dos.encender())
print(Vehiculo_dos.avanzar())
Vehiculo_tres = Vehiculo ("Gris","Cronos","AF548UV")
print(Vehiculo_tres.encender())
print(Vehiculo_tres.avanzar()) 
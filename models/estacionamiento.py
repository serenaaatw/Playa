from models.db import db


class Estacionamiento(db.Model):
    __tablename__ = "Estacionamiento"
    id_estacionamiento = db.Column(db.Integer, primary_key = True)
    capacidad = db.Column(db.Integer)
    tarifa_auto = db.Column(db.Float)
    tarifa_camioneta = db.Column(db.Float)
    tarifa_moto = db.Column(db.Float)
    espacios_disponibles = db.Column(db.Integer)
    espacios_ocupados = db.Column(db.Integer)
    def __init__(self, id_estacionamiento, capacidad, tarifa_auto, tarifa_camioneta, tarifa_moto):
        self.id_estacionamiento = id_estacionamiento
        self.capacidad = capacidad
        self.tarifa_auto = tarifa_auto
        self.tarifa_camioneta = tarifa_camioneta
        self.tarifa_moto = tarifa_moto
        self.espacios_ocupados = 0
    def asignar_espacio(self):
        if self.espacios_ocupados < self.capacidad:
            self.espacios_ocupados += 1
            return "Espacio asignado correctamente"
        else:
            return "No hay espacios disponibles"
    def liberar_espacio(self):
       if self.espacios_ocupados > 0:
         self.espacios_ocupados -= 1
         return "Espacio liberado"
       else:
         return "No hay vehículos para retirar"
    def espacios_disponibles(self):
        return self.capacidad - self.espacios_ocupados
    def serialize (self):
       return {
          "id_estacionamiento": self.id_estacionamiento,
          "capacidad": self.capacidad,
          "tarifa_auto": self.tarifa_auto,
          "tarifa_camioneta": self.tarifa_camioneta,
          "tarifa_moto": self.tarifa_moto
       }
    

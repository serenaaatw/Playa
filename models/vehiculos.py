from models.db import db

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(100), unique=True, nullable=False)
    color = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    modelo = db.Column(db.String(100))

    def __init__(self, matricula, color, marca, modelo):
        self.matricula=matricula
        self.color=color
        self.marca=marca
        self.modelo=modelo

    def to_dict(self):
        return {
            'id': self.id,
            'matricula':self.matricula,
            'color': self.color,
            'marca': self.marca,
            'modelo': self.modelo

        }
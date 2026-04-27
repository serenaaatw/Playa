from models.db import db

class Propietario(db.Model):
    __tablename__="Propietario"
    dni= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), nullable= False)
    apellido= db.Column(db.String(50), nullable=False)
    telefono= db.Column(db.String(20), nullable= False)

    def __init__(self, dni, nombre, apellido, telefono):
        self.dni= dni
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono 

    def serialize(self):
        return {"dni": self.dni,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "telefono": self.telefono}
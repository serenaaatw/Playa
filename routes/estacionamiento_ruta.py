from flask import Blueprint
from models.estacionamiento import Estacionamiento

Estacionamiento_bp = Blueprint("estacionamiento", __name__)


#@app.route("/estacionamiento")
#def ver_estacionamiento():
  #  return f"Espacios disponibles: {est.espacios_disponibles()}"

#@app.route("/estacionamiento/asignar")
#def asignar():
 #   return est.asignar_espacio()

#@app.route("/estacionamiento/liberar")
#def liberar():
 #   return est.liberar_espacio()

@Estacionamiento_bp.route ("/infoEstacionamientos")
def infoEstacionamientos():
 info = Estacionamiento.query.all()
 return [estacionamiento.serialize() for estacionamiento in info]

@Estacionamiento_bp.route ("/infoEstacionamiento/<int:id>")
def infoEstacionamiento(id):
 info = Estacionamiento.query.get (id)
 if info:
  return info.serialize() 
 else:
  return print(f"El estacionamiento con el id {id} no existe")

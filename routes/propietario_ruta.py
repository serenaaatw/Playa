from flask import Blueprint
from models.propietario import Propietario

propietario_db= Blueprint("propietario", __name__)

@propietario_db.route("/propietario/<int:id>")
def info_propietario(id):
    propietario= Propietario.query.get(id)
    if propietario:
        return propietario.serialize()
    else:
        return {"error": "Propietario no encontrado"}, 404
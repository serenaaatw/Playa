from flask import Blueprint, jsonify
from models.vehiculos import Vehiculo

vehiculo_bp=Blueprint('Vehiculo_bp', __name__)

@vehiculo_bp.route("/infovehiculo/<int:id>", methods=["GET"])
def get_vehiculo(id):
    vehiculo=Vehiculo.query.get(id)

    if vehiculo:
        return jsonify ({
            "id":vehiculo.id,
            "marca": vehiculo.marca,
            "modelo": vehiculo.modelo,
            "color": vehiculo.color,
            "matricula": vehiculo.matricula
        }), 200
    else: 
        return jsonify({"mensaje":"Vehículo no encontrado"}), 404
<<<<<<< HEAD
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
=======
from flask import Blueprint


>>>>>>> d6dcbcd5672e291f1674d6ace0d7d2a4120eb2c7

@playa.route("/infovehiculos/<int:id>")
def infovehiculo(id):
    vehiculo={
        "id": id,
        "marca": "Peugeot",
        "modelo": "208",
        "color": "blanco",
        "matricula": "AG642GQ"
    }
    return vehiculo
from flask import Flask
from routes.vehiculo_ruta import vehiculo_bp
from config.config import DATABASE_CONNECTION_URI
from models.db import db

# Create a Flask application instance

app = Flask(__name__)
app.register_blueprint(vehiculo_bp)


# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.vehiculos import Vehiculo
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
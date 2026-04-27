from flask import Flask
from routes.propietario_ruta import propietario_db
from config.config import DATABASE_CONNECTION_URI
from models.db import db

# Create a Flask application instance

app = Flask(__name__)
app.register_blueprint(propietario_db)


app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.propietario import Propietario
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
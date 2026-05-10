# Sistema de Gestión de Estacionamiento

## Integrantes del grupo
- Serena Vargas
- Tomás Caballero
- Antonella Fernandez

---

## Descripción breve
Este proyecto consiste en una aplicación desarrollada para gestionar un estacionamiento de manera sencilla y organizada. El sistema permite administrar información relacionada con vehículos, estacionamientos y propietarios.

---

## Configuración de la base de datos

Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

```env
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base>
MYSQL_HOST=<host_de_mysql>
MYSQL_PORT=<puerto_de_mysql>
```

---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/serenaaatw/Playa.git
```

### 2. Ingresar al repositorio
```bash
cd TPEstacionamiento
code .
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

---

## Endpoints implementados

- GET /infoEstacionamientos
- GET /infoEstacionamiento/<int:id>
- GET /propietario/<int:id>
- GET /infovehiculo/<int:id>

---

## Aporte de cada integrante

### Tomás Caballero
- Creación del modelo estacionamiento
- Creación de rutas para estacionamiento
- Rama utilizada: `featureEstacionamiento`

### Antonella Fernandez
- Creación del modelo vehículo
- Creación de rutas para vehículo
- Solución de conflictos en Git
- Rama utilizada: `feature/vehiculos`

### Serena Vargas
- Creación del modelo propietario
- Creación de rutas para propietario
- Solución de conflictos en Git
- Testeo y corrección final
- Rama utilizada: `featurePropietario`

---

## Trabajo grupal
- Configuración de la aplicación
- Configuración de la base de datos
- Integración general del proyecto
"""
Este módulo inicializa la base de datos de la aplicación de estrella de mar.
"""

from api_starfish.app import app, db

# Crear todas las tablas en la base de datos
with app.app_context():
    db.create_all()

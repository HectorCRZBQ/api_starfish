"""
Pruebas de carga para la API de Starfish utilizando Locust.
"""

import json
import random
from locust import HttpUser, task, between

class StarfishLoadTest(HttpUser):
    """Clase para realizar pruebas de carga en la API de Starfish."""

    wait_time = between(1, 5)  # Simula una espera de entre 1 a 5 segundos entre tareas

    @task(1)
    def get_all_starfish(self):
        """Realiza una solicitud GET a la ruta para obtener todas las estrellas de mar."""
        self.client.get("/starfish")

    @task(2)
    def create_starfish(self):
        """Realiza una solicitud POST para crear una nueva estrella de mar."""
        starfish_data = {
            "name": f"Starfish_{random.randint(1, 1000)}",
            "color": random.choice(["red", "blue", "green", "yellow"]),
            "limbs": random.randint(5, 10),
            "depth": round(random.uniform(5.0, 200.0), 2),
            "age": random.randint(1, 100),
            "gender": random.choice(["male", "female"]),
            "latin_name": "Asterias rubens",
            "habitat": random.choice(["coral reef", "deep sea", "sand", "rocky shore"])
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/starfish", data=json.dumps(starfish_data), headers=headers)

    @task(1)
    def get_starfish_by_id(self):
        """Realiza una solicitud GET a una estrella de mar específica."""
        starfish_id = random.randint(1, 100)  # Asume que hay al menos 100 estrellas de mar
        self.client.get(f"/starfish/{starfish_id}")

    @task(1)
    def update_starfish(self):
        """Realiza una solicitud PUT para actualizar una estrella de mar existente."""
        starfish_id = random.randint(1, 100)  # Asume que hay al menos 100 estrellas de mar
        updated_data = {
            "name": "Updated_Starfish",
            "color": "purple"
        }
        headers = {'Content-Type': 'application/json'}
        self.client.put(f"/starfish/{starfish_id}", data=json.dumps(updated_data), headers=headers)

    @task(1)
    def delete_starfish(self):
        """Realiza una solicitud DELETE para eliminar una estrella de mar."""
        starfish_id = random.randint(1, 100)  # Asume que hay al menos 100 estrellas de mar
        self.client.delete(f"/starfish/{starfish_id}")

    def on_start(self):
        """Función opcional para ejecutar cuando un usuario se conecta por primera vez."""
        # Puedes inicializar el estado del usuario aquí si es necesario.
        # Eliminar la declaración pass ya que no se necesita inicializar nada


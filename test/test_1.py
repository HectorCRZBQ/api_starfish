import unittest
import json
from app import app, db, Starfish

class StarfishAPITestCase(unittest.TestCase):

    def setUp(self):
        # Configuración para pruebas
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()  # Crear todas las tablas

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()  # Limpiar la sesión
            db.drop_all()  # Borrar todas las tablas

    def test_crear_starfish(self):
        response = self.client.post('/starfish', 
                                     data=json.dumps({
                                         'name': 'Estrella Azul',
                                         'color': 'Azul',
                                         'limbs': 5,
                                         'depth': 20.5,
                                         'age': 3,
                                         'gender': 'Femenino',
                                         'latin_name': 'Asterias',
                                         'habitat': 'Océano'
                                     }), 
                                     content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Estrella Azul', str(response.data))

    def test_obtener_todas_starfish(self):
        self.client.post('/starfish', 
                         data=json.dumps({
                             'name': 'Estrella Amarilla',
                             'color': 'Amarillo',
                             'limbs': 5,
                             'depth': 15.0,
                             'age': 2,
                             'gender': 'Masculino',
                             'latin_name': 'Echinaster',
                             'habitat': 'Arrecife'
                         }), 
                         content_type='application/json')

        response = self.client.get('/starfish')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Estrella Amarilla', str(response.data))

    def test_obtener_starfish_por_id(self):
        self.client.post('/starfish', 
                         data=json.dumps({
                             'name': 'Estrella Verde',
                             'color': 'Verde',
                             'limbs': 5,
                             'depth': 10.0,
                             'age': 4,
                             'gender': 'Femenino',
                             'latin_name': 'Astropecten',
                             'habitat': 'Aguas poco profundas'
                         }), 
                         content_type='application/json')

        response = self.client.get('/starfish/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Estrella Verde', str(response.data))

    def test_actualizar_starfish(self):
        self.client.post('/starfish', 
                         data=json.dumps({
                             'name': 'Estrella Rosa',
                             'color': 'Rosa',
                             'limbs': 5,
                             'depth': 25.0,
                             'age': 5,
                             'gender': 'Femenino',
                             'latin_name': 'Paxillopsis',
                             'habitat': 'Mar abierto'
                         }), 
                         content_type='application/json')

        response = self.client.put('/starfish/1', 
                                    data=json.dumps({
                                        'color': 'Rosa Claro'
                                    }), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Rosa Claro', str(response.data))

    def test_eliminar_starfish(self):
        self.client.post('/starfish', 
                         data=json.dumps({
                             'name': 'Estrella Naranja',
                             'color': 'Naranja',
                             'limbs': 5,
                             'depth': 5.0,
                             'age': 1,
                             'gender': 'Masculino',
                             'latin_name': 'Asterina',
                             'habitat': 'Playa'
                         }), 
                         content_type='application/json')

        response = self.client.delete('/starfish/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('La estrella de mar con ID 1 ha sido eliminada.', str(response.data))

if __name__ == '__main__':
    unittest.main()

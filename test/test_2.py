"""
Pruebas unitarias para la API de Starfish.
"""
import pytest
from app import app, db

@pytest.fixture
def test_client():
    """
    Configurar la aplicación para pruebas.
    """
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usar una base de datos en memoria
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos
        yield app.test_client()  # Proveer el cliente de prueba
        db.drop_all()  # Limpiar la base de datos después de las pruebas

def test_crear_starfish(test_client):
    """
    Prueba para crear una estrella de mar.
    """
    response = test_client.post('/starfish', json={
        'name': 'Estrella Azul',
        'color': 'Azul',
        'limbs': 5,
        'depth': 10.5,
        'age': 2,
        'gender': 'Femenino',
        'latin_name': 'Asterias',
        'habitat': 'Océano'
    })
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Estrella Azul'
    assert data['color'] == 'Azul'

def test_obtener_starfish(test_client):
    """
    Prueba para obtener todas las estrellas de mar.
    """
    test_client.post('/starfish', json={
        'name': 'Estrella Verde',
        'color': 'Verde',
        'limbs': 5,
        'depth': 8.0,
        'age': 3,
        'gender': 'Masculino',
        'latin_name': 'Echinaster',
        'habitat': 'Arrecife de coral'
    })

    response = test_client.get('/starfish')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0  # Debe devolver al menos una estrella de mar

def test_obtener_starfish_por_id(test_client):
    """
    Prueba para obtener una estrella de mar por su ID.
    """
    response = test_client.post('/starfish', json={
        'name': 'Estrella Rosa',
        'color': 'Rosa',
        'limbs': 5,
        'depth': 5.0,
        'age': 1,
        'gender': 'Femenino',
        'latin_name': 'Ophidiaster',
        'habitat': 'Playas de arena'
    })
    
    starfish_id = response.get_json()['id']
    response = test_client.get(f'/starfish/{starfish_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == starfish_id

def test_actualizar_starfish(test_client):
    """
    Prueba para actualizar una estrella de mar existente.
    """
    response = test_client.post('/starfish', json={
        'name': 'Estrella Amarilla',
        'color': 'Amarillo',
        'limbs': 5,
        'depth': 12.0,
        'age': 4,
        'gender': 'Masculino',
        'latin_name': 'Asterina',
        'habitat': 'Aguas costeras'
    })

    starfish_id = response.get_json()['id']
    response = test_client.put(f'/starfish/{starfish_id}', json={
        'name': 'Estrella Amarilla Actualizada',
        'color': 'Amarillo Brillante'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Estrella Amarilla Actualizada'
    assert data['color'] == 'Amarillo Brillante'

def test_eliminar_starfish(test_client):
    """
    Prueba para eliminar una estrella de mar y verificar que no se puede obtener después.
    """
    response = test_client.post('/starfish', json={
        'name': 'Estrella Morada',
        'color': 'Morado',
        'limbs': 5,
        'depth': 15.0,
        'age': 5,
        'gender': 'Femenino',
        'latin_name': 'Astropecten',
        'habitat': 'Fondo marino'
    })

    starfish_id = response.get_json()['id']
    response = test_client.delete(f'/starfish/{starfish_id}')
    
    assert response.status_code == 200
    assert "La estrella de mar con ID" in response.get_json()["mensaje"]

    # Intentar obtener la estrella de mar eliminada
    response = test_client.get(f'/starfish/{starfish_id}')
    assert response.status_code == 404

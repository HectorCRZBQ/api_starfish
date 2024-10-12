import pytest
import json
from app import app, db, Starfish

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_crear_starfish_valido(client):
    # Datos de entrada válidos
    response = client.post('/starfish', json={
        'name': 'Dorado',
        'color': 'Amarillo',
        'limbs': 5,
        'depth': 30.0,
        'age': 2,
        'gender': 'Macho',
        'latin_name': 'Asteroidea',
        'habitat': 'Océano'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Dorado'

def test_crear_starfish_invalido(client):
    # Datos de entrada inválidos (falta el campo 'name')
    response = client.post('/starfish', json={
        'color': 'Rojo',
        'limbs': 5,
        'depth': 20.0,
        'age': 1,
        'gender': 'Hembra',
        'latin_name': 'Asteroidea',
        'habitat': 'Océano'
    })
    assert response.status_code == 400  # Bad Request

def test_obtener_starfish_no_existente(client):
    # Intentar obtener una estrella de mar que no existe
    response = client.get('/starfish/999')
    assert response.status_code == 404  # Not Found

def test_actualizar_starfish_invalido(client):
    # Primero, crear un objeto para actualizar
    response = client.post('/starfish', json={
        'name': 'Estrella',
        'color': 'Azul',
        'limbs': 5,
        'depth': 10.0,
        'age': 3,
        'gender': 'Macho',
        'latin_name': 'Astropecten',
        'habitat': 'Coral'
    })
    starfish_id = response.get_json()['id']

    # Intentar actualizar la estrella de mar con datos inválidos
    response = client.put(f'/starfish/{starfish_id}', json={
        'name': 'Estrella',
        'color': 'Verde',
        'limbs': -1,  # Valor inválido para limbs
        'depth': 10.0,
        'age': 3,
        'gender': 'Macho',
        'latin_name': 'Astropecten',
        'habitat': 'Coral'
    })
    assert response.status_code == 400  # Bad Request

def test_eliminar_starfish(client):
    # Crear una estrella de mar para eliminar
    response = client.post('/starfish', json={
        'name': 'Estrella',
        'color': 'Morada',
        'limbs': 5,
        'depth': 15.0,
        'age': 4,
        'gender': 'Hembra',
        'latin_name': 'Astropecten',
        'habitat': 'Roca'
    })
    starfish_id = response.get_json()['id']

    # Eliminar la estrella de mar
    response = client.delete(f'/starfish/{starfish_id}')
    assert response.status_code == 200  # OK

    # Verificar que ya no se puede obtener
    response = client.get(f'/starfish/{starfish_id}')
    assert response.status_code == 404  # Not Found

def test_inyeccion_sql(client):
    # Intentar una inyección SQL (aunque SQLAlchemy debería prevenir esto)
    response = client.get('/starfish/1; DROP TABLE starfish; --')
    assert response.status_code == 404  # Not Found

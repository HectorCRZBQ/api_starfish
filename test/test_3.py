import pytest
from app import app, db, Starfish
from flask import json

# Este decorador indica que es una función que se ejecutará antes de todas las pruebas
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

# Helper para agregar una estrella de mar al sistema durante las pruebas
def crear_estrella_mar(client, name, color, limbs, depth, age, gender, latin_name, habitat):
    return client.post('/starfish', 
        data=json.dumps({
            "name": name,
            "color": color,
            "limbs": limbs,
            "depth": depth,
            "age": age,
            "gender": gender,
            "latin_name": latin_name,
            "habitat": habitat
        }), 
        content_type='application/json')

# Test: Crear una nueva estrella de mar
def test_crear_starfish(client):
    response = crear_estrella_mar(client, "Estrella Azul", "Azul", 5, 30.0, 3, "Hembra", "Asterias rubens", "Océano Atlántico")
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == "Estrella Azul"
    assert data['color'] == "Azul"

# Test: Obtener todas las estrellas de mar
def test_obtener_todas_las_starfish(client):
    crear_estrella_mar(client, "Estrella Roja", "Rojo", 5, 20.0, 2, "Macho", "Acanthaster planci", "Océano Pacífico")
    response = client.get('/starfish')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['name'] == "Estrella Roja"

# Test: Obtener una estrella de mar por ID
def test_obtener_starfish_por_id(client):
    response_post = crear_estrella_mar(client, "Estrella Verde", "Verde", 5, 25.0, 4, "Hembra", "Pisaster ochraceus", "Océano Índico")
    data_post = json.loads(response_post.data)
    starfish_id = data_post['id']

    response_get = client.get(f'/starfish/{starfish_id}')
    assert response_get.status_code == 200
    data_get = json.loads(response_get.data)
    assert data_get['name'] == "Estrella Verde"

# Test: Actualizar una estrella de mar
def test_actualizar_starfish(client):
    response_post = crear_estrella_mar(client, "Estrella Amarilla", "Amarillo", 5, 35.0, 5, "Hembra", "Protoreaster nodosus", "Océano Índico")
    data_post = json.loads(response_post.data)
    starfish_id = data_post['id']

    response_put = client.put(f'/starfish/{starfish_id}', 
        data=json.dumps({"name": "Estrella Amarilla Modificada"}),
        content_type='application/json')
    
    assert response_put.status_code == 200
    data_put = json.loads(response_put.data)
    assert data_put['name'] == "Estrella Amarilla Modificada"

# Test: Eliminar una estrella de mar
def test_eliminar_starfish(client):
    response_post = crear_estrella_mar(client, "Estrella Morada", "Morado", 5, 15.0, 2, "Macho", "Linckia laevigata", "Océano Atlántico")
    data_post = json.loads(response_post.data)
    starfish_id = data_post['id']

    response_delete = client.delete(f'/starfish/{starfish_id}')
    assert response_delete.status_code == 200
    data_delete = json.loads(response_delete.data)
    assert "eliminada" in data_delete['mensaje']

    # Verificar que la estrella fue eliminada
    response_get = client.get(f'/starfish/{starfish_id}')
    assert response_get.status_code == 404

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starfish.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Starfish(db.Model):
    """
    Modelo de datos para una estrella de mar, con atributos adicionales como hábitat.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    limbs = db.Column(db.Integer, nullable=False)
    depth = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    latin_name = db.Column(db.String(80), nullable=False)
    habitat = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        """
        Convierte el objeto Starfish a un diccionario.
        """
        return {
            'id': self.id,  
            'name': self.name,
            'color': self.color,
            'limbs': self.limbs,
            'depth': self.depth,
            'age': self.age,
            'gender': self.gender,
            'latin_name': self.latin_name,
            'habitat': self.habitat
        }

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

@app.route('/starfish', methods=['POST'])
def crear_starfish():
    """
    Crea una nueva entrada de estrella de mar.
    """
    data = request.json
    required_fields = ['name', 'color', 'limbs', 'depth', 'age', 'gender', 'latin_name', 'habitat']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    nueva_starfish = Starfish(
        name=data['name'],
        color=data['color'],
        limbs=data['limbs'],
        depth=data['depth'],
        age=data['age'],
        gender=data['gender'],
        latin_name=data['latin_name'],
        habitat=data['habitat']
    )
    db.session.add(nueva_starfish)
    db.session.commit()
    return jsonify(nueva_starfish.to_dict()), 201

@app.route('/starfish', methods=['GET'])
def obtener_starfish():
    """
    Obtiene una lista de todas las estrellas de mar.
    """
    starfish_list = Starfish.query.all()
    return jsonify([s.to_dict() for s in starfish_list]), 200

@app.route('/starfish/<int:starfish_id>', methods=['GET'])
def obtener_starfish_por_id(starfish_id):
    """
    Obtiene una estrella de mar específica por ID.
    """
    starfish = Starfish.query.get_or_404(starfish_id)
    return jsonify(starfish.to_dict()), 200

@app.route('/starfish/<int:starfish_id>', methods=['PUT'])
def actualizar_starfish(starfish_id):
    """
    Actualiza una estrella de mar existente.
    """
    data = request.json
    starfish = Starfish.query.get_or_404(starfish_id)

    if 'limbs' in data and data['limbs'] < 0:
        return jsonify({"error": "El número de extremidades no puede ser negativo."}), 400

    starfish.name = data.get('name', starfish.name)
    starfish.color = data.get('color', starfish.color)
    starfish.limbs = data.get('limbs', starfish.limbs)
    starfish.depth = data.get('depth', starfish.depth)
    starfish.age = data.get('age', starfish.age)
    starfish.gender = data.get('gender', starfish.gender)
    starfish.latin_name = data.get('latin_name', starfish.latin_name)
    starfish.habitat = data.get('habitat', starfish.habitat)

    db.session.commit()
    return jsonify(starfish.to_dict()), 200

@app.route('/starfish/<int:starfish_id>', methods=['DELETE'])
def eliminar_starfish(starfish_id):
    """
    Elimina una estrella de mar por su ID.
    """
    starfish = Starfish.query.get_or_404(starfish_id)
    db.session.delete(starfish)
    db.session.commit()
    return jsonify({"mensaje": f"La estrella de mar con ID {starfish_id} ha sido eliminada."}), 200

if __name__ == '__main__':
    app.run(debug=True)

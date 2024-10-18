.PHONY: all setup init_db test clean lint coverage trivy encrypt decrypt

all: setup lint test trivy encrypt decrypt clean

# Montaje del entorno
setup:
	@echo "Creando el entorno virtual y activándolo..."
	python3 -m venv venv
	@echo "Instalando las dependencias desde requirements.txt..."
	venv/bin/pip install -r requirements.txt
	@echo "Inicializando la base de datos..."
	venv/bin/python init_db.py

# Inicialización de la base de datos manualmente
init_db:
	@echo "Inicializando la base de datos manualmente..."
	venv/bin/python init_db.py

# Linter con Pylint
lint:
	@echo "Ejecutando Pylint en app.py y en la carpeta de pruebas..."
	venv/bin/pylint app.py test/ || true

# Ejecutar pruebas con cobertura de código
test: coverage

coverage:
	@echo "Ejecutando pruebas y generando reporte de cobertura..."
	venv/bin/coverage run -m pytest test/
	@echo "Generando reporte de cobertura..."
	venv/bin/coverage report
	@echo "Generando reporte en HTML..."
	venv/bin/coverage html

# Escanear el proyecto en busca de vulnerabilidades con Trivy
trivy:
	@echo "Escaneando la imagen de Docker en busca de vulnerabilidades..."
	trivy fs .

# Cifrar el archivo secrets.yaml
encrypt:
	@echo "Cifrando el archivo secrets.yaml..."
	@read -p "Introduce tu PGP Key ID (últimos 8 caracteres o ID completo): " PGP_KEY_ID; \
	sops --encrypt --pgp $$PGP_KEY_ID secrets.yaml > secrets.enc.yaml; \
	echo "Archivo cifrado como secrets.enc.yaml"

# Descifrar el archivo secrets.enc.yaml
decrypt:
	@echo "Descifrando el archivo secrets.enc.yaml..."
	sops --decrypt secrets.enc.yaml > secrets.yaml
	@echo "Archivo descifrado como secrets.yaml"

# Limpiar el entorno
clean:
	@echo "Limpiando el entorno..."
	rm -rf venv
	rm -rf htmlcov
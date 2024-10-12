.PHONY: all setup init_db test clean

all: setup test clean

setup:
	@echo "Creando el entorno virtual y activándolo..."
	python3 -m venv venv
	@echo "Instalando las dependencias desde requirements.txt..."
	venv/bin/pip install -r requirements.txt
	@echo "Inicializando la base de datos..."
	venv/bin/python init_db.py

# Versión extendida de test (los 5 separados)
test:
	@echo "Ejecutando pruebas..."
	for test_file in test/test_*.py; do \
		echo "Ejecutando $$test_file..."; \
		venv/bin/pytest $$test_file; \
	done

# Version reducida de tests (unico de los 5)

# test:
#	@echo "Ejecutando pruebas..."
#	venv/bin/pytest tests/

clean:
	@echo "Limpiando el entorno..."
	rm -rf venv



from projen.python import PythonProject
from projen.github import GithubWorkflow
from projen import javascript

# Configuración básica del proyecto
project = PythonProject(
    author_email="hectorcb3333@gmail.com",
    author_name="HectorCRZBQ",
    version="0.1.0", # Versión inicial
    name="api-starfish", # Nombre del proyecto
    description="API that makes the CRUD tasks about starfish", # Descripción del proyecto
    module_name="api_starfish", # Nombre del módulo principal
    python_version="3.12", # Versión mínima de Python requerida
    deps=[
        # Dependencias declaradas en requirements.txt
        "anaconda-anon-usage", "archspec", "astroid==3.3.5", "attrs==24.2.0",
        "blinker==1.8.2", "Brotli", "certifi", "cffi", "click==8.1.7",
        "conda", "coverage==7.3.1", "dill==0.3.9", "Flask==2.2.5",
        "Flask-Cors==5.0.0", "Flask-Login==0.6.3", "Flask-SQLAlchemy==3.1.1",
        "Flask-Testing==0.8.1", "gevent==24.10.2", "idna", "importlib_resources==6.4.5",
        "isort==5.13.2", "itsdangerous==2.2.0", "Jinja2==3.1.4",
        "locust==2.31.8", "marshmallow==3.22.0", "marshmallow-sqlalchemy==1.1.0",
        "msgpack==1.1.0", "pylint==3.3.1", "pytest==7.4.3", "pytest-flask==1.3.0",
        "python-dotenv==1.0.1", "SQLAlchemy==2.0.35"
    ],
    dev_deps=[
        # Dependencias para desarrollo
        "pytest", "pytest-flask", "coverage", "pylint"
    ],
)

# Configuración de Github Workflows para CI/CD
workflow = GithubWorkflow(project, "ci")

# Tareas de Projen
project.add_task("lint", {
    "exec": "pylint api_starfish/ tests/"
})
project.add_task("test", {
    "exec": "pytest --cov=api_starfish"
})
project.add_task("coverage", {
    "exec": "coverage report -m"
})
project.add_task("trivy", {
    "exec": "make trivy" # Ejecuta el comando para trivy, definido en Makefile
})
project.add_task("encrypt", {
    "exec": "sops --encrypt --pgp FBC7B9E2A4F9289AC0C1D4843D16CEE4A27381B4 secrets.yaml > secrets.enc.yaml"
})
project.add_task("decrypt", {
    "exec": "sops --decrypt secrets.enc.yaml > secrets.yaml"
})

# Configuración de Gitignore
project.gitignore.add_patterns(
    ".venv",
    "*.pyc",
    "__pycache__",
    "secrets.yaml",  # Ignorar secrets.yaml para evitar filtración
    ".env",  # Ignorar .env
)

# Configuración de ESLint (para proyectos con TypeScript o JS)
eslint = javascript.Eslint(project)
eslint.add_ignore_patterns("**/node_modules/*")
eslint.add_ignore_patterns("**/dist/*")

# Ejecutar Projen
project.synth()

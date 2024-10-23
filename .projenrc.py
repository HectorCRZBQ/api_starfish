from projen.python import PythonProject

project = PythonProject(
    author_email="hectorcb3333@gmail.com",
    author_name="HectorCRZBQ",
    module_name="api_starfish",
    name="api_starfish",
    version="0.1.0",
)

project.synth()
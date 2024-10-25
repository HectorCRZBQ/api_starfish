# Comparación entre Poetry y Projen


## Propósito y Alcance

- **Poetry**: gestor de dependencias enfocado en proyectos Python. Facilita la instalación, actualización y resolución de versiones de paquetes, además de gestionar entornos virtuales y empaquetar proyectos para su distribución.
- **Projen**: herramienta usada para generar y automatizar la configuración de proyectos. Gestiona no solo dependencias, sino también la creación de archivos como **package.json**, **.gitignore**, **README.md**, y más.

**Conclusion**

  - Si el proyecto es solo Python y se busca *simplicidad* en la gestión de dependencias, Poetry es la mejor opción.

  - Para proyectos *más complejos* donde la automatización y consistencia son clave, Projen es más eficiente.


## Facilidad de Uso

- **Poetry**:
  - Comandos simples como:
    * **poetry init** para iniciar el proyecto y crear el arhivo *pyproject.toml*.
    * **poetry add $(cat requirements.txt)** para añadir las dependencias.
    * **poetry install** para instalar las dependencias definidas en *pyproject.toml*.
    * **poetry lock** que crea o actualiza **poetry.lock** con las versiones exactas de las dependencias.

Una ventaja que tiene Poetry es que es muy facil de modificar el archivo *pyproject.toml* por su escritura similar a un *requirements.txt*

  
- **Projen**:
 - Mayor complejidad al ser necesariuo crear un archivo de configuración TypeScript, que es *.projenrc.ts*

  - Las modificaciones se realizan usando TypeScript siendo una estructura no muy común.

**Conclusión**: 

 - Poetry es más amigable para proyectos *pequeños* y *medianos*.

 - Projen es más adecuado para proyectos *grandes* con múltiples configuraciones que requieren automatización.


## Flexibilidad y Modificación

- **Poetry**:
  - Los archivos generados pueden ser modificados directamente usando el comando **nano**.
  - Permite hacer ajustes rápidos debido a su simplicidad.
  
- **Projen**:
  - No esta enfocado en modificaciones manuales, ya que la modificación se realiza en *.projenrc.ts* y tras hecerse se debe volver a generar el proyecto con el comando **npx projen**.
  - Esto garantiza consistencia pero dificulta la corrección de pequeños errores.

**Conclusión**

 - Poetry ofrece una mayor flexibilidad para modificaciones rápidas y directas.

 - Projen asegura consistencia,pero en cambio obliga a que las modificaciones se realicen mediante el archivo de configuración *.projenrc.ts* y obliga la regeneración.


## Esfuerzo de Configuración Inicial

- **Poetry**:
  - La configuración es rápida e interactiva, donde el comando **poetry init** guía al usuario a través de la creación del archivo de configuración.
  - Es fácil añadir dependencias y gestionar versiones.

- **Projen**:
  - Se requiere crear un archivo *.projenrc.ts* en TypeScript.
  - La configuración inicial demanda más tiempo y conocimiento.

**Conclusión**: 

 - Poetry es más sencillo y rápido de configurar.

 - Projen requiere un mayor esfuerzo inicial, pero es más adecuado para configuraciones más complejas y automatizadas.

## Automatización

- **Poetry**:
  - Se centra exclusivamente en la gestión de dependencias. 
  - No automatiza la creación de archivos o scripts adicionales.

- **Projen**:
  - Projen es más potente en términos de automatización, ya que genera automáticamente archivos como *.gitignore*, *package.json*, entre otros, y mantiene la consistencia en todo el proyecto.
  - Los cambios realizados se reflejan en todos los archivos relacionados cuando se ejecuta *npx projen*.

**Conclusión**

 - Poetry al esta más enfocado en dependencias no ofrece la misma amplitud de automatización más allá de la gestión de las mismas.
 
 - Projen destaca por su capacidad de automatización en proyectos grandes


## Tabla comparativa

| **Categoría**                | **Poetry**                                                                                       | **Projen**                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Propósito y Alcance**       | Si el proyecto es solo Python y se busca *simplicidad* en la gestión de dependencias, Poetry es la mejor opción. | Para proyectos *más complejos* donde la automatización y consistencia son clave, Projen es más eficiente. |
| **Facilidad de Uso**          | Poetry es más amigable para proyectos *pequeños* y *medianos*.                                    | Projen es más adecuado para proyectos *grandes* con múltiples configuraciones que requieren automatización. |
| **Flexibilidad y Modificación**| Poetry ofrece una mayor flexibilidad para modificaciones rápidas y directas.                    | Projen asegura consistencia, pero requiere que las modificaciones se realicen mediante el archivo *.projenrc.ts* y obliga la regeneración. |
| **Esfuerzo de Configuración Inicial** | Poetry es más sencillo y rápido de configurar.                                                | Projen requiere un mayor esfuerzo inicial, pero es más adecuado para configuraciones más complejas y automatizadas. |
| **Automatización**            | Poetry, al estar más enfocado en dependencias, no ofrece la misma amplitud de automatización más allá de la gestión de las mismas. | Projen destaca por su capacidad de automatización en proyectos grandes.                                  |




